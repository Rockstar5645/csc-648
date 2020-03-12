from father.database_manager import cnx

db = cnx.MyDB()

db.query("CREATE TABLE user ("
         "user_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
         "first_name VARCHAR(30),"
         "last_name VARCHAR(30),"
         "email VARCHAR(20),"
         "phone_number VARCHAR(10),"
         "PRIMARY KEY (user_id))")