import bcrypt
import base64
import hashlib
import secrets
import mysql.connector
import redis
from src.config import session_duration

def login(username, password_plain, ip_address, db, r):
    query = ("SELECT user_id, username, password FROM user WHERE username=%s")

    try:
        db.query(query, (username,))
    except mysql.connector.Error as err:
        # print("Internal server error with database: {}".format(err))
        error_message = {
            'status': 'error',
            'message': 'internal-error'
        }
        return error_message

    for (user_id, username, password) in db._db_cur:
        # print(password)
        password_entered = password_plain
        password_entered = password_entered.encode('utf-8')
        if bcrypt.checkpw(base64.b64encode(hashlib.sha256(password_entered).digest()), password.encode('utf-8')):
            # password is a match
            secret_token = secrets.token_urlsafe(100)
            r.set(secret_token, user_id)

            success_message = {
                'status': 'success',
                'login': 'success',
                'token': secret_token
            }
            # print('Successfully logged in user {} with secret token {}'.format(user_id, secret_token))
            return success_message
        else:
            success_message = {
                'status': 'success',
                'login': 'failed',
            }
            # print('Unsuccessful login attempt by user {}'.format(user_id))
            return success_message




