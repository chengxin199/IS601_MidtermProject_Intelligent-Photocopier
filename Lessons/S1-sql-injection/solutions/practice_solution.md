---
title: Introduction to sql injection - Practice Solution
layout: layouts/course.njk
courseId: S1-sql-injection
tags:
  - solutions
  - code
date: 2025-12-08T16:42:24.722357
---
# Introduction to SQL Injection: Practice Solution Document

## Learning Objectives
- Master key concepts
- Apply practical techniques
- Build real-world projects

---

## Exercise 1: Basic SQL Injection Vulnerability

### Overview
In this exercise, we will demonstrate a basic SQL injection vulnerability by simulating a user login. The goal is to show how improper handling of user input can lead to SQL injection attacks.

### Basic Implementation

```python
import sqlite3

# Establish a connection to the SQLite database
def connect_db():
    conn = sqlite3.connect('users.db')
    return conn

# Create a simple user table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    # Insert a sample user
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
    conn.commit()
    conn.close()

# Function to authenticate user (Vulnerable to SQL Injection)
def authenticate(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    # SQL query directly from user input (Vulnerable)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user is not None
```

**Key Comments:**
- The `connect_db` function establishes a connection to the SQLite database.
- The `create_table` function creates a user table and inserts a sample user.
- The `authenticate` function constructs a SQL query using direct user input, making it vulnerable to SQL injection.

### Enhanced Implementation

```python
import sqlite3

# Establish a connection to the SQLite database
def connect_db():
    conn = sqlite3.connect('users.db')
    return conn

# Create a simple user table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    # Insert a sample user
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
    conn.commit()
    conn.close()

# Enhanced function to authenticate user (Using parameterized queries)
def authenticate(username, password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        # Use parameterized queries to prevent SQL injection
        query = "SELECT * FROM users WHERE username=? AND password=?"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        return user is not None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()
```

**Key Comments:**
- The enhanced `authenticate` function uses parameterized queries instead of direct string interpolation to prevent SQL injection.
- Error handling is added to catch database errors and ensure the connection is closed properly.

### Testing the Solution

```python
def test_authenticate():
    create_table()  # Setup test database

    # Test valid login
    assert authenticate('admin', 'password123') == True, "Test case failed: Valid credentials should return True"
    
    # Test invalid login
    assert authenticate('admin', 'wrongpassword') == False, "Test case failed: Invalid credentials should return False"
    
    # Test SQL injection attempt
    assert authenticate("' OR '1'='1", "' OR '1'='1") == False, "Test case failed: SQL Injection should not succeed"

# Run tests
test_authenticate()
print("All tests passed!")
```

### Explanation
- The `test_authenticate` function sets up the user table and runs assertions to verify the `authenticate` function's behavior.
- The tests cover valid credentials, invalid credentials, and a SQL injection attempt.

### Key Takeaways
- Always use parameterized queries to prevent SQL injection.
- Handle database errors gracefully and ensure connections are closed.
- Test your code thoroughly with various scenarios, including edge cases like SQL injection attempts.

---

## Alternative Approaches
1. **ORM (Object-Relational Mapping)**: Using an ORM like SQLAlchemy can abstract away raw SQL queries and provide built-in protection against SQL injection.
2. **Web Frameworks**: Many web frameworks (e.g., Django, Flask) provide mechanisms to protect against SQL injection by default.

By following best practices and understanding the underlying concepts, developers can write secure code and build resilient applications.