from father.database_manager import cnx

db = cnx.MyDB()

db.query("CREATE TABLE digital_media_test ("
         "media_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
         "owner_name VARCHAR(50),"
         "name VARCHAR(50),"
         "description VARCHAR(150),"
         "file_path VARCHAR(200),"
         "thumbnail VARCHAR(200),"
         "category VARCHAR(20),"
         "price FLOAT(2),"
         "PRIMARY KEY (media_id))")