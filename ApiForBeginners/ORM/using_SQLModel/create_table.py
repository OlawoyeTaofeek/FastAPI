from database import engine
from sqlmodel import SQLModel
from models import User, Role


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
