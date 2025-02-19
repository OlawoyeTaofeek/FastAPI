from sqlmodel import create_engine
from contextlib import contextmanager
from sqlmodel import Session
import yaml

with open(r"C:\Users\user\Desktop\ApiDevelopment\ApiTutorial\ApiForBeginners\ORM\config.yaml", "r") as file:
    config = yaml.safe_load(file)

db_config = config["database"]
DATABASE_URL = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"

engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session
        

# @contextmanager
# def get_session():
#     with Session(engine) as session:
#         yield session
        
# @contextmanager: Turns a function into a context manager, allowing you to use it with with statements.