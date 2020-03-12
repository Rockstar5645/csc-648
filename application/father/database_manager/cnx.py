import mysql.connector
from father.config import db_conn

class MyDB(object):

    def __init__(self):
        self._db_connection = mysql.connector.connect(user=db_conn['user'], password=db_conn['password'],
                                  host=db_conn['host'], database=db_conn['database'])
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params=''):
        if params != '':
            print('executing parameters')
            return self._db_cur.execute(query, params)
        else:
            print('executing without paramters')
            return self._db_cur.execute(query)
        self._db_cur.commit()

    def __del__(self):
        self._db_cur.close()
        self._db_connection.close()