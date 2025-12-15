---
title: Introduction to fastapi - Quick Reference
layout: layouts/course.njk
courseId: Z4-fastapi-intro
permalink: /Lessons/Z4-fastapi-intro/quick-reference.html
tags:
  - reference
  - quick-guide
date: 2025-12-15T23:12:55.051789
---
# FastAPI Quick Reference Guide

## Course Overview
- **Duration:** 1-2 hours
- **Level:** Beginner
- **Topics Covered:**
  - Introduction to FastAPI
  - Core Concepts
  - Advanced Techniques
  - Best Practices
  - Summary

---

## 1. Introduction to FastAPI
- **What is FastAPI?**
  - A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
  
- **Key Features:**
  - Fast to code: Increase the speed of development.
  - Fewer bugs: Reduce human error with automatic data validation.
  - High performance: Comparable to NodeJS and Go.
  - Easy to use: Designed for beginners and experts alike.

---

## 2. Core Concepts

### 2.1. FastAPI Basics
- **Installation:**
  ```bash
  pip install fastapi uvicorn
  ```

- **Creating a Simple App:**
  ```python
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/")
  def read_root():
      return {"Hello": "World"}
  ```

- **Running the App:**
  ```bash
  uvicorn main:app --reload
  ```

### 2.2. Path Parameters
- **Example:**
  ```python
  @app.get("/items/{item_id}")
  def read_item(item_id: int):
      return {"item_id": item_id}
  ```

### 2.3. Query Parameters
- **Example:**
  ```python
  @app.get("/items/")
  def read_item(skip: int = 0, limit: int = 10):
      return {"skip": skip, "limit": limit}
  ```

### 2.4. Request Body
- **Using Pydantic for Data Validation:**
  ```python
  from pydantic import BaseModel

  class Item(BaseModel):
      name: str
      price: float
      is_offer: bool = None

  @app.post("/items/")
  def create_item(item: Item):
      return item
  ```

---

## 3. Advanced Techniques

### 3.1. Dependency Injection
- **Example:**
  ```python
  from fastapi import Depends

  def get_query_param(q: str = None):
      return q

  @app.get("/items/")
  def read_item(query: str = Depends(get_query_param)):
      return {"query": query}
  ```

### 3.2. Middleware
- **Example:**
  ```python
  from starlette.middleware.cors import CORSMiddleware

  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )
  ```

### 3.3. Background Tasks
- **Example:**
  ```python
  from fastapi import BackgroundTasks

  def write_log(message: str):
      with open("log.txt", mode="a") as log:
          log.write(message)

  @app.post("/send-notification/")
  def send_notification(email: str, background_tasks: BackgroundTasks):
      background_tasks.add_task(write_log, f"Notification sent to {email}")
      return {"message": "Notification sent"}
  ```

---

## 4. Best Practices
- **Use Pydantic Models:** For data validation and serialization.
- **Organize Code:** Separate routes, models, and services into different files.
- **Use Type Hints:** Enhances code readability and helps with auto-completion in IDEs.
- **Documentation:** FastAPI automatically generates interactive API docs (Swagger UI) at `/docs`.

---

## 5. Summary
- FastAPI is a powerful framework for building APIs quickly and efficiently with Python.
- Utilize path and query parameters, request bodies, and dependency injection for robust API design.
- Follow best practices to maintain clean, readable, and efficient code.

---

## Troubleshooting Quick Fixes
- **Server not starting:** Ensure `uvicorn` is installed and the correct module is referenced.
  - Command: `uvicorn main:app --reload`
  
- **404 Error:** Check the endpoint URL and ensure the corresponding function is defined.
  
- **Validation Error:** Ensure the request body matches the Pydantic model structure.

- **CORS Issues:** Ensure CORS middleware is correctly configured if accessing from a different origin.

---

This guide serves as a practical reference for coding with FastAPI. For further learning, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).