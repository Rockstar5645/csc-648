import mysql.connector
from application.config import db_conn
from mysql.connector import errorcode


try:
    cnx = mysql.connector.connect(user=db_conn['user'], password=db_conn['password'],
                                  host=db_conn['host'], database=db_conn['database'])
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
