from father.database_manager import cnx



class DB:

    def __init__(self):
        self.db_connection = cnx.MyDB()

    def search_like(self, category, term):
        self.db_connection.query("SELECT * FROM digital_media_test")
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        return data