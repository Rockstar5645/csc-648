from father.database_manager import cnx



class DB:

    def __init__(self):
        self.db_connection = cnx.MyDB()

    def search(self, term, category):
        if term =='':
            return self.get_category(category)
        else:
            return self.search_like(term, category)

    def search_like(self, term, category):
        # query db using %like for owner_name, name, description, category, and price
        # this works for values that contain the search term
        self.db_connection.query(
            "SELECT media_id, owner_name, name, description, file_path, thumbnail, category, price "
            "FROM digital_media_test "
            "WHERE owner_name LIKE %s OR name LIKE %s OR description LIKE %s OR category LIKE %s OR price LIKE %s",
            ("%" + term + "%","%" + term + "%","%" + term + "%","%" + term + "%", "%" + term + "%",))
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        # query all items in database if user enters 'all' in search box
        if len(data) == 0 and term == 'all' and category == 'all':
            self.db_connection.query("Select * FROM digital_media_test")
            data = self.db_connection.fetchall()
            self.db_connection.commit()
        # fetch from cursor and commit
        # ret
        return data

    ''' Just messing around with SQL search options
    def search_like(self, term, category):
        self.db_connection.query(
            "SELECT * "
            "FROM digital_media_test "
            "WHERE (name LIKE %s OR description LIKE %s) AND category LIKE %s",
            ("%" + term + "%","%" + term + "%", "%" + category,)
        )
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        print("\nlength: ")
        print(len(data))
        print("\n")
        if len(data) == 0:
            data = self.get_category(category)
        return data
    ''' 

    def get_category(self, category):
        self.db_connection.query("Select * FROM digital_media_test WHERE category LIKE %s", ("%" + category + "%",))
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        if len(data) == 0:
            data = self.get_all_media()
        return data
    
    def get_all_media(self):
        self.db_connection.query("Select * FROM digital_media_test")
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        return data
