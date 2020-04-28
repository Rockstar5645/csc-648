import redis
from src.config import session_duration


# this method is called to check if the user is in a valid session
def validate_session(session_token, r):
    try:
        return_val = r.expire(session_token, session_duration)    # reset session token expiration if session token
        # exists

        if return_val is True:
            print('The user is still in a valid session')
            success_msg = {
                'status': 'success'
            }
            return success_msg
        else:
            # perhaps the session is inactive, or the user tampered with the cookie value
            # TODO: maybe the user tampered with the cookie value
            print('we were not able to reset the session duration successfully')
            success_msg = {
                'status': 'invalid_token',
                'msg': 'the users session is inactive or the user tampered with the cookie value'
            }
            return success_msg

    except redis.exceptions.TimeoutError as err:
        print('Redis connection error: {}'.format(err))
        # FIXME: Implement logic to deal with this potentially fatal issue
        error_message = {
            'status': 'fail',
            'message': 'Redis connection error: {}'.format(err)
        }
        return error_message
