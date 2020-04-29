

def initialize_database_skeleton(db):
    ###############################
    #      DROP ALL TABLES        #
    ###############################
    print('Dropping any residual tables')

    db.query("DROP TABLE IF EXISTS messages")
    db.commit()

    db.query("DROP TABLE IF EXISTS digital_media")
    db.commit()

    db.query("DROP TABLE IF EXISTS categories")
    db.commit()

    db.query("DROP TABLE IF EXISTS media_types")
    db.commit()

    db.query("DROP TABLE IF EXISTS team_about")
    db.commit()

    db.query("DROP TABLE IF EXISTS user")
    db.commit()

    print('Residual Tables dropped')


    ############################
    #         USER TABLE       #
    ############################
    print('Creating User Table')

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
    print('User Table created')

    """Creating an Index on the username to make login faster"""



    ###############################
    #      CATEGORIES TABLE       #
    ###############################
    print('Creating categories table')
    db.query("CREATE TABLE categories ("
             "category_id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
             "category VARCHAR(50),"
             "PRIMARY KEY (category_id))")
    db.commit()
    print('Categories table created')


    ###############################
    #      MEDIA TYPE TABLE       #
    ###############################
    print('Creating media types table')
    db.query("CREATE TABLE media_types ("
             "media_type_id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
             "media_type VARCHAR(50),"
             "PRIMARY KEY (media_type_id))")
    db.commit()
    print('Created media types table')


    ###############################
    #      DIGITAL MEDIA TABLE    #
    ###############################
    """ 
    https://stackoverflow.com/a/30532735/4944292
    SHOW ENGINE INNODB STATUS
    Go to "Latest Foreign Key Error" section 
    """


    print('Creating digital media table')
    db.query("CREATE TABLE digital_media ("
             "media_id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
             "owner_id INT UNSIGNED NOT NULL,"
             "name VARCHAR(50),"
             "description VARCHAR(150),"
             "file_path VARCHAR(200),"
             "thumbnail_path VARCHAR(200),"
             "category_id INT UNSIGNED NOT NULL,"
             "media_type_id INT UNSIGNED NOT NULL,"
             "price FLOAT(2),"
             "approval INT,"
             "PRIMARY KEY (media_id),"
             "FOREIGN KEY (owner_id) REFERENCES user (user_id),"
             "FOREIGN KEY (category_id) REFERENCES categories (category_id),"
             "FOREIGN KEY (media_type_id) REFERENCES media_types (media_type_id),"
             "INDEX (description, category_id, media_type_id))")
    db.commit()
    print('Digital media table created')


    ###############################
    #         MESSAGES TABLE      #
    ###############################
    print('Creating Messages Table')
    db.query("CREATE TABLE messages ("
             "message_id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
             "time_stamp DATETIME NOT NULL,"
             "sender INT UNSIGNED NOT NULL,"
             "recipient INT UNSIGNED NOT NULL,"
             "message_content TEXT NOT NULL,"   # 64KB Limit
             "media_id INT UNSIGNED NOT NULL,"
             "seen BOOLEAN,"
             "subject TINYTEXT NOT NULL,"        # 255 Byte Limit
             "PRIMARY KEY (message_id),"
             "FOREIGN KEY (sender) REFERENCES user (user_id),"
             "FOREIGN KEY (recipient) REFERENCES user (user_id),"
             "FOREIGN KEY (media_id) REFERENCES digital_media (media_id),"
             "INDEX (time_stamp, sender, recipient, seen))")
    db.commit()
    print('Messages table created')


    ###############################
    #      TEAM ABOUT TABLE       #
    ###############################
    print('Creating team members profiles table')
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
    print('Created team members profiles table')