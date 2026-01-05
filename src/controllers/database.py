import psycopg2 as sql
import psycopg2.extras as sql_ext

from config import ( DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME )

class DatabaseController:
    _instance = None
    connections: dict[str, tuple] = {}

    def __new__(cls):
        print("[DATABASE] Creating new instance")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connections = {}
        print(cls._instance.connections)
        return cls._instance

    def connect(self, username: str = None, password: str = None):
        if username is None or password is None:
            username, password = DB_USER, DB_PASSWORD

        print(f"[DATABASE] Connecting to database as {username}")
        conn = sql.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=username, password=password)
        cursor = conn.cursor(cursor_factory=sql_ext.RealDictCursor)

        self.connections[username] = (conn, cursor)

    def disconnect(self, username: str):
        conn, cursor = self.connections[username]
        cursor.close()
        conn.close()
        del self.connections[username]

    def execute(self, query: str, params: list = None, fetch_count: int = -1, executor_username: str = None) -> Exception | dict:
        result = None

        if executor_username is None:
            executor_username = DB_USER

        if executor_username not in self.connections:
            print(f"[DATABASE] Connecting to database as {DB_USER}")
            executor_username = DB_USER

        if executor_username == DB_USER and executor_username not in self.connections:
            self.connect()

        print(f"[DATABASE] Executing query as {executor_username}")
        conn, cur = self.connections[executor_username]

        try:
            cur.execute(query, params)

            match fetch_count:
                case 1: result = cur.fetchone()
                case 0: result = None
                case -1: result = cur.fetchall()
                case _: result = cur.fetchmany(fetch_count)

            conn.commit()

        except Exception as e:
            result = e
            conn.rollback()
            print(e)

        finally:
            print(result)
            return result