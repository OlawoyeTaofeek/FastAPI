from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base, engine
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True) # Unique identifier for each user
    name = Column(String, index=True) # User's full name
    username = Column(String, unique=True, index=True) # User's unique username
    email = Column(String, unique=True, index=True) # User's unique email address
    password_hash = Column(String) # Hashed version of the user's password
    role_id = Column(Integer, ForeignKey('roles.id')) # Foreign key to the 'roles' table, referencing the role ID
    role = relationship('Role', back_populates='users', cascade="all, delete-orphan") # Relationship with the 'roles' table, allowing one-to-many relationship between 'users' and 'roles'
    """cascade="all, delete-orphan": This defines how changes 
    to the User affect related Address records. Specifically, 
    when a User is deleted, all their associated Address records 
    will also be deleted (all), and if an Address is no longer 
    associated with a User, it will be orphaned and deleted (delete-orphan).
    """
    
class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True) # Unique identifier for each role
    name = Column(String, unique=True, index=True) # Role's name
    description = Column(String) # Description of the role
    users = relationship('User', back_populates='role') # Relationship with the 'users' table, allowing one-to-many relationship between 'roles' and 'users'
    

# Explanation:
   ## ForeignKey('roles.id') establishes a foreign key link between User.role_id and Role.id.
   ## relationship('Role', back_populates='users') establishes the ORM relationship.
   ## back_populates='role' ensures bidirectional access between User and Role
   
   
## SQLAlchemy 2.0
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    # Primary key with mapping type hint
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)  # Unique identifier for each user

    # User's full name with mapping type hint
    name: Mapped[str] = mapped_column(String, index=True)  # User's full name

    # User's unique username with mapping type hint
    username: Mapped[str] = mapped_column(String, unique=True, index=True)  # User's unique username

    # User's unique email address with mapping type hint
    email: Mapped[str] = mapped_column(String, unique=True, index=True)  # User's unique email address

    # Hashed version of the user's password with mapping type hint
    password_hash: Mapped[str] = mapped_column(String)  # Hashed version of the user's password

    # Foreign key to the 'roles' table, referencing the role ID with mapping type hint
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('roles.id'))  # Foreign key to the 'roles' table, referencing the role ID

    # Relationship to the Role model with mapping type hint
    role: Mapped["Role"] = relationship('Role', back_populates='users', cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, username={self.username!r}, email={self.email!r})"
