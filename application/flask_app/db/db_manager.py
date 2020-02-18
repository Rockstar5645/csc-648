from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

############################################
#             Database Manager             #
############################################
class DB_Manager(object):

    def __init__(self):
        self.engine = create_engine(db_conn, convert_unicode=True)
        self.db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=self.engine))
        self.Base = declarative_base()
        self.Base.query = self.db_session.query_property()

    def init_db(self):
        # import all modules here that might define models so that
        # they will be registered properly on the metadata.  Otherwise
        # you will have to import them first before calling init_db()
        import flask_app.db.models
        self.Base.metadata.create_all(bind=self.engine)