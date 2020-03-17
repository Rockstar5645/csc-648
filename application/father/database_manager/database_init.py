from father.database_manager import cnx

db = cnx.MyDB()

# if a table already exits in your database just comment it out!!!

db.query("CREATE TABLE user ("
         "user_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
         "first_name VARCHAR(30),"
         "last_name VARCHAR(30),"
         "email VARCHAR(20),"
         "phone_number VARCHAR(10),"
         "PRIMARY KEY (user_id))") 

db.query("CREATE TABLE digital_media ("
         "media_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
         "owner_id BIGINT UNSIGNED NOT NULL,"
         "name VARCHAR(50),"
         "description VARCHAR(150),"
         "file_path VARCHAR(200),"
         "thumbnail VARCHAR(200),"
        "time_stamp DATE,"
        "category VARCHAR(20),"
        "price FLOAT(2),"
        "PRIMARY KEY (media_id),"
        "FOREIGN KEY (owner_id) REFERENCES user (user_id))")