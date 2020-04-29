import mysql.connector
from mysql.connector import errorcode
from src.config import db_conn

class MyDB(object):

    def __init__(self, datbase_connection_paramaters=db_conn):
        try:
            self.db_conn_params = datbase_connection_paramaters
            self.database_connection = mysql.connector.connect(**datbase_connection_paramaters)
            self.cursor = self.database_connection.cursor(buffered=True)
        except mysql.connector.Error as err:
            print("Unable to connect to database, ERROR: {}\n\n".format(err))
            raise

    def query(self, query, params=''):
        try:
            if params != '':
                # print('executing parameters')
                return self.cursor.execute(query, params)
            else:
                # print('executing without paramters')
                return self.cursor.execute(query)
        except mysql.connector.Error as err:
            if err.errno == errorcode.CR_SERVER_GONE_ERROR or err.errno == errorcode.CR_SERVER_LOST or \
                    err.errno == errorcode.CR_SERVER_LOST_EXTENDED:
                # TODO: Log this loss of connection to database
                """The database connection was lost, attempt to reconnect and redo the query"""
                print('The client has lost connection to the mysql server, errno: {}'.format(err.errno))
                self.database_connection.reconnect()
                query(query, params)
            else:
                # Some other error occurred during execution of command, reraising error, this is usually a
                # programming problem
                raise

    def commit(self):
        try:
            self.database_connection.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.CR_SERVER_GONE_ERROR or err.errno == errorcode.CR_SERVER_LOST or \
                    err.errno == errorcode.CR_SERVER_LOST_EXTENDED:
                # TODO: Log this loss of connection to database
                """The database connection was lost, attempt to reconnect and redo the query"""
                print('The client has lost connection to the mysql server, errno: {}'.format(err.errno))
                self.database_connection.reconnect()
                self.database_connection.commit()
            else:
                # Some other error occurred during the commit, reraising error, this is usually a
                # programming problem
                raise


    def get_last_row_id(self):
        # This method does not issue a request to the database
        return self.cursor.lastrowid

    def get_row_count(self):
        return self.cursor.rowcount

    def fetchall(self):
        # This method does not issue a request to the database
        return self.cursor.fetchall()


    def __del__(self):
        try:
            # sometimes the connections may have closed unexpectedly, and will generate an error if we try to destroy
            # them again
            self.cursor.close()
            self.database_connection.close()
        except Exception as err:
            print(err)