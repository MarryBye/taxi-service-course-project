import psycopg2 as sql
import psycopg2.extras as sql_ext

from os import path, walk
from typing import Literal
from config import ( DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME )

MAP = {}

for root, dirs, files in walk('./src/database/'):
    for file in files:
        if file.endswith('.sql'):
            full_path = path.join(root, file)
            filename_without_ext = path.splitext(file)[0]
            MAP[filename_without_ext] = full_path

class Database:
    def __init__(self):
        self.__connection: None | sql.extensions.connection = None
        self.__cursor: None | sql.extensions.cursor = None
        
    def connect(self):
        self.__connection = sql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database=DB_NAME)
        self.__cursor = self.__connection.cursor(cursor_factory=sql_ext.RealDictCursor)

    def disconnect(self):
        self.__cursor.close()
        self.__connection.close()

    def execute(self, query: str, params=None, fetch_count: int = 1):
        params = params if params else []
        result = None

        self.connect()

        try:
            self.__cursor.execute(query, params)

            match fetch_count:
                case 1: result = self.__cursor.fetchone()
                case 0: result = None
                case -1: result = self.__cursor.fetchall()
                case _: result = self.__cursor.fetchmany(fetch_count)

            self.__connection.commit()

        except Exception as e:
            print(f'[DATABASE]: Error: {e}')
            self.__connection.rollback()
        finally:
            self.disconnect()
            return result

database = Database()