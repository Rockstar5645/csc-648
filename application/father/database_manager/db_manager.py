from father.database_manager import cnx



class DB:

    def __init__(self):
        self.db_connection = cnx.MyDB()

    def search(self, term, category):
        print("term: " + term)
        print("cat: " + category)
        if term =='':
            return self.get_category(category)
        else:
            return self.search_like(term, category)

    def search_like(self, term, category):
        if category == 'all':
            self.db_connection.query(
                "SELECT * "
                "FROM digital_media_test "
                "WHERE `name` LIKE %s OR `description` LIKE %s",
                ("%" + term + "%","%" + term + "%",)
            )
        else:
            self.db_connection.query(
                "SELECT * "
                "FROM digital_media_test "
                "WHERE (`name` LIKE %s OR `description` LIKE %s) AND category LIKE %s",
                ("%" + term + "%","%" + term + "%", "%" + category,)
            )
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        if len(data) == 0:
            data = self.get_category(category)
        return data

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

    def get_category_select_field(self):
        self.db_connection.query("Select * FROM categories")
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        cats = [(c[1], c[1]) for c in data]
        return cats

    def get_team(self, name):
        self.db_connection.query("Select * FROM team_about WHERE `name` %s", ("%"+name+"%",))
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        return data