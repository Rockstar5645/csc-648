from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BLOB

#######################################################
#                  BASE OBJECT CLASS                  #
#######################################################
Base = declarative_base()


#######################################################
#                 USER Class Model                    #
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


#######################################################
#              DIGITAL MEDIA Class Model              #
#######################################################

class Digital_Media(Base):
    __tablename__ = 'digital_media'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(120), unique=True)
    file = Column(BLOB)

    def __init__(self, name=None, description=None, file=None):
        self.name = name
        self.description = description
        self.file = file

    def __repr__(self):
        return '<Digital_Media %r>' % (self.name)