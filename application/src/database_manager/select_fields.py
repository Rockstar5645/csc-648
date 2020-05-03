


def get_media_type_select_field(conn):
    # this returns the categories for a select field in a form
    conn.query("SELECT * FROM media_types")
    data = conn.fetchall()
    conn.commit()
    # make a usable list of tuples for select field
    media_types = [(c[0], c[1]) for c in data]
    return media_types

def get_category_select_field(conn):
    # this returns the categories for a select field in a form
    conn.query("SELECT * FROM categories")
    data = conn.fetchall()
    conn.commit()
    # make a usable list of tuples for select field
    cats = [(c[0], c[1]) for c in data]
    return cats