import psycopg2 as sql
import psycopg2.extras as sql_ext
import psycopg2.errors as sql_err

guest_data = ('guest_account', 'guest_account')



db = DatabaseController()
db.connect()
r = db.execute("SELECT * FROM public.authenticate(%s, %s)", ['MarryBye', 'Ukraine555U'])
print(r)
if isinstance(r, Exception):
    print("Incorrect credentials")
else:
    db.connect('MarryBye', 'Ukraine555U')
    jwt_login = 'MarryBye'
    db.execute("SELECT * FROM public.authenticate(%s, %s)", ['MarryBye', 'Ukraine555U'], fetch_count=1, executor=jwt_login)