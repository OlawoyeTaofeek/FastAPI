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