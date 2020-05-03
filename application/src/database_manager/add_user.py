import bcrypt
import base64
import hashlib
import mysql.connector
from mysql.connector import errorcode


def add_user(username, email, password, db, bcrypt_rotate=14):
    # user_id (auto increment), first_name, last_name, email, phone_number, username, password
    add_user_query = ("INSERT INTO user "
                      "(username, email, password) "
                      "VALUES (%s, %s, %s)")

    password = password.encode('utf-8')  # encode it into a binary format for bcrypt to process

    # bcrypt only accepts passwords that have a length upto 80 characters, so limit the size of the password we pass
    # to the bcrypt function, we get the sha256 hash and base64 encode that
    # then generate the bcrypt hash of our password and salt, using 14 rounds (approximately 1.5 seconds)
    hashed = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password).digest()), bcrypt.gensalt(bcrypt_rotate))

    # this is the other way to do it, but it will break if user enters password greater than 80 characters
    # hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))

    values_to_be_inserted = (username, email, hashed)

    try:
        db.query(add_user_query, values_to_be_inserted)
        db.commit()
        # now we establish the user's session
        user_id = db.get_last_row_id()  # grab the userid of the user just created
        success_message = {
            'status': 'success',
            'user_id': user_id
        }
        return success_message
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DUP_ENTRY:
            # The user picked a username that already exists
            error_message = {
                'status': 'username_exists'
            }
            return error_message
        else:
            # FIXME: log this potentially fatal error
            # FIXME: distinguish between database connection error, and username already exists error
            # TODO: what other errors could occur with the database connection object?
            # print("Failed to create user: {}".format(err))
            error_message = {
                'status': 'database_error',
                'message': "Failed to create user: {}".format(err)
            }
            return error_message