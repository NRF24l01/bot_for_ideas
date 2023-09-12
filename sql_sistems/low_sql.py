import sqlite3 as sql


class DataBaseConnector:
    def __init__(self, file_name: str):
        """

        :param dbname: database name
        """
        self.file_name

        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            # пытаемся подключиться к базе данных
            self.conn = sql.connect(self.file_name)
            self.cursor = self.conn.cursor()
        except Exception as er:
            raise er

    def insert(self, table: str, columns: tuple, values: tuple):
        if self.cursor:
            colms = ", ".join(columns)
            vals_q = ", ".join(self._genq(values))
            self.cursor.execute(f"INSERT INTO {table} ({colms}) VALUES({vals_q})", values)
            self.conn.commit()
        else:
            raise ConnectionError

    def select(self, table: str, column: tuple, where: tuple):
        if self.cursor:
            # Build the SQL query
            column = ", ".join(column)
            query = f"SELECT {column} FROM {table}"
            if where:
                query += " WHERE "
                query += " AND ".join([f"{column} = ?" for column, value in where])

            try:
                self.cursor.execute(query, [value for _, value in where])
                result = self.cursor.fetchall()
                return result
            except Exception as e:
                print(f"Failed to execute SELECT query: {e}")
                return None
        else:
            raise ConnectionError

    def _genq(self, values: tuple) -> tuple:
        res = []
        for i in range(len(values)):
            res.append("?")
        return tuple(res)

    def stop(self):
        if self.cursor or self.conn:
            self.cursor.close()  # закрываем курсор
            self.conn.close()  # закрываем соединение

    def __del__(self):
        self.stop()
