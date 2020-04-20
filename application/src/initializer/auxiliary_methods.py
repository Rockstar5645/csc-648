
def fill_team_about(db):
    ###############################
    #     FILL TEAM ABOUT TABLE   #
    ###############################

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



def fill_categories(db):
    ############################
    #      FILL CATEGORIES     #
    ############################

    add_category_query = ("INSERT INTO categories "
                          "(category)"
                          "VALUES (%s)")

    categories_entries = [
        ('all',),
        ('image',),
        ('video',),
        ('audio',),
        ('document',)
    ]

    for category_entry in categories_entries:
        db.query(add_category_query, category_entry)
        db.commit()