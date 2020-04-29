def fill_categories(db):
    
    print('Inserting entries into catgories table')
    
    category_query = ("INSERT INTO categories (category) VALUES (%s)")

    category_entries = [
        ('all',),
        ('art',),
        ('math',),
        ('biology',),
        ('computer science',)
    ]

    for category_entry in category_entries:
        db.query(category_query, category_entry)
        db.commit()

    print('Initialization of category entries table complete')