import redis
from src.config import session_duration


# this method is called to check if the user is in a valid session
def validate_session(session_token, r):
    try:
        # pipelines ensure there is only one round trip to the server for multiple redis commands
        # pipelines are also used to implement transactions
        with r.pipeline() as pipe:  # open a redis pipeline with the resource manager
            pipe.multi()    # indicates the start of a multi part transaction issued to the redis server
            pipe.get(session_token) # retrieve session token entry if exists
            pipe.expire(session_token, session_duration)    # reset session token expiration if session token exists
            gotten_val = pipe.execute()     # execute pipeline

        if (gotten_val[1]):
            print('value of {} was successfully retreived'.format(gotten_val[0].decode('utf-8')))
        else:
            print('we were not able to update the value successfully')

    except redis.exceptions.TimeoutError as err:
        print('Redis connection error: {}'.format(err))
        # FIXME: Implement logic to deal with this potentially fatal issue
        error_message = {
            'status': 'error',
            'message': 'Redis connection error: {}'.format(err)
        }
        return error_message
