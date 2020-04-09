import bcrypt
import base64
import hashlib
import secrets
import mysql.connector

def register(username, password_plain, first_name, last_name, phone_number, email, db, r):
    add_user = ("INSERT INTO user "
                    "(first_name, last_name, email, phone_number, username, password) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")

    password = password_plain
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password).digest()), bcrypt.gensalt(14))
    # hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))

    vals = (first_name, last_name, email, phone_number, username, hashed)

    try:
        db.query(add_user, vals)
        db.commit()
    except mysql.connector.Error as err:
        # print("Failed to create user: {}".format(err))
        error_message = {
            'status': 'error',
            'message': "Failed to create user: {}".format(err)
        }
        return error_message

    user_id = db._db_cur.lastrowid

    # map the the secret token to a userid

    secret_token = secrets.token_urlsafe(100)
    r.set(secret_token, user_id)
    success_message = {
        'status': 'success',
        'token': secret_token
    }
    # print('Successfully created user {} with secret token {}'.format(user_id, secret_token))
    return success_message

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




