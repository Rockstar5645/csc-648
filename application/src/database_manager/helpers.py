def get_media_type(conn, id):
    conn.query("SELECT `media_type` FROM media_types WHERE `media_type_id` = %s", (id,))
    data = conn.fetchall()
    conn.commit()
    return data

def get_category_type(conn, id):
    conn.query("SELECT `category` FROM categories WHERE `category_id` = %s", (id,))
    data = conn.fetchall()
    conn.commit()
    return data