from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import yaml

with open(r"C:\Users\user\Desktop\ApiDevelopment\ApiTutorial\ApiForBeginners\ORM\config.yaml", "r") as file:
    config = yaml.safe_load(file)

db_config = config["database"]

SQLALCHEMY_DATABASE_URI = (f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}")

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()