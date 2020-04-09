from src.database_manager import cnx
from src.database_manager import register_login
from src.database_manager import redis_cnx

db_connection = cnx.MyDB()
redis_connection = redis_cnx.get_redis_con()

status = register_login.register('rockstar22', 'some_pass', 'akhil', 'gandu', '4153755555', 'akhilhello@gmail.com',
                                 db_connection, redis_connection)

if status['status'] == 'success':
    print('User registration was successful, and redis connection is healthy')
    print('session token {}'.format(status['token']))
elif status['status'] == 'error':
    print('Something went wrong at the datbase layer')
    print(status['message'])

status = register_login.login('rockstar', 'some_pass', '127.0.0.1', db_connection, redis_connection)

if status['status'] == 'success':
    if status['login'] == 'success':
        print('Redis connection is healthy and login was successful')
        print('session token {}'.format(status['token']))
    elif status['login'] == 'failed':
        print("Reids connection is healthy but the login was unsuccessful")
elif status['status'] == 'error':
    print('SOmething went wrong with the database, not redis')
    print(status['message'])