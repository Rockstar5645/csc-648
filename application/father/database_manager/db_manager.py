from father.database_manager import cnx



class DB:

    def __init__(self):
        self.db_connection = cnx.MyDB()

    def search_like(self, category, term):
        #query db
        self.db_connection.query("SELECT * FROM digital_media_test")
        # fetch from cursor and commit
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        # ret
        return data