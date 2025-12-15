---
title: Introduction to fastapi - Practice Solution
layout: layouts/course.njk
courseId: Z4-fastapi-intro
permalink: /Lessons/Z4-fastapi-intro/practice-solution.html
tags:
  - solutions
  - code
date: 2025-12-15T23:14:17.979272
---
# Introduction to FastAPI - Practice Solution Document

## Overview

FastAPI is a modern web framework for building APIs with Python 3.6+ based on standard Python type hints. It is designed to be fast and easy to use, making it ideal for both beginners and advanced users. This document will guide you through key concepts of FastAPI via hands-on exercises, culminating in a simple RESTful API project.

## Learning Objectives

- Master key concepts of FastAPI
- Apply practical techniques to build APIs
- Build a real-world project using FastAPI

## Exercise 1: Building a Simple API

### Overview

In this exercise, we will create a simple API that manages a list of items. The API will allow users to create, read, update, and delete items.

### Basic Implementation

```python
# Importing required modules from FastAPI
from fastapi import FastAPI, HTTPException

# Initialize the FastAPI application
app = FastAPI()

# In-memory storage for items
items = {}

# Create an item
@app.post("/items/{item_id}")
def create_item(item_id: int, item: str):
    items[item_id] = item
    return {"item_id": item_id, "item": item}

# Read an item
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "item": items.get(item_id, "Item not found")}
```

### Enhanced Implementation

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for items
items = {}

# Define a model for the item using Pydantic
class Item(BaseModel):
    name: str

# Create an item with error handling
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item.name
    return {"item_id": item_id, "item": item.name}

# Read an item with error handling
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": items[item_id]}
```

### Testing the Solution

To test our FastAPI application, we can use the `httpx` library or FastAPI’s own test client.

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_item():
    response = client.post("/items/1", json={"name": "Test Item"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "item": "Test Item"}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "item": "Test Item"}

def test_read_nonexistent_item():
    response = client.get("/items/2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
```

### Explanation

- **Basic Implementation**: This version creates and reads items using basic dictionary storage without error handling.
- **Enhanced Implementation**: This version utilizes Pydantic for data validation and adds error handling with `HTTPException` for better user feedback.
- **Testing**: Uses FastAPI's `TestClient` to simulate requests and validate API responses. This helps ensure the API behaves as expected during development and after changes.

### Key Takeaways

- FastAPI simplifies API development with automatic validation via Pydantic.
- Error handling improves the robustness and user experience of your API.
- Testing is crucial in validating the correctness of your API endpoints.

## Exercise 2: Updating and Deleting Items

### Overview

For this exercise, we will extend our API to include functionality for updating and deleting items.

### Basic Implementation

```python
# Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    if item_id not in items:
        return {"error": "Item not found"}
    items[item_id] = item
    return {"item_id": item_id, "item": item}

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "Item not found"}
    del items[item_id]
    return {"message": "Item deleted"}
```

### Enhanced Implementation

```python
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item.name
    return {"item_id": item_id, "item": item.name}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted successfully"}
```

### Testing the Solution

```python
def test_update_item():
    client.post("/items/1", json={"name": "Test Item"})
    response = client.put("/items/1", json={"name": "Updated Item"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "item": "Updated Item"}

def test_delete_item():
    client.post("/items/2", json={"name": "Another Item"})
    response = client.delete("/items/2")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted successfully"}

def test_delete_nonexistent_item():
    response = client.delete("/items/3")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
```

### Explanation

- **Update and Delete**: The enhanced implementation leverages error handling to ensure that we respond appropriately to users trying to update or delete items that do not exist.
- **Testing**: Each function is tested to ensure it performs as expected, with assertions checking for both the expected status codes and response data.

### Key Takeaways

- Updating and deleting resources follows similar patterns in RESTful APIs.
- Proper error handling can significantly improve the clarity of API responses.
- Comprehensive tests ensure that changes to the API do not break existing functionality.

This document serves as a guide for beginners looking to understand and implement FastAPI. The exercises progressively build upon each other to give you a strong foundation in creating RESTful APIs.