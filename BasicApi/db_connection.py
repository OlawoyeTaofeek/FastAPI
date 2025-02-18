import os
import yaml
import psycopg2
from psycopg2.extras import RealDictCursor

# Load configuration from YAML file
with open(r"C:\Users\user\Desktop\ApiDevelopment\ApiDevelopment\ORM\config.yaml", "r") as file:
    config = yaml.safe_load(file)

db_config = config["database"]

# Connecting to PostgreSQL using psycopg2
try:
    conn = psycopg2.connect(
        host=db_config['host'],
        database=db_config['name'],
        user=db_config['user'],
        password=db_config['password'],
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
