# 🚀 FastAPI Comprehensive Guide  

This repository contains a **detailed tutorial** on **FastAPI**, covering everything from **basic API development** to **advanced topics like Docker, deployment, and Python best practices**.  

---

## 📖 Table of Contents  
- [🌟 Introduction](#-introduction)  
- [⚙️ Setting Up FastAPI](#️-setting-up-fastapi)  
- [🖥️ Building APIs with FastAPI](#%EF%B8%8F-building-apis-with-fastapi)  
- [📦 Containerization with Docker](#-containerization-with-docker)  
- [🚀 Deploying FastAPI](#-deploying-fastapi)  
  - [Heroku Deployment](#heroku-deployment)  
  - [AWS Deployment](#aws-deployment)  
- [🐍 Python Fundamentals for FastAPI](#-python-fundamentals-for-fastapi)  
  - [OOP in Python](#oop-in-python)  
  - [Pydantic for Data Validation](#pydantic-for-data-validation)  
- [📜 Additional Resources](#-additional-resources)  
- [📌 Author](#-author)  

---

## 🌟 Introduction  
FastAPI is a **modern, high-performance web framework** for building APIs with Python 3.7+ based on standard **Python type hints**.  

### ✅ Why FastAPI?  
✔️ **Blazing fast** (async support using Starlette)  
✔️ **Automatic validation** with Pydantic  
✔️ **Auto-generated Swagger & OpenAPI docs**  
✔️ **Easy-to-use Dependency Injection**  
✔️ **Built-in OAuth2 & authentication support**  

---

## ⚙️ Setting Up FastAPI  

### 🔹 Install FastAPI and Uvicorn  
```bash
pip install fastapi uvicorn
```
---
## 🛠️ Create a Virtual Environment  
To set up a virtual environment for your FastAPI project, run the following commands:  

```bash
python -m venv api_env
source api_env/bin/activate  # For Mac/Linux
api_env\Scripts\activate     # For Windows
```
---

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```
---

## 🖥️ Building APIs with FastAPI

### 🔹 Create a Simple API
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

---
### 🔹 Run the API
```bash
uvicorn main:app --reload
```
---

## 📦 Containerization with Docker
### 🔹 Create a Dockerfile
```bash
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
### 🔹 Build and Run the Docker Container
```bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```


---

## 🐍 Python Fundamentals for FastAPI

### 🔤 Type Casting and Typing in Python  

Python allows for **explicit** and **implicit** type conversion.  

### 🔹 Implicit Type Casting  
Python automatically converts smaller data types to larger ones.  
```python
num_int = 5  
num_float = 2.5  
result = num_int + num_float  # int is implicitly converted to float  
print(result)  # Output: 7.5
print(type(result))  # Output: <class 'float'>
```
## 🔠 Python Typing (Type Hints)
### 📌 Basic Type Hints
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Taofeek"))  # Output: Hello, Taofeek
```

### 📌 Typing with Lists, Tuples, and Dicts
```python
from typing import List, Tuple, Dict  

def process_numbers(numbers: List[int]) -> Tuple[int, int]:  
    return min(numbers), max(numbers)

print(process_numbers([3, 1, 4, 1, 5]))  # Output: (1, 5)
```
### 📌 Typing with Optional and Union
```python
from typing import Optional, Union  

def get_value(flag: bool) -> Optional[Union[int, str]]:  
    return 42 if flag else None  

print(get_value(True))  # Output: 42
print(get_value(False))  # Output: None
```

### 🔹 OOP in Python
```python
class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def display(self):
        return f"{self.title}: {self.content}"
```

## 🔹 Pydantic for Data Validation
```python
from pydantic import BaseModel

class PostSchema(BaseModel):
    title: str
    content: str
```

--- 
## 📜 Additional Resources  

- [FastAPI Documentation](https://fastapi.tiangolo.com/)  
- [Docker Documentation](https://docs.docker.com/)  
- [AWS ECR Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)  

---

## 📌 Author  

👤 **Taofeek Olawoye**  
📧 Email: [OlawoyeTaofeek](oladipupoolawoye26@gmail.com)  
<!-- 🐦 Twitter: [@yourhandle](https://twitter.com/yourhandle)   -->
📂 GitHub: [OlawoyeTaofeek](https://github.com/OlawoyeTaofeek)

📂 LinkedIn: [OlawoyeTaofeek](https://www.linkedin.com/in/opeyemi-oladipupo-a7862021a/)  

---
🔥 Enjoy learning FastAPI? Give this repo a ⭐ and share with others! 🚀  

