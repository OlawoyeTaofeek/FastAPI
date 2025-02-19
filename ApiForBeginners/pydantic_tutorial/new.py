from typing import Optional
from pydantic import BaseModel

# Use Optional[T] when a field can be None
# Optional[T] means the field can either be T (a valid type) or None
# It’s just shorthand for Union[T, None]
class User(BaseModel):
    username: str
    age: Optional[int]  # This means age can be int OR None

user1 = User(username="Alice", age=25)  
user2 = User(username="Bob")  

print(user1)  # User(username='Alice', age=25)
print(user2)  # User(username='Bob', age=None)


# Use Union[T1, T2] when a field can have multiple types
from typing import Union
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: Union[int, float]  # Can be int OR float
    discount: Union[int, None]  # Can be int OR None (same as Optional[int])

product1 = Product(name="Laptop", price=999, discount=10)  # ✅ Works
product2 = Product(name="Phone", price=699.99, discount=None)  # ✅ Works
product3 = Product(name="Tablet", price="Free")  # ❌ Error (Only int or float allowed)

print(product1)  # Product(name='Laptop', price=999, discount=10)
print(product2)  # Product(name='Phone', price=699.99, discount=None)
