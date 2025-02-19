from sqlmodel import create_engine
from contextlib import contextmanager
from sqlmodel import Session

DATABASE_URL = "postgresql+psycopg2://postgres:oladipupo@localhost:5432/FastAPI"

engine = create_engine(DATABASE_URL)

@contextmanager
def get_session():
    with Session(engine) as session:
        yield session
        
# @contextmanager: Turns a function into a context manager, allowing you to use it with with statements.