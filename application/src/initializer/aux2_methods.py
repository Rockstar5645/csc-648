from src.database_manager.add_user import add_user
from src.database_manager.send_message import send_message
import time

def create_test_users(db):
    # creating test users
    bcrypt_rounds = 6
    print('Inserting list of test users')
    add_user('rockstar22', 'rockstar@sfsu.edu', 'apples', db, bcrypt_rounds)   # user id 1
    add_user('spongebob', 'sponge@sfsu.edu', 'apples', db, bcrypt_rounds)      # user id 2
    add_user('patrick', 'patrick@sfsu.edu', 'apples', db, bcrypt_rounds)       # user id 3
    add_user('squidward', 'squid@sfsu.edu', 'apples', db, bcrypt_rounds)       # user id 4
    add_user('sandy', 'sand@sfsu.edu', 'apples', db, bcrypt_rounds)            # user id 5
    print('Test users added')

def simulate_test_messages(db):
    # send some test messages between the users
    print('Sending test messages between users')
    send_message(1, 2, 'from 1', 'I want to buy 2', db)
    time.sleep(1)
    send_message(2, 3, 'from 2', 'I want to buy 3', db)
    time.sleep(1)
    send_message(3, 4, 'from 3', 'I want to buy 4', db)
    time.sleep(1)
    send_message(4, 1, 'from 4', 'I want to buy 1', db)
    time.sleep(1)
    send_message(5, 1, 'from 5', 'I want to buy 1', db)
    time.sleep(1)
    send_message(1, 3, 'from 1', 'I want to buy 3', db)
    time.sleep(1)
    send_message(2, 4, 'from 2', 'I want to buy 4', db)
    time.sleep(1)
    send_message(3, 1, 'from 3', 'I want to buy 1', db)
    time.sleep(1)
    send_message(4, 1, 'from 4', 'I want to buy 1', db)
    time.sleep(1)
    send_message(5, 2, 'from 5', 'I want to buy 2', db)
    print('List of test messages initialized')