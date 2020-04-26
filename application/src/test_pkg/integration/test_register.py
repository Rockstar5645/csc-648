import pytest


@pytest.fixture()
def init_db_register(init_db_add_user, init_redis_gen_session, request):
    db = init_db_add_user
    r = init_redis_gen_session

    yield db, r

