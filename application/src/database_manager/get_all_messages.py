import mysql.connector

def get_all_messages(user_id, db):
    try:
        get_all_messages_query = (
            "SELECT m.message_id, m.subject, m.message_body, m.time_stamp,"
            " u.username AS sender, m.seen"
            " FROM messages m"
            " JOIN user u ON m.sender=u.user_id"
            " WHERE m.recipient=%s"
            " ORDER BY m.time_stamp DESC")

        db.query(get_all_messages_query, (user_id,))
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
        # The user doesn't have any messages
        status_msg = {
            'status': 'no-messages'
        }
        return status_msg
    else:
        message_list = []
        for (message_id, subject, message_body, time_stamp, sender, seen) in db.fetchall():
            if seen == 0:
                seen = False
            else:
                seen = True
            message = {
                'message-id': message_id,
                'subject': subject,
                'time_stamp': time_stamp,
                'message_body': message_body,
                'sender': sender,
                'seen': seen
            }
            message_list.append(message)

        status_msg = {
            'status': 'success',
            'message-list': message_list
        }
        return status_msg


