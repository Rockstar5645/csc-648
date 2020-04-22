from src.config import session_duration
import time
from src.database_manager.generate_session import generate_session


def test_set_session_token(init_redis_gen_session, request):
    r = init_redis_gen_session

    return_message = generate_session(1, r)
    status = return_message['status']
    token = return_message['token']
    print(token)
    request.node.token_val = token

    time.sleep(2)

    assert status == 'success'
    assert 1 == int(r.get(token).decode('utf-8'))
    assert r.ttl(token) < session_duration
