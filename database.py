import sqlite3
from datetime import datetime

class Database():
    def __get_connection(self):
        connection = sqlite3.connect("database.db")
        return connection

    def __init__(self) -> None:
        connection = self.__get_connection()
        cursor = connection.cursor()

        # If table is not created
        table = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='finances';")
        table = table.fetchone()

        if not table:
            self.__create_table()

        connection.close()

    def get_records(self) -> list[tuple]:
        connection = self.__get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT amount, description, category, date FROM finances;")
        results = cursor.fetchall()
        connection.close()
        return results

    def __add_record(self, amount: float, description: str, category: str, date: datetime) -> None:
        connection = self.__get_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO finances(amount, description, category, date) VALUES (?, ?, ?, ?);", (amount, description, category, date))
        connection.commit()
        connection.close()

    def __delete_record(self, id: int) -> None:
        connection = self.__get_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM finances WHERE id=?;", (id,))
        connection.commit()
        connection.close()

    def __create_table(self) -> None:
        connection = self.__get_connection()
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE finances(id integer primary key, amount real, description varchar(255), category varchar(255), date datetime);")
        connection.close()
    def __delete_table(self) -> None:
        connection = self.__get_connection()
        cursor = connection.cursor()

        cursor.execute("DROP TABLE finances;")
        connection.close()