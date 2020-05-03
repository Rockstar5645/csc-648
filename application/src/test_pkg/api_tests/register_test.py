from src.database_manager.db_manager import DB

db = DB()

status = db.register('rockstar24', 'akhilhello@gmail.com', 'some_pass')

if status['status'] == 'success':
    print('User registration was successful, and redis, database connection is healthy')
    print('session token {}'.format(status['token']))
elif status['status'] == 'database_error':
    print('Something went wrong at the database layer: {}'.format(status['message']))
elif status['status'] == 'redis_error':
    print('something went wrong with the redis instance: {}'.format(status['message']))
