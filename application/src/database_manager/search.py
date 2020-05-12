
'''
digital media index:
    0 - digital media id
    1 - owner_id
    2 - name
    3 - description
    4 - file_path
    5 - thumbnail_path
    6 - category_id
    7 - media_type_id
    8 - price
    9 - approved
'''

##############################################
#                Search logic                #
##############################################

def search(conn, params):
    q = Q_Container(conn, params)
    if q.term != '':
        results = term_search(q)
    else:
        results = no_term_search(q)
    results = final_check(q, results)
    return results

def term_search(q):
    results = term_query(q)
    results = filter_by_category(q, results)
    results = filter_by_type(q, results)
    results = filter_by_approved(results)
    results = filter_by_license(q, results)
    return results

def no_term_search(q):
    if q.category == '1':
        results = get_all_table(q)
    else:
        results = get_all_category(q)
    results = filter_by_type(q, results)
    results = filter_by_license(q, results)
    return results

def filter_by_category(q, results):
    if q.category == '1':
        return results
    for result in results:
        if result[6] != q.category:
            results.remove(result)
    return results

def filter_by_type(q, results):
    if len(q.media_types) == 0:
        return results
    for result in results:
        if result[7] not in q.media_types:
            results.remove(result)
    return results

def filter_by_approved(results):
    for result in results:
        if result[9] == 0:
            results.remove(result)
    return results

def filter_by_license(q, results):
    if q.license == 'all':
        return results
    elif q.license == 'free':
        for result in results:
            if result[8] > 0:
                results.remove(result)
    elif q.license == 'paid':
        for result in results:
            if result[8] == 0:
                results.remove(result)
    return results

def final_check(q, results):
    if len(results) > 0:
        return results
    else:
        if q.term == '' and q.category == '1' and len(q.media_types) == 0:
            results = get_all_table(q)
        elif q.term != '':
            results = term_query(q)
        elif q.category != '1':
            results = get_all_category(q)
            results = filter_by_category(q, results)
        elif len(q.media_types) > 0:
            results = get_all_table(q)
            results = filter_by_type(q, results)
        if len(results) == 0:
            return get_all_table(q)

        return results

##############################################
#       functions that access the db         #
##############################################

def term_query(q):
    q.conn.query(
                "SELECT * FROM digital_media WHERE `name` LIKE %s OR `description` LIKE %s", ("%" + q.term + "%","%" + q.term + "%"))
    data = q.conn.fetchall()
    q.conn.commit()
    return data

def get_all_category(q):
    q.conn.query("SELECT * FROM digital_media WHERE category_id LIKE %s", ("%" + q.category + "%"))
    data = q.conn.fetchall()
    q.conn.commit()
    return data
        

def get_all_table(q):
    q.conn.query("SELECT * FROM digital_media")
    data = q.conn.fetchall()
    q.conn.commit()
    return data

#################################################
#       Query parameter container object        #
#################################################

class Q_Container(object):

    def __init__(self, conn, params):
        self.conn = conn
        self.term = params['term']
        self.category = params['category']
        self.license = params['license']
        self.media_types = []
        if 'image_check' in params:
            self.media_types.append(1)
        if 'video_check' in params:
            self.media_types.append(2)
        if 'audio_check' in params:
            self.media_types.append(3)
        if 'document_check' in params:
            self.media_types.append(4)
