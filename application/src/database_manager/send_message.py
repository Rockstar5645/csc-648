import mysql.connector
from datetime import datetime 

def send_message(sender_id, media_id, subject, message_body, db):

    try:
        get_owner_id_query = ("SELECT owner_id FROM digital_media WHERE media_id=%s")
        db.query(get_owner_id_query, (media_id,))
    except mysql.connector.Error as err:
        # print("Internal server error with database: {}".format(err))
        # FIXME: log this potentially fatal error
        # TODO: what other errors could occur with the connection object?
        error_message = {
            'status': 'fail',
            'msg': 'Internal database error: {}'.format(err)
        }
        return error_message

    if db.get_row_count() == 0:
        # Some sort of logic error, the user is attempting to send a message for a media item that does not exist
        # potential insecure direct object reference 
        success_message = {
            'status': 'no_media',
            'msg': 'There doesnt exist any media item with that media idea',
        }
        return success_message

    for recipient_id in db.fetchall()[0]:

        add_message = ("INSERT INTO messages "
                      "(time_stamp, sender, recipient, message_content, media_id, seen, subject) "
                      "VALUES (%s, %s, %s, %s, %s, %s, %s)")

        time_stamp = datetime.now()

        values_to_be_inserted = (time_stamp, sender_id, recipient_id, message_body, media_id, False, subject)

        try:
            db.query(add_message, values_to_be_inserted)
            db.commit()
            success_message = {
                'status': 'success',
            }
            return success_message
        except mysql.connector.Error as err:
            # FIXME: log this potentially fatal error
            # TODO: what other errors could occur with the database connection object?
            error_message = {
                'status': 'fail',
                'message': "Failed to send message: {}".format(err)
            }
            return error_message
                

            