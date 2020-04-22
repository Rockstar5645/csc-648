import pytest
from src.database_manager.add_user import  add_user
import bcrypt
import base64
import hashlib


def test_add_user(init_db_add_user, request, users):
    db = init_db_add_user
    username, email, password = users
    status_msg = add_user(username, email, password, db)
    user_id = status_msg['user_id']
    request.node.user_id = user_id

    assert status_msg['status'] == 'success'
    assert user_id > 0
    db.query('SELECT * FROM user WHERE user_id=(%s)', (user_id,))
    user_entry = db.fetchall()

    assert len(user_entry) == 1
    (user_id_db, first_name, last_name, email_db, phone_number, username_db, password_db) = user_entry[0]

    assert user_id_db == user_id
    assert first_name is None
    assert last_name is None
    assert email_db == email
    assert phone_number is None
    assert username_db == username
    assert bcrypt.checkpw(base64.b64encode(hashlib.sha256(password.encode('utf-8')).digest()),
                          password_db.encode('utf-8'))


def test_already_existing_user(init_db_add_user, request, username, email, password):
    pass




