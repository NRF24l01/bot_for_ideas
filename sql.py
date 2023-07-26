import psycopg2

class SQL_connector:
    def __init__(self, host: str, username: str, userpass:str, db_name: str, port: int = 5432):
        self.conn = psycopg2.connect(dbname=db_name, user=username, password=userpass, host=host, port=port)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()  # закрываем курсор
        self.conn.close()  # закрываем соединение

    def select(self):
        self.cursor