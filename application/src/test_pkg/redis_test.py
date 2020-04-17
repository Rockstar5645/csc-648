import redis

local_redis = {
    'host': '10.0.0.188',
    'port': '6379',
    'socket_timeout': 3
}

r = redis.Redis(**local_redis)

def set_value():
    if (r.setex('abc', 60, 30)):
        print('successfully set the value')
    else:
        print('unsuccessful')

def get_value():

    try:
        with r.pipeline() as pipe:
            pipe.multi()
            pipe.get('abc')
            pipe.expire('abc', 60)
            gotten_val = pipe.execute()

        if (gotten_val[1]):
            print('value of {} was successfully set'.format(gotten_val[0].decode('utf-8')))
        else:
            print('we were not able to update the value successfully')

    except redis.exceptions.TimeoutError as err:
        print('Redis connection error: {}'.format(err))

# set_value()
get_value()

