from src.database_manager import cnx
from src.database_manager import register_login
from src.database_manager import redis_cnx

db_connection = cnx.MyDB()
redis_connection = redis_cnx.get_redis_con()

# created_user = register_login.register('rockstar', 'some_pass', 'akhil', 'gandu', '4153755555', 'akhilhello@gmail.com',
#                        db_connection, redis_connection)

register_login.login('rockstar', 'some_pass', '127.0.0.1', db_connection, redis_connection)