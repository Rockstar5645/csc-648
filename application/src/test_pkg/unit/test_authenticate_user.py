import pytest
from src.database_manager.database_connection import MyDB
from src.database_manager.authenticate_user import authenticate_user



def test_authenticate_valid_user(init_db_authenticate_user):
    user_id, username, password_plain, db = init_db_authenticate_user

    status_message = authenticate_user(username, password_plain, db)

    assert status_message['status'] == 'success'
    assert status_message['login'] == 'success'

    assert user_id == status_message['user_id']


def test_authenticate_invalid_user(init_db_authenticate_user):
    user_id, username, password_plain, db = init_db_authenticate_user

    status_message = authenticate_user(username, password_plain + 'wrong_pass', db)

    assert status_message['status'] == 'success'
    assert status_message['login'] == 'failed'
