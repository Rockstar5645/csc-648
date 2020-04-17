from src.database_manager.db_manager import DB

db = DB()

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