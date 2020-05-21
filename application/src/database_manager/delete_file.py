import mysql.connector

def delete_file(media_id, db):
    try:
        delete_digital_media = ("DELETE FROM digital_media WHERE media_id = %s", (media_id))
        db.query(delete_digital_media, (media_id,))
    except mysql.connector.Error as err:
        # print("Internal server error with database: {}".format(err))
        # FIXME: log this potentially fatal error
        # TODO: what other errors could occur with the connection object?
        error_message = {
            'status': 'fail',
            'msg': 'Internal database error: {}'.format(err)
        }
        return error_message
    db.commit()