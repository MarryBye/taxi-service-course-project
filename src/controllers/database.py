import psycopg2 as sql
import psycopg2.extras as sql_ext
import psycopg2.errors as sql_err

from config import ( DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, DB_SUPER_USER, DB_SUPER_PASSWORD )
from src.schemas.token import TokenDataSchema
from src.utils.crypto import CryptoUtil

class Database:
    def __init__(self, user: TokenDataSchema | None = None):
        self.__user = user
        self.__connection: None | sql.extensions.connection = None
        self.__cursor: None | sql.extensions.cursor = None
        
    def connect(self, as_admin: bool = False):
        if as_admin:
            user = DB_SUPER_USER
            password = DB_SUPER_PASSWORD
        else:
            user = DB_USER if not self.__user else self.__user.login
            password = DB_PASSWORD if not self.__user else self.__user.password
        print(f"[DATABASE]: Connecting to database {DB_NAME} ({user}:{password})")
        self.__connection = sql.connect(user=user, password=password, host=DB_HOST, port=DB_PORT, database=DB_NAME)
        self.__cursor = self.__connection.cursor(cursor_factory=sql_ext.RealDictCursor)

    def disconnect(self):
        self.__cursor.close()
        self.__connection.close()

    def execute(self, query: str, params=None, fetch_count: int = 1) -> Exception | dict:
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
        except sql_err.ProgrammingError as e:
            print(f"[DATABASE]: {e}")
            result = None
        except Exception as e:
            result = e
            print(f"[DATABASE]: {e}")
            self.__connection.rollback()
        finally:
            self.__connection.commit()
            self.disconnect()
            return result

    def create_superuser(self):
        self.connect(as_admin=True)

        query = "CALL admin.create_user(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = [
            'admin_account',
            'admin@gmail.com',
            '+38-066-073-43-48',
            CryptoUtil.hash_password('1234'),
            'Admin',
            'Adminovich',
            'Ukraine',
            'Odessa',
            'admin'
        ]

        self.__cursor.execute(query, params)
        self.__connection.commit()

        self.disconnect()
