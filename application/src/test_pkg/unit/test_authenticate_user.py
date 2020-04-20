import pytest
from src.database_manager.database_connection import MyDB
from src.database_manager.add_user import  add_user
from src.database_manager.authenticate_user import authenticate_user


user_entries = (pytest.param(
                    'rockstar55', 'akhilhello@gmail.com', 'some_pass', id="first"
                ),
                pytest.param(
                    '27jlvkj010', 'ja;ksvj209384', 'vnhkj12304809asp98hao3wjeoiawrioa;sejrlikj*&^(*&%%$#$%', id="second"
                ),
                pytest.param(
                    'spongebob2987', 'sponge@bikini.bottom', 'the_sea_bear',
                    id="third"
                ))

@pytest.fixture(params=user_entries)
def users(request):
    print(request.param)
    return request.param

@pytest.fixture()
def init_db_user(users):
    db = MyDB()

    # add a test user into the database
    status_message = add_user(username, email, password, db)
    user_id = status_message['user_id']

    initialized_user_entry = {
        'user_id': user_id,
        'username': username,
        'email': email,
        'password': password
    }

    yield user_id, username, email, password, db

    db.query('DELETE FROM user WHERE user_id=(%s)', (user_id,))
    db.commit()


def test_authenticate_valid_user(init_db_user):
    user_id, username, email, password_plain, db = init_db_user

    status_message = authenticate_user(username, email, password_plain, db)

    assert status_message['status'] == 'success'
    assert status_message['login'] == 'success'

    assert user_id == status_message['user_id']

def test_authenticate_invalid_user(init_db, init_users):
    db = init_db
    username = init_users['username']
    email = init_users['email']
    password_plain = init_users['password']

    status_message = authenticate_user(username, email, password_plain, db)

    assert status_message['status'] == 'success'
    assert status_message['login'] == 'failed'
