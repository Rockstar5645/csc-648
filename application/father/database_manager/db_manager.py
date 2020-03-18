from father.database_manager import cnx



class DB:

    def __init__(self):
        self.db_connection = cnx.MyDB()

    def search_like(self, category, term):
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