from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
from typing import List
import yaml
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Load configuration from YAML file
with open(r"C:\Users\user\Desktop\ApiDevelopment\ApiTutorial\ApiForBeginners\ORM\config.yaml", "r") as file:
    config = yaml.safe_load(file)

db_config = config["database"]

# Function to establish a database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=db_config["host"],
            database=db_config["name"],
            user=db_config["user"],
            password=db_config["password"],
            port=db_config["port"]
        )
        print("Connected to the PostgreSQL database")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

# Define Pydantic model for response
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# Route to fetch all posts
@app.get("/posts") 
def get_posts():
    conn = get_db_connection()
    if conn is None:
        return {"message": "Database connection failed."}

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM public."Posts";')  
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return {'message': 'Posts fetched successfully', 'posts': rows}

# Route to create a new post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    conn = get_db_connection()
    if conn is None:
        return {"message": "Database connection failed."}

    cursor = conn.cursor()
    query = '''
        INSERT INTO "Posts" (title, content, published) 
        VALUES (%s, %s, %s) RETURNING *;
    '''
    cursor.execute(query, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()
    
    return {'data': new_post}

# Route to get a single post by ID
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    conn = get_db_connection()
    if conn is None:
        return {"message": "Database connection failed."}

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = 'SELECT * FROM "Posts" WHERE id = %s;'
    cursor.execute(query, (post_id,))
    post = cursor.fetchone()

    cursor.close()
    conn.close()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    return {'data': post}

# Route to delete a post by ID
@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail="Database connection failed.")

    cursor = conn.cursor()
    query = 'DELETE FROM "Posts" WHERE id = %s RETURNING *;'
    cursor.execute(query, (post_id,))
    deleted_post = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id {post_id} not found")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Route to update a post by ID
@app.put("/posts/{post_id}", status_code=status.HTTP_201_CREATED)
def update_post(post_id: int, post: Post):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail="Database connection failed.")

    cursor = conn.cursor()
    query = '''
        UPDATE "Posts" SET title=%s, content=%s, published=%s 
        WHERE id = %s RETURNING *;
    '''
    cursor.execute(query, (post.title, post.content, post.published, post_id))
    updated_post = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id {post_id} not found")
    
    return {'data': updated_post}
