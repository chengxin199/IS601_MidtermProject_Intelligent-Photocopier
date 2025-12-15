---
title: Introduction to fastapi - Exercise Instructions
layout: layouts/course.njk
courseId: Z4-fastapi-intro
permalink: /Lessons/Z4-fastapi-intro/exercise-instructions.html
tags:
  - exercises
  - practice
date: 2025-12-15T23:13:53.547033
---
## Exercise 1: Creating a Simple FastAPI Application
**Difficulty:** Beginner  
**Time Estimate:** 30 minutes

### Objective
Implement a basic FastAPI application that responds to a GET request with a welcome message.

### Starter Code
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # TODO: Return a welcome message
    return {"message": "Welcome to FastAPI!"}
```

### Requirements
- The application should respond to a GET request at the root endpoint ("/").
- The response should be a JSON object with a key "message" and a value "Welcome to FastAPI!".

### Test Cases
```python
# Example test case
# You can use an HTTP client like requests to test your FastAPI app
import requests

response = requests.get("http://127.0.0.1:8000/")
assert response.json() == {"message": "Welcome to FastAPI!"}
```

### Hints
- Make sure to run the FastAPI application using `uvicorn` to test your endpoint.
- Check the console for any errors if the application does not start.

---

## Exercise 2: Creating a Simple Endpoint with Path Parameters
**Difficulty:** Beginner  
**Time Estimate:** 30 minutes

### Objective
Build an endpoint that greets a user by their name using path parameters.

### Starter Code
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
def greet_user(name: str):
    # TODO: Return a greeting message using the name parameter
    return {"message": f"Hello, {name}!"}
```

### Requirements
- Create a GET endpoint `/greet/{name}`.
- The endpoint should return a JSON object with a key "message" and a value "Hello, {name}!", where `{name}` is replaced by the actual name provided in the request.

### Test Cases
```python
# Example test case
response = requests.get("http://127.0.0.1:8000/greet/John")
assert response.json() == {"message": "Hello, John!"}

response = requests.get("http://127.0.0.1:8000/greet/Alice")
assert response.json() == {"message": "Hello, Alice!"}
```

### Hints
- Make sure to test the endpoint with different names.
- The path parameter should be specified in the function definition.

---

## Exercise 3: Creating a POST Endpoint to Handle JSON Data
**Difficulty:** Intermediate  
**Time Estimate:** 40 minutes

### Objective
Create a POST endpoint that accepts a JSON body with user details and returns a confirmation message.

### Starter Code
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/user/")
def create_user(user: User):
    # TODO: Return a confirmation message with user details
    return {"message": f"User {user.name} aged {user.age} created!"}
```

### Requirements
- Define a Pydantic model called `User` with fields `name` (str) and `age` (int).
- Create a POST endpoint `/user/` that accepts the user details in JSON format.
- The response should be a JSON object with a key "message" confirming the creation of the user.

### Test Cases
```python
# Example test case
import requests

user_data = {"name": "John", "age": 30}
response = requests.post("http://127.0.0.1:8000/user/", json=user_data)
assert response.json() == {"message": "User John aged 30 created!"}

user_data = {"name": "Alice", "age": 25}
response = requests.post("http://127.0.0.1:8000/user/", json=user_data)
assert response.json() == {"message": "User Alice aged 25 created!"}
```

### Hints
- Make sure to install Pydantic, if you haven't already, as it is used for validating request bodies.
- Test your endpoint using a tool like Postman or curl for sending JSON data.

---

## Exercise 4: Adding Query Parameters to Your Endpoint
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Enhance the `/greet/` endpoint to accept an optional query parameter for language to customize the greeting.

### Starter Code
```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/greet/{name}")
def greet_user(name: str, lang: Optional[str] = None):
    # TODO: Customize greeting based on the lang query parameter
    if lang == "es":
        return {"message": f"¡Hola, {name}!"}
    return {"message": f"Hello, {name}!"}
```

### Requirements
- Modify the existing `/greet/{name}` endpoint to accept an optional query parameter `lang`.
- If `lang` is "es", return a greeting in Spanish; otherwise, return the default English greeting.

### Test Cases
```python
# Example test cases
response = requests.get("http://127.0.0.1:8000/greet/John")
assert response.json() == {"message": "Hello, John!"}

response = requests.get("http://127.0.0.1:8000/greet/John?lang=es")
assert response.json() == {"message": "¡Hola, John!"}
```

### Hints
- Use Python’s `Optional` type to indicate that the query parameter is not required.
- Be careful with string comparisons, ensuring that the case matches.

---

## Exercise 5: Handling Errors with Custom Exception Handling
**Difficulty:** Advanced  
**Time Estimate:** 45 minutes

### Objective
Implement custom error handling for the user creation endpoint to manage invalid input.

### Starter Code
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

    @validator('age')
    def age_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Age must be a positive integer')
        return v

@app.post("/user/")
def create_user(user: User):
    # TODO: Handle potential validation errors
    return {"message": f"User {user.name} aged {user.age} created!"}
```

### Requirements
- Add validation to ensure that the `age` field is a positive integer.
- If the validation fails, raise an `HTTPException` with a 400 status code and a message indicating the issue.

### Test Cases
```python
# Example test cases
response = requests.post("http://127.0.0.1:8000/user/", json={"name": "John", "age": 30})
assert response.json() == {"message": "User John aged 30 created!"}

response = requests.post("http://127.0.0.1:8000/user/", json={"name": "Alice", "age": -5})
assert response.status_code == 400
assert response.json() == {"detail": [{"loc": ["age"], "msg": "Age must be a positive integer", "type": "value_error"}]}
```

### Hints
- Use FastAPI's built-in validation features with Pydantic models to handle errors efficiently.
- Test your endpoint with both valid and invalid input to ensure proper error handling.

---

These exercises provide a structured approach to learning FastAPI, gradually increasing in complexity while allowing students to build real-world applications incrementally.