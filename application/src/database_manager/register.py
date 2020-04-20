from src.database_manager.add_user import add_user
from src.database_manager.generate_session import generate_session

def register(username, email, password, db, r):

    # attempt to add the new user to the database
    status_msg = add_user(username, email, password, db)

    if status_msg['status'] == 'success':
        # the new user was added successfully
        session_msg = generate_session(status_msg['user_id'], r)
        if session_msg['status'] == 'success':
            # the user was added and the session was generated successfully
            return session_msg
        elif session_msg['status'] == 'redis_error':
            # the user was added to the database, but we weren't able to generate a valid session token
            err_msg = {
                'status': 'user-added'
            }
            return err_msg
    elif status_msg['status'] == 'database_error':
        err_msg = {
            'status': 'fail'
        }
        return err_msg

