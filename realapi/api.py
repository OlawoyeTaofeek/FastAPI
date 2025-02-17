from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
from typing import List
import datetime
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Define Pydantic model for response
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# Function to establish a database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="FastAPI",
            user="postgres",
            password="oladipupo",
            port=5432
        )
        print("Connected to the PostgreSQL database")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

# Route to fetch all posts
@app.get("/posts") 
def get_posts():
    conn = get_db_connection()
    if conn is None:
        return {"message": "Database connection failed."}

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM public."Posts";')  
    rows = cursor.fetchall()

    return {
        'message': 'Posts fetched successfully',
        'posts': rows
    } 
    
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    conn = get_db_connection()
    if conn is None:
        return {"message": "Database connection failed."}
    
    cursor = conn.cursor()
    query = '''
              INSERT INTO "Posts" 
              (title, content, published) 
              VALUES (%s, %s, %s) RETURNING *;
            '''
    values = (post.title, post.content, post.published)
    cursor.execute(query, values)

    # ✅ Fetch the inserted post before closing the cursor
    new_post = cursor.fetchone()

    conn.commit()
    cursor.close()  # Now close the cursor after fetching data
    
    return {
        'data': new_post,
    }
