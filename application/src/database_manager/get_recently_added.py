import mysql.connector

def get_recently_added(db):
    try:
        
        db.query("SELECT * FROM digital_media WHERE approval = 1 ORDER BY media_id DESC LIMIT 6")
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