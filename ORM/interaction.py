from sqlalchemy.orm import Session
from database import SessionLocal
from sql_alchemy_orm import User, Role  


session = SessionLocal()

# Insert a new role
admin_role = Role(name="Admin", description="Administrator role")
session.add(admin_role)
session.commit()

# Insert users assigned to the role
user1 = User(name="Alice", username="alice123", email="alice@email.com", password_hash="hashed_pwd2", role_id=admin_role.id)
user2 = User(name="Bob", username="bob456", email="bob@email.com", password_hash="hashed_pwd2", role_id=admin_role.id)

session.add_all([user1, user2])
session.commit()

print("Users and roles inserted successfully!")

## Example Usage
# Fetch a user and get their role
user = session.query(User).filter(User.username == "alice123").first()
print(f"User: {user.name}, Role: {user.role.name}")

## Add more roles and users as needed
editor_role = Role(name="Editor", description="Can edit content")
viewer_role = Role(name="Viewer", description="Can only view content")

session.add_all([editor_role, viewer_role])
session.commit()

user3 = User(name="Charlie", username="charlie789", email="charlie@email.com", password_hash="hashed_pwd3", role_id=editor_role.id)
user4 = User(name="David", username="david000", email="david@email.com", password_hash="hashed_pwd4", role_id=viewer_role.id)
user5 = User(name="Eve", username="eve999", email="eve@email.com", password_hash="hashed_pwd5", role_id=viewer_role.id)
session.add_all([user3, user4, user5])
session.commit()

print("Roles and users inserted successfully!")