# Connecting to database using psycopg2
import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn = psycopg2.connect(
        host='localhost',
        database='FastAPI',
        user='postgres',
        password='oladipupo',
        cursor_factory=RealDictCursor
    )
    cur = conn.cursor()
    print("Connected to the PostgreSQL database")

    cur.execute('SELECT * FROM "Posts";')
    posts = cur.fetchall()
    print(posts)

    cur.close()  # Close cursor after fetching data
    conn.close()  # Close database connection

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
