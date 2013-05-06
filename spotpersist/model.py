from sqlalchemy import schema, types
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = schema.MetaData()

CHECKIN = "CHECKIN"
CUSTOM = "CUSTOM"
TRACK = "TRACK"

class Message(Base):
    __tablename__ = "messages"
    id = schema.Column(types.Integer, primary_key=True)
    messengerId = schema.Column(types.Text(), nullable=False)
    latitude = schema.Column(types.Float(), nullable=False)
    longitude = schema.Column(types.Float(), nullable=False)
    dateTime = schema.Column(types.Text(), nullable=False)
    unixTime = schema.Column(types.Integer(), nullable=False)
    altitude = schema.Column(types.Text(), nullable=True)
    messengerName = schema.Column(types.Text(), nullable=False)
    messageType = schema.Column(types.Text(), nullable=False)
    showCustomMsg = schema.Column(types.Text(), nullable=False)
    hidden = schema.Column(types.Text(), nullable=False)
    messageContent = schema.Column(types.Text(), nullable=True)

    def simple(self):
        return ( self.longitude, self.latitude )

    def __repr__(self):
        return '<Point %s,%s:%s>' %(self.latitude, self.longitude, self.messageType)


class CartoDbSyncEntry(Base):
    __tablename__ = "cartodb_log"
    id = schema.Column(types.Integer, primary_key=True)
    point_id = schema.Column(types.Integer, schema.ForeignKey('messages.id'))
    timestamp = schema.Column(types.DateTime)
