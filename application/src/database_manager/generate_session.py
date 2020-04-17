import secrets
import redis
from src.config import session_duration


def generate_session(user_id, r):
    # generate a secret token
    secret_token = secrets.token_urlsafe(100)

    # map the secret token to a userid, in our redis database, and set the duration of the session (amount of time
    # before the session token expires) atomically
    try:
        if r.setex(secret_token, session_duration, user_id) is True:
            success_message = {
                'status': 'success',
                'token': secret_token
            }
            # print('Successfully created user {} with secret token {}'.format(user_id, secret_token))
            return success_message
        else:
            # FIXME: We need to deal with potential connection termination errors, why would this ever happen?
            error_message = {
                'status': 'redis_error',
                'message': 'Failed to set the session token in the redis server, redirect users to login'
            }
            return error_message
    except redis.exceptions.TimeoutError as err:
        # TODO: what other errors could possibly happen with the redis connection object r
        # FIXME: We need to deal with potential connection termination errors
        print('Redis connection error: {}'.format(err))
        error_message = {
            'status': 'redis_error',
            'message': 'Failed to set the session token in the redis server, redis connection timed out'
        }
        return error_message
