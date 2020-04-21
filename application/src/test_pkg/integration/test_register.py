import pytest

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
def init_db_user(users):
    db = MyDB()
    username, email, password = users
    # add a test user into the database
    status_message = add_user(username, email, password, db)
    user_id = status_message['user_id']

    yield user_id, username, password, db

    db.query('DELETE FROM user WHERE user_id=(%s)', (user_id,))
    db.commit()