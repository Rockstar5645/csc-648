import redis
import time

local_redis = {
    'host': '10.0.0.188',
    'port': '6379',
    'socket_timeout': 3
}

r = redis.Redis(**local_redis)

def set_value():
    if (r.setex('abc', 3, 3)):
        print('successfully set the value')
    else:
        print('unsuccessful')
    print(r.get('abc'))
    print(r.ttl('abc'))
    print(r.exists('abc'))

def get_value():

    try:
        with r.pipeline() as pipe:
            pipe.multi()
            pipe.get('abc')
            pipe.expire('abc', 2)
            gotten_val = pipe.execute()

        print('value retrieved from redis server')
        print(gotten_val)
        print(r.get('abc'))
        print(r.ttl('abc'))
        print(r.exists('abc'))

        if (gotten_val[0] is None):
            print('The value of abc is no longer on the server')

        if (r.exists('abc') == 0):
            print('Checked existence, no longer there')

    except redis.exceptions.TimeoutError as err:
        print('Redis connection error: {}'.format(err))

set_value()
get_value()
time.sleep(3)
get_value()