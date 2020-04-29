import redis
from src.config import session_duration


# this method is called to check if the user is in a valid session, and retrieve the userid of that user
def get_session_id(session_token, r):
    try:
        # pipelines ensure there is only one round trip to the server for multiple redis commands
        # pipelines are also used to implement transactions
        with r.pipeline() as pipe:  # open a redis pipeline with the resource manager
            pipe.multi()    # indicates the start of a multi part transaction issued to the redis server
            pipe.get(session_token) # retrieve session token entry if exists
            pipe.expire(session_token, session_duration)    # reset session token expiration if session token exists
            pipe_return_value = pipe.execute()     # execute pipeline

        if pipe_return_value[1] is True:
            # session is still activate, and we have the session_id
            user_id = pipe_return_value[0].decode('utf-8')
            print('value of {} was successfully retreived'.format(user_id))
            success_msg = {
                'status': 'success',
                'user_id': user_id
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
