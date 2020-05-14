


def get_user_data(user_id, db):
    db.query("SELECT * FROM user WHERE `user_id` = %s", (user_id,))
    data = db.fetchall()
    db.commit()
    return data