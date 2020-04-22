

def initialize_database_skeleton(db):
    ###############################
    #      DROP ALL TABLES        #
    ###############################

    db.query("DROP TABLE IF EXISTS digital_media")
    db.commit()

    db.query("DROP TABLE IF EXISTS user")
    db.commit()

    db.query("DROP TABLE IF EXISTS categories")
    db.commit()

    db.query("DROP TABLE IF EXISTS team_about")
    db.commit()


    ############################
    #         USER TABLE       #
    ############################

    db.query("CREATE TABLE user ("
             "user_id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
             "first_name VARCHAR(30),"
             "last_name VARCHAR(30),"
             "email VARCHAR(50),"
             "phone_number VARCHAR(10),"
             "username VARCHAR(30) UNIQUE,"
             "password BINARY(60),"
             "PRIMARY KEY (user_id))")
    db.commit()


    ###############################
    #      DIGITAL MEDIA TABLE    #
    ###############################

    db.query("CREATE TABLE digital_media ("
             "media_id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
             "owner_id INT UNSIGNED NOT NULL,"
             "name VARCHAR(50),"
             "description VARCHAR(150),"
             "file_path VARCHAR(200),"
             "thumbnail_path VARCHAR(200),"
             "category VARCHAR(20),"
             "price FLOAT(2),"
             "approval INT,"
             "PRIMARY KEY (media_id),"
             "FOREIGN KEY (owner_id) REFERENCES user (user_id))")
    db.commit()


    ###############################
    #      CATEGORIES TABLE       #
    ###############################

    db.query("CREATE TABLE categories ("
             "cat_id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
             "category VARCHAR(50),"
             "PRIMARY KEY (cat_id))")
    db.commit()


    ###############################
    #      TEAM ABOUT TABLE       #
    ###############################

    db.query("CREATE TABLE team_about ("
                "team_id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
                "name VARCHAR(50),"
                "link VARCHAR(20),"
                "position VARCHAR(50),"
                "image VARCHAR(100),"
                "description VARCHAR(100),"
                "facebook VARCHAR(100),"
                "twitter VARCHAR(100),"
                "instagram VARCHAR(100),"
                "linkedin VARCHAR(100),"
                "PRIMARY KEY (team_id))")
    db.commit()