import pytest
from src.database_manager import database_connection
from src.config import db_conn
import mysql.connector


@pytest.fixture()
def init_MyDB_connection():
    # establish connection to test database
    test_db_conn = dict(db_conn)
    test_db_conn['database'] = 'sanpster_remote_test'
    db = database_connection.MyDB(test_db_conn)

    yield db    # perform tests on db object

    del db  # delete the database object

@pytest.fixture()
def init_query_connection_collapse(init_MyDB_connection):
    db = init_MyDB_connection
    db.query('drop table if exists pet')

    test_db_conn = dict(db_conn)

    cnx = mysql.connector.connect(**test_db_conn)
    cursor = cnx.cursor(buffered=True)

    # simulate the server terminating the
    # database connection
    cursor.execute('kill {}'.format(db.database_connection.connection_id))
    cnx.commit()

    yield db

    db.query('drop table pet')
    cursor.close()  # close the cursor
    cnx.close()  # close the database connection








