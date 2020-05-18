import mysql.connector

def get_user_digital_media(user_id, db):
    try:
        
        db.query("SELECT * FROM digital_media WHERE owner_id = %s", (user_id,))
    except mysql.connector.Error as err:
        # print("Internal server error with database: {}".format(err))
        # FIXME: log this potentially fatal error
        # TODO: what other errors could occur with the connection object?
        error_message = {
            'status': 'fail',
            'msg': 'Internal database error: {}'.format(err)
        }
        return error_message

    return db.fetchall()
        