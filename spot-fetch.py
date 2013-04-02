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
Fetches SPOT message feeds from findmespot.com

Usage: spot-fetch.py -h
"""
import argparse, getpass
import urllib2

BASE_FEED_URL = "https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/%s/%s.%s"
TYPE_LATEST = "latest"
TYPE_ALL = "message"
FORMAT_JSON = "json"
FORMAT_XML = "xml"
PASSWORD = "?feedPassword=%s"


def fetch_data(glid, type = TYPE_ALL, format = FORMAT_JSON, password = None):
    url = BASE_FEED_URL % (glid, type, format)

    if password:
        url += PASSWORD % (password)

    conn = urllib2.urlopen(url)
    data = conn .read()
    conn.close()
    return data

def _main():
    parser = argparse.ArgumentParser(description="Utility for fetching SPOT message feeds")
    parser.add_argument('glid', nargs=1, type=str, help="The feed id (glid) see http://faq.findmespot.com/index.php?action=showEntry&data=69")
    parser.add_argument('-t', '--type', choices=[TYPE_ALL, TYPE_LATEST], help="The type of feed to fetch (default: message)", default=TYPE_ALL)
    parser.add_argument('-f', '--format', choices=['json', 'xml'], help="The desired output format (default: json)", default='json')
    parser.add_argument('-p', '--password', action='store_true', help="Prompts for the feed's password interactively")
    parser.add_argument('-P', '--no-prompt-password', help="The feed's password read from the arguments")
    args = parser.parse_args()

    password = None
    if args.password:
        password = getpass.getpass()
    elif args.no_prompt_password:
        password = args.no_prompt_password

    print fetch_data(args.glid[0], args.type, args.format, password)

if __name__ == '__main__':
    _main()
