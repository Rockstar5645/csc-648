import pytest
import redis
from src.config import redis_conn
from src.config import session_duration
import time
from src.database_manager.generate_session import generate_session

@pytest.fixture()
def init_redis():
    r = redis.Redis(**redis_conn)
    yield r


def test_set_session_token(init_redis):
    r = init_redis

    return_message = generate_session(1, r)
    status = return_message['status']
    token = return_message['token']

    time.sleep(2)

    assert status == 'success'
    assert 1 == int(r.get(token).decode('utf-8'))
    assert r.ttl(token) < session_duration

    r.delete(token)
