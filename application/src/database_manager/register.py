import bcrypt
import base64
import hashlib
import secrets
import mysql.connector
import redis
from src.config import session_duration

def register(username, email, password, db, r):

    # user_id (auto increment), first_name, last_name, email, phone_number, username, password
    add_user_query = ("INSERT INTO user "
                    "(username, email, password) "
                    "VALUES (%s, %s, %s)")

    password = password.encode('utf-8')     # encode it into a binary format for bcrypt to process

    # bcrypt only accepts passwords that have a length upto 80 characters, so limit the size of the password we pass
    # to the bcrypt function, we get the sha256 hash and base64 encode that
    # then generate the bcrypt hash of our password and salt, using 14 rounds (approximately 1.5 seconds)
    hashed = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password).digest()), bcrypt.gensalt(14))

    # this is the other way to do it, but it will break if user enters password greater than 80 characters
    # hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))

    values_to_be_inserted = (username, email, hashed)

    try:
        db.query(add_user_query, values_to_be_inserted)
        db.commit()
    except mysql.connector.Error as err:
        # TODO: log this potentially fatal error
        # TODO: distinguish between database connection error, and username already exists error
        # print("Failed to create user: {}".format(err))
        error_message = {
            'status': 'database_error',
            'message': "Failed to create user: {}".format(err)
        }
        return error_message

    # now we establish the user's session
    user_id = db.get_last_row_id() # grab the userid of the user just created
    # generate a secret token
    secret_token = secrets.token_urlsafe(100)

    # map the secret token to a userid, in our redis database, and set the duration of the session (amount of time
    # before the session token expires) atomically
    try:
        if r.setex(secret_token, session_duration, user_id) is True:
            success_message = {
                'status': 'success',
                'token': secret_token
            }
            # print('Successfully created user {} with secret token {}'.format(user_id, secret_token))
            return success_message
        else:
            error_message = {
                'status': 'redis_error',
                'message': 'Failed to set the session token in the redis server, redirect users to login'
            }
            return error_message
    except redis.exceptions.TimeoutError as err:
        # FIXME: We need to deal with potential connection termination errors
        print('Redis connection error: {}'.format(err))
        error_message = {
            'status': 'redis_error',
            'message': 'Failed to set the session token in the redis server, redis connection timed out'
        }