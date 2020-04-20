import mysql.connector
from src.config import db_conn
import time

del db_conn['database']

cnx = mysql.connector.connect(**db_conn)
cursor = cnx.cursor(buffered=True)
a = cnx.connection_id
print('first connection id {}'.format(a))
# cnx.disconnect()

cnx2 = mysql.connector.connect(**db_conn)
cursor2 = cnx2.cursor(buffered=True)
print('second connection id {}'.format(cnx2.connection_id))

cursor2.execute('kill {}'.format(cnx.connection_id))    # simulate database connection loss
cnx2.commit()

try:
    cursor.execute('use test')
except Exception as e:
    print('somethings wrong here')