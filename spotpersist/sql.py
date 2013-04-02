from sqlalchemy import orm
from sqlalchemy import create_engine

from . import model

debug = False
session = None

def init_db(db_url):
    global session
    # Create an engine and create all the tables we need
    engine = create_engine(db_url, echo=debug)
    model.metadata.bind = engine
    model.metadata.create_all()

    # Set up the session
    sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False,
        expire_on_commit=True)
    session = orm.scoped_session(sm)

def populate(messages, update = False):

    if session is None:
        raise Exception("database not initialized")

    for m in messages:
        message = model.Message()
        for k in m.keys():
            if hasattr(message, k):
                setattr(message, k, m[k])
        if update:
            session.merge(message)
        else:
            session.add(message)

    session.flush()
    session.commit()

