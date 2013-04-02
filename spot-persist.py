#!/usr/bin/env python
#
# Copyright (C) 2013 Casey Link <unnamedrambler@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Parse SPOT data feeds in JSON format and save them to a SQL database

Usage: spot-persist.py -h
"""
import argparse, getpass
import json
import sys
from sqlalchemy import orm
from sqlalchemy import create_engine

import model

def init_db(file):
# Create an engine and create all the tables we need
    engine = create_engine('sqlite:///%s' % (file), echo=True)
    model.metadata.bind = engine
    model.metadata.create_all()

# Set up the session
    sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False,
        expire_on_commit=True)
    return orm.scoped_session(sm)

def parse(handle):

    data = json.load(handle)
    metadata = data['response']['feedMessageResponse']['feed']
    messages = data['response']['feedMessageResponse']['messages']['message']
    return metadata, messages

def populate(session, metadata, messages):

    for m in messages:
        message = model.Message()
        for k in m.keys():
            if hasattr(message, k):
                setattr(message, k, m[k])
        session.add(message)

    session.flush()
    session.commit()

def _main():
    parser = argparse.ArgumentParser(description="Utility for parsing SPOT feeds in JSON format and saving them to a SQL database")
    parser.add_argument('file', nargs='?', help='The json data to parse', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-n', '--database-name', help="The filename of the SQLite database (default: messages.db)", default='messages.db')
    args = parser.parse_args()

    metadata, messages = parse(args.file)
    print "Parsing %s messages from feed %s (device: %s, id: %s)" % (len(messages), metadata['name'], metadata['name'], metadata['id'])
    session = init_db(args.database_name)
    populate(session, metadata, messages)

    # for m in msg_q:
    #     print m.latitude, m.longitude


    # msg_q = session.query(model.Message)

if __name__ == '__main__':
    _main()
