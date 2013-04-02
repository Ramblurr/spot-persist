from sqlalchemy import orm
import datetime
from sqlalchemy import schema, types

metadata = schema.MetaData()

message_table = schema.Table('message', metadata,
                             schema.Column('id', types.Integer,
                                            schema.Sequence('message_seq_id', optional=True),
                                            primary_key=True),
                            schema.Column('messengerId', types.Text(), nullable=False),
                            schema.Column('messengerName', types.Text(), nullable=False),
                            schema.Column('unixTime', types.Integer(), nullable=False),
                            schema.Column('messageType', types.Text(), nullable=False),
                            schema.Column('latitude', types.Float(), nullable=False),
                            schema.Column('longitude', types.Float(), nullable=False),
                            schema.Column('showCustomMsg', types.Text(), nullable=False),
                            schema.Column('dateTime', types.Text(), nullable=False),
                            schema.Column('altitude', types.Text(), nullable=False),
                            schema.Column('hidden', types.Text(), nullable=False),
                            schema.Column('messageContent', types.Text(), nullable=True),
)

class Message(object):
    pass

orm.mapper(Message, message_table)
