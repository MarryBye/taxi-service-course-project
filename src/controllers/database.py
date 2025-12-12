import psycopg2 as sql
import psycopg2.extras as sql_ext

from os import path, walk
from typing import Literal
from config import ( DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME )
from src.enums.roles import UserRole
from src.schemas.auth import AuthUserSchema

class Database:
    def __init__(self):
        self.__connection: None | sql.extensions.connection = None
        self.__cursor: None | sql.extensions.cursor = None
        
    def connect(self, executor_data: AuthUserSchema = None):
        user = DB_USER if not executor_data else executor_data.login
        password = DB_PASSWORD if not executor_data else executor_data.password
        print(f"[DATABASE]: Connecting to database {DB_NAME} ({user}:{password})")
        self.__connection = sql.connect(user=user, password=password, host=DB_HOST, port=DB_PORT, database=DB_NAME)
        self.__cursor = self.__connection.cursor(cursor_factory=sql_ext.RealDictCursor)

    def disconnect(self):
        self.__cursor.close()
        self.__connection.close()

    def execute(self, query: str, params=None, fetch_count: int = 1, executor_data: AuthUserSchema = None):
        params = params if params else []
        result = None

        self.connect(executor_data=executor_data)

        print(f'[DATABASE]: Executing query: {query}')

        try:
            self.__cursor.execute(query, params)

            match fetch_count:
                case 1: result = self.__cursor.fetchone()
                case 0: result = None
                case -1: result = self.__cursor.fetchall()
                case _: result = self.__cursor.fetchmany(fetch_count)

            self.__connection.commit()

            print(f'[DATABASE]: Query executed successfully')

        except Exception as e:
            print(f'[DATABASE]: Error: {e}')
            self.__connection.rollback()
            return e
        finally:
            self.disconnect()
            return result

database = Database()