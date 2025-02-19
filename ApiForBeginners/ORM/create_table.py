# create_tables.py
from database import engine, Base
from sql_alchemy_orm import User, Role

# Create tables in the database
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
