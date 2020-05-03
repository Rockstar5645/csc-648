import mysql.connector

def get_message_by_id(message_id, requester_id, db):

    try:

        # get the specific message
        get_message_by_id_query = (
            "SELECT m.subject, m.time_stamp, m.message_body, m.recipient, m.media_id,"
            " u.username AS sender"
            " FROM messagxes m"
            " JOIN user u ON m.sender=u.user_id"
            " WHERE m.message_id=%s"
        )

        db.query(get_message_by_id_query, (message_id,))

        if db.get_row_count() == 0:
            # The user doesn't have any messages
            status_msg = {
                'status': 'invalid-message-id',
                'msg': 'There is not message with that message id'
            }
            return status_msg

        subject, time_stamp, message_body, recipient_id, media_id, sender = db.fetchall()[0]

        # check if the user has permission to view this message
        if recipient_id == requester_id:
            # update the seen status, to true
            update_seen_status_query = "UPDATE messages SET seen=True WHERE message_id=%s"
            db.query(update_seen_status_query, (message_id,))
            db.commit()

            status_msg = {
                'status': 'success',
                'subject': subject,
                'time_stamp': time_stamp,
                'sender': sender,
                'message_body': message_body,
                'media_id': media_id
            }

            return status_msg
        else:
            status_msg = {
                'status': 'unauthorized'
            }
            return status_msg

    except mysql.connector.Error as err:
        # print("Internal server error with database: {}".format(err))
        # FIXME: log this potentially fatal error
        # TODO: what other errors could occur with the connection object?
        error_message = {
            'status': 'fail',
            'msg': 'Internal database error: {}'.format(err)
        }
        return error_message