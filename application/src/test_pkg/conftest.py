import pytest
import redis
from src.config import redis_conn
from src.database_manager.database_connection import MyDB
from src.database_manager.add_user import  add_user

user_entries = [
    ('rockstar55', 'akhilhello@gmail.com', 'some_pass'),
    ('27jlvkj010', 'ja;ksvj209384', 'vnhkj12304809asp98hao3wjeoiawrioa;sejrlikj*&^(*&%%$#$%'),
    ('spongebob2987', 'sponge@bikini.bottom', 'the_sea_bear')
]

user_entry_ids = [
    user_entry[0] for user_entry in user_entries
]

@pytest.fixture(params=user_entries, ids=user_entry_ids)
def users(request):
    return request.param


@pytest.fixture()
def init_db_add_user(request):
    db = MyDB()
    yield db

    user_id = request.node.user_id
    db.query('DELETE FROM user WHERE user_id=(%s)', (user_id,))
    db.commit()

@pytest.fixture()
def init_db_authenticate_user(users):
    db = MyDB()
    username, email, password = users
    # add a test user into the database
    status_message = add_user(username, email, password, db)
    user_id = status_message['user_id']

    yield user_id, username, password, db

    db.query('DELETE FROM user WHERE user_id=(%s)', (user_id,))
    db.commit()


@pytest.fixture()
def init_redis_gen_session(request):
    r = redis.Redis(**redis_conn)
    yield r

    # remove token from redis
    r.delete(request.node.token_val)
