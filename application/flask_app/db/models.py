from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

#######################################################
#                  BASE OBJECT CLASS                  #
#######################################################
Base = declarative_base()


#######################################################
#              Team_Member Class Model                #
#######################################################
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
