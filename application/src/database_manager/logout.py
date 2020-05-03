import redis


"""
THe following method removes the user's session token from the redis store, effectively performing a 
'logout'    
"""

def logout(session_token, r):
    try:
        num = r.delete(session_token)

        if num == 1:
            # the user's session token and only the user's session token was deleted
            sucess_message = {
                'status': 'success'    
            }
            return sucess_message
        elif num == 0:
            # the user's session token didn't exist
            status = {
                'status': 'unauthorized', 
                'msg': 'The user attempting to log out is not in a valid session'
            }
            return status
        else:
            # some other unkown database error
            status = {
                'status': 'unknown',
                'msg': 'This is an invalid condition, the number of deleted keys was {}'.format(num)
            }
            return status
    except redis.exceptions.TimeoutError as err:
        print('Redis connection error: {}'.format(err))
        # FIXME: Implement logic to deal with this potentially fatal issue
        error_message = {
            'status': 'fail',
            'msg': 'Redis connection error: {}'.format(err)
        }
        return error_message
