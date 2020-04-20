import pytest
import mysql.connector
from src.database_manager import database_connection
from src.config import db_conn

@pytest.fixture()
def db_connection_params():
    return dict(db_conn)


def test_wrong_username(db_connection_params):
    """Pass the wrong Username to the database connection object"""
    db_connection_params['user'] = 'wrong_username'
    with pytest.raises(mysql.connector.Error) as exception_info:
        db = database_connection.MyDB(datbase_connection_paramaters=db_connection_params)

    err = exception_info.value
    print("\n\n" + str(err))

    assert "1045 (28000): Access denied for user 'wrong_username'@'localhost' (using password: YES)" in err._full_msg
    assert err.errno == 1045
    assert "28000" in err.sqlstate
    assert "Access denied for user 'wrong_username'@'localhost' (using password: YES)" in err.msg


def test_wrong_password(db_connection_params):
    """Pass the wrong password to the database connection object"""
    db_connection_params['password'] = 'wrong_password'
    with pytest.raises(mysql.connector.Error) as exception_info:
        db = database_connection.MyDB(datbase_connection_paramaters=db_connection_params)

    err = exception_info.value
    print("\n\n" + err._full_msg)

    assert "1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)" in err._full_msg
    assert err.errno == 1045
    assert "28000" in err.sqlstate
    assert "Access denied for user 'root'@'localhost' (using password: YES)" in err.msg

def test_wrong_host(db_connection_params):
    """Pass the wrong host to the database connection object"""
    db_connection_params['host'] = 'wrong_host'
    with pytest.raises(mysql.connector.Error) as exception_info:
        db = database_connection.MyDB(datbase_connection_paramaters=db_connection_params)

    err = exception_info.value
    print("\n\n" + err._full_msg)

    assert "2005 (HY000): Unknown MySQL server host 'wrong_host' (0)" in err._full_msg
    assert err.errno == 2005
    assert "HY000" in err.sqlstate
    assert "Unknown MySQL server host 'wrong_host' (0)" in err.msg

def test_wrong_port(db_connection_params):
    """Pass the wrong port number to the database connection object"""
    db_connection_params['port'] = 1234
    with pytest.raises(mysql.connector.Error) as exception_info:
        db = database_connection.MyDB(datbase_connection_paramaters=db_connection_params)

    err = exception_info.value
    print("\n\n" + err._full_msg)

    assert "2003 (HY000): Can't connect to MySQL server on 'localhost' (10061)" in err._full_msg
    assert err.errno == 2003
    assert "HY000" in err.sqlstate
    assert "Can't connect to MySQL server on 'localhost' (10061)" in err.msg

    """Pass a alphabetic character string as port to the database connection object"""
    db_connection_params['port'] = 'abcd'
    with pytest.raises(mysql.connector.Error) as exception_info:
        db = database_connection.MyDB(datbase_connection_paramaters=db_connection_params)

    err = exception_info.value
    print("\n\n" + err._full_msg)

    assert "TCP/IP port number should be an integer" in err._full_msg
    assert err.errno == -1
    assert err.sqlstate is None
    assert "TCP/IP port number should be an integer" in err.msg


def test_wrong_database(db_connection_params):
    """Pass the wrong database identifier to the database connection object"""
    db_connection_params['database'] = 'wrong_database'
    with pytest.raises(mysql.connector.Error) as exception_info:
        db = database_connection.MyDB(datbase_connection_paramaters=db_connection_params)

    err = exception_info.value
    print("\n\n" + err._full_msg)

    assert "1049 (42000): Unknown database 'wrong_database'" in err._full_msg
    assert err.errno == 1049
    assert "42000" in err.sqlstate
    assert "Unknown database 'wrong_database'" in err.msg