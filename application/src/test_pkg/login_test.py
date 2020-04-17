from src.database_manager.db_manager import DB

db = DB()

status = db.login('rockstar23', 'some_pass', '127.0.0.1')

if status['status'] == 'success':
    if status['login'] == 'success':
        print('Redis and database connections are healthy and login was successful')
        print('session token {}'.format(status['token']))
    elif status['login'] == 'failed':
        print("Redis and database connections are healthy but the login was unsuccessful, use entered incorrect "
              "password")
elif status['status'] == 'database_error':
    print('Something went wrong at the database layer: {}'.format(status['message']))
elif status['status'] == 'redis_error':
    print('something went wrong with the redis instance: {}'.format(status['message']))