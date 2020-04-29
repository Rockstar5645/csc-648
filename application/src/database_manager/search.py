


def search(conn, term, category, media_type, startsat, perpage):

    q = Q_Container(conn, term, category, media_type, startsat, perpage)

    if term == '':
        result = no_term_search(q)
        
    else:
        result = term_search(q)

    return check(q, result)

def term_search(q):
    if q.category == 'all' and q.media_type == 'all':
        return term_query(q)
    elif q.category == 'all' and q.media_type is not 'all':
        return term_media_query(q)
    else:
        return term_category_query(q)

def no_term_search(q):
    if q.category == 'all' and q.media_type == 'all':
        return get_all_table(q)
    elif q.category == 'all' and q.media_type is not 'all':
        return get_all_media_type(q)
    else:
        return get_all_category(q)

def term_query(q):
    q.conn.query(
                "SELECT * "
                "FROM digital_media "
                "WHERE `name` LIKE %s OR `description` LIKE %s "
                "LIMIT %s, %s",
                ("%" + q.term + "%","%" + q.term + "%",  q.startsat, q.perpage)
            )
    data = q.conn.fetchall()
    q.conn.commit()
    return data

def term_media_query(q):
    q.conn.query(
                "SELECT * "
                "FROM digital_media "
                "WHERE (`name` LIKE %s OR `description` LIKE %s) AND media_type LIKE %s LIMIT %s, %s",
                ("%" + q.term + "%","%" + q.term + "%", "%" + q.media_type, q.startsat, q.perpage)
            )
    data = q.conn.fetchall()
    q.conn.commit()
    return data

def term_category_query(q):
    q.conn.query(
                "SELECT * "
                "FROM digital_media "
                "WHERE (`name` LIKE %s OR `description` LIKE %s) AND category_id LIKE %s LIMIT %s, %s",
                ("%" + q.term + "%","%" + q.term + "%", "%" + q.category, q.startsat, q.perpage)
        )
    data = q.conn.fetchall()
    q.conn.commit()
    return data
        

def get_all_table(q):
    q.conn.query("SELECT * FROM digital_media LIMIT %s, %s", (q.startsat, q.perpage))
    data = q.conn.fetchall()
    q.conn.commit()
    return data

def get_all_media_type(q):
    q.conn.query("SELECT * FROM digital_media WHERE media_type_id LIKE %s LIMIT %s, %s", ("%" + q.media_type + "%", q.startsat, q.perpage))
    data = q.conn.fetchall()
    q.conn.commit()
    return data

def get_all_category(q):
    q.conn.query("SELECT * FROM digital_media WHERE category_id LIKE %s LIMIT %s, %s", ("%" + q.category + "%", q.startsat, q.perpage))
    data = q.conn.fetchall()
    q.conn.commit()
    return data

def check(q, result):
    if len(result) == 0:
        print('SEARCH: no matches, getting whole table')
        if q.category is not 'all':
            result = get_all_category(q)
        elif q.media_type is not 'all':
            result = get_all_media_type(q)
        else:
            result = get_all_table(q)
    return result

class Q_Container(object):

    def __init__(self, conn, term='', category='all', media_type='all', startsat=0, perpage=12):
        self.conn=conn
        self.term = term
        self.category = category
        self.media_type = media_type
        self.startsat = startsat
        self.perpage = perpage
