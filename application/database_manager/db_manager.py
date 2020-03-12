import sqlalchemy
from sqlalchemy import create_engine
from models import User, create_table
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:apples@localhost:3306/snapster')

create_table(engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')

Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()

session.commit()

print(our_user)

print(ed_user is our_user)

