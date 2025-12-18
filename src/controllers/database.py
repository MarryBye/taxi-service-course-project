import psycopg2 as sql
import psycopg2.extras as sql_ext
import psycopg2.errors as sql_err

from config import ( DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME )
from src.schemas.token import TokenDataSchema

class Database:
    def __init__(self, user: TokenDataSchema | None = None):
        self.__user = user
        self.__connection: None | sql.extensions.connection = None
        self.__cursor: None | sql.extensions.cursor = None
        
    def connect(self):
        print(f"[DATABASE]: Connecting to database {DB_NAME} ({DB_USER}:{DB_PASSWORD})")
        self.__connection = sql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database=DB_NAME)
        self.__cursor = self.__connection.cursor(cursor_factory=sql_ext.RealDictCursor)

        sql_ext.register_composite(
            'public.address',
            self.__connection,
            globally=True
        )

    def disconnect(self):
        self.__cursor.close()
        self.__connection.close()

    def execute(self, query: str, params=None, fetch_count: int = 1) -> Exception | dict:
        params = params if params else []
        result = None

        self.connect()

        try:
            self.__cursor.execute("SET ROLE %s", [self.__user.role if self.__user else 'guest'])
            self.__cursor.execute(query, params)
            match fetch_count:
                case 1: result = self.__cursor.fetchone()
                case 0: result = None
                case -1: result = self.__cursor.fetchall()
                case _: result = self.__cursor.fetchmany(fetch_count)
        except Exception as e:
            print(f"[DATABASE]: {e}")
            result = e
            self.__connection.rollback()
        finally:
            self.__cursor.execute("RESET ROLE")
            self.__connection.commit()
            self.disconnect()
        return result