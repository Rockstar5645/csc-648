import redis
from src.config import redis_conn

def get_redis_con():
    if redis_conn['mode'] == 'prod':
        return redis.Redis(host=redis_conn['host'], port=redis_conn['port'])
    else:
        rco = MyRLocal()
        return rco

class MyRLocal(object):

    def __init__(self):
        self.key_val_map = {}

    def set(self, key, val):
        self.key_val_map[key] = val





