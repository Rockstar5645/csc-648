
def fill_team_about(db):
    ###############################
    #     FILL TEAM ABOUT TABLE   #
    ###############################
    print('Inserting data into team member profiles table')

    add_about_team_query = ("INSERT INTO team_about "
                            "(name, link, position, image, description, facebook, twitter, instagram, linkedin) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

    team_about_entries = [
        ('Avery Chen', '/avery', 'Back-end Member', 'static/team_images/avery.jpg', 'Undergraduate student at SFSU',
        '', '', '', ''),
        ('Akhil Gandu', '/akhil', 'GitHub Master', 'static/team_images/akhil.jpg', 'Graduate Student at SFSU',
         'https://www.facebook.com/rockstar290', 'https://twitter.com/Rockstar5645',
         'https://www.instagram.com/akhil_gandu/', 'https://www.linkedin.com/in/akhilgandu/'),
        ('Chris Eckhardt', '/chris', 'Back-end lead', 'static/team_images/chris.jpg', 'Undergrad at SFState', '', '',
         'https://www.instagram.com/chris_evan_eckhardt/', 'https://www.linkedin.com/in/christopher-eckhardt-04abb1119/'),
        ('Elliot Yardley', '/elliot', 'Front-end lead', 'static/team_images/elliot.jpg', 'Graduate Student, SFSU',
         '', '', '', ''),
        ('Thomas Yu', '/thomas', 'Front End Member', 'static/team_images/Thomas.jpg', 'Undergraduate Student, SFSU',
         '', '', '', ''),
        ('Bakulia Kurmant', '/bakulia', 'Team Lead', 'static/team_images/bakulia.jpg', 'In my spare time I like going outdoors, techno music, reading, traveling', '', '', 'https://www.instagram.com/bakuliak/?hl=en', 'https://www.linkedin.com/in/bakulia-kurmant/')
    ]

    for team_about_entry in team_about_entries:
        db.query(add_about_team_query, team_about_entry)
        db.commit()
    print('Inserted data into team member profiles table')



def fill_media_types(db):
    ############################
    #      FILL MEDIA TYPES    #
    ############################
    print('Initializing media types table with an enumeration of available media types')

    add_media_type_query = ("INSERT INTO media_types "
                          "(media_type)"
                          "VALUES (%s)")

    media_types_entries = [
        ('all',),
        ('image',),
        ('video',),
        ('audio',),
        ('document',)
    ]

    for media_type_entry in media_types_entries:
        db.query(add_media_type_query, media_type_entry)
        db.commit()
    print('Media types table initialized')


def fill_digital_media(db):
    ############################
    #      FILL CATEGORIES     #
    ############################

    print('Inserting data test entries into digital media table')

    add_digital_media_query = ("INSERT INTO digital_media  "
                               "(owner_id, name, description, file_path, thumbnail_path, category_id, media_type_id, price, approval) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

    digital_media_entries = [
        ('1', 'sponge bob 1', 'this is the first test photo', '/M2_test_images/sb1.jpg', '/thumbnails/sb1_t.jpg',
            1, 2, 99.99, 0),
        ('2', 'sponge bob 2', 'this is the second test photo', '/M2_test_images/sb2.jpg','/thumbnails/sb2_t.jpg' ,\
            1, 3 , 89.99, 0),
        ('3', 'sponge bob 3', 'this is the third test photo', '/M2_test_images/sb3.jpg','/thumbnails/sb3_t.jpg' ,
            1, 5 , 79.99, 0),
        ('4', 'sponge bob 4', 'this is the fourth test photo', '/M2_test_images/sb4.jpg','/thumbnails/sb4_t.jpg' ,
            1, 4 , 69.99, 0),
        ('5', 'sponge bob 5', 'this is the fifth test photo', '/M2_test_images/sb5.jpg','/thumbnails/sb5_t.jpg' ,
            1, 2 , 59.99, 0)
    ]

    for digital_media_entry in digital_media_entries:
        db.query(add_digital_media_query, digital_media_entry)
        db.commit()

    print('Initialization of digital media entries table complete')