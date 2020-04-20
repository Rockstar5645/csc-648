import mysql.connector
import pytest


def test_query_connection_collapse(init_query_create_table):
    db = init_query_create_table

    # the application should automatically reconnect to the database server
    db.query('CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE)')
    db.commit()
    db.query('DESCRIBE pet')
    db.commit()
    rows = db.fetchall()

    assert rows[0][0] == 'name'
    assert rows[0][1] == 'varchar(20)'
    assert rows[0][2] == 'YES'
    assert rows[4][0] == 'birth'
    assert rows[4][1] == 'date'
    assert rows[4][2] == 'YES'


def test_query_create_table(init_query_create_table):
    db = init_query_create_table

    db.query('CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE)')
    db.commit()
    db.query('DESCRIBE pet')
    db.commit()
    rows = db.fetchall()

    assert rows[0][0] == 'name'
    assert rows[0][1] == 'varchar(20)'
    assert rows[0][2] == 'YES'
    assert rows[4][0] == 'birth'
    assert rows[4][1] == 'date'
    assert rows[4][2] == 'YES'


def test_connection_loss(init_raw_database_connection_collapse):
    """The server has terminated the connection from the client (simulation)"""
    cursor = init_raw_database_connection_collapse

    with pytest.raises(mysql.connector.errors.OperationalError) as exception_info:
        cursor.execute('use test')

    err = exception_info.value
    print("\n\n" + str(err))

    assert "2013 (HY000): Lost connection to MySQL server during query" in err._full_msg
    assert err.errno == 2013
    assert "HY000" in err.sqlstate
    assert "Lost connection to MySQL server during query" in err.msg
