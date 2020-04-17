import mysql.connector
from src.config import db_conn
import sys

class MyDB(object):

    def __init__(self):
        try: 
            # self._db_connection = mysql.connector.connect(user=db_conn['user'], password=db_conn['password'],
            #                      host=db_conn['host'], database=db_conn['database'])
            self._db_connection = mysql.connector.connect(**db_conn)
            self._db_cur = self._db_connection.cursor(buffered=True)
            
        except mysql.connector.Error as err:
            print("\n\n")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!!     UNABLE TO CONNECT TO DATABASE     !!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("\n\n")
            print("ERROR: {}\n\n".format(err))
            sys.exit()

    def get_last_row_id(self):
        return self._db_cur.lastrowid

    def check_connection(self):
        if self._db_connection.is_connected() is False:
            print('We have lost connection to the database, attempting to reconnect')
            self._db_cur.close()
            self._db_connection.close()
            self._db_connection = mysql.connector.connect(**db_conn)
            self._db_cur = self._db_connection.cursor(buffered=True)

    def query(self, query, params=''):
        self.check_connection()

        if params != '':
            # print('executing parameters')
            return self._db_cur.execute(query, params)
        else:
            # print('executing without paramters')
            return self._db_cur.execute(query)

    def fetchall(self):
        self.check_connection()
        return self._db_cur.fetchall()

    def commit(self):
        self._db_connection.commit()

    def __del__(self):
        self._db_cur.close()
        self._db_connection.close()