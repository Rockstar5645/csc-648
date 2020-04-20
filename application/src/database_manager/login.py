from src.database_manager.generate_session import generate_session
from src.database_manager.authenticate_user import authenticate_user

def login(username, password_plain, ip_address, db, r):
    status_msg = authenticate_user(username, password_plain, db)

    if status_msg['status'] == 'database_error':
        # the authentication attempt failed because of a database server error
        err_msg = {
            'status': 'fail'
        }
        return err_msg
    elif status_msg['status'] == 'success':     # the authentication procedure ran sucessfully
        if status_msg['login'] == 'success':    # the user entered valid credentials
            # attempt to generate a session for the user
            success_message = generate_session(status_msg['user_id'], r)
            if success_message['status'] == 'success':
                # a valid session was generated for the user, the login procedure was sucessful
                return success_message
            else:
                # there was an error generating the session for the user
                err_msg = {
                    'status': 'fail'
                }
                return err_msg
        elif status_msg['login'] == 'failed':
            # the user entered the incorrect login credentials 
            err_msg = {
                'status': 'invalid'
            }
            return err_msg
