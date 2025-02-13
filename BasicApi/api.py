from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import Optional, Union

app = FastAPI()

# Define supported operations using Enum
class Operation(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"

# Request Body Schema
class CalculationRequest(BaseModel):
    operation: Operation
    number1: int
    number2: int

# Response Schema
class CalculationResponse(BaseModel):
    operation: Operation
    number1: int
    number2: int
    result: Union[int, str]  

@app.post("/calculate", response_model=CalculationResponse)
async def calculate(data: CalculationRequest):
    if data.operation == "add":
        result = data.number1 + data.number2
    elif data.operation == "subtract":
        result = data.number1 - data.number2
    elif data.operation == "multiply":
        result = data.number1 * data.number2
    else:
        return {"operation": data.operation, "number1": data.number1, "number2": data.number2, "result": "Invalid operation"}

    return {
        "operation": data.operation,
        "number1": data.number1,
        "number2": data.number2,
        "result": result
    }


## Using Body
# from fastapi import FastAPI, Body

# app = FastAPI()

# @app.post("/calculate")
# async def calculate(
#     operation: str = Body(..., embed=True),
#     number1: int = Body(..., embed=True),
#     number2: int = Body(..., embed=True) # embed=True makes FastAPI expect a JSON object instead of raw values.
# ):
#     if operation == "add":
#         result = number1 + number2
#     elif operation == "subtract":
#         result = number1 - number2
#     elif operation == "multiply":
#         result = number1 * number2
#     else:
#         return {"error": "Invalid operation"}

#     return {
#         "operation": operation,
#         "number1": number1,
#         "number2": number2,
#         "result": result
#     }


# from fastapi import FastAPI, Body

# app = FastAPI()

# @app.post("/create_post")
# async def create_post(
#     title: str = Body(..., embed=True),
#     content: str = Body(..., embed=True),
#     published: bool = Body(False, embed=True)
# ):
#     return {
#         "message": "Post created successfully",
#         "post": {
#             "title": title,
#             "content": content,
#             "published": published
#         }
#     }
