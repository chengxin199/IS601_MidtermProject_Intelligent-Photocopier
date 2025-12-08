---
title: Introduction to sql injection - Exercise Instructions
layout: layouts/course.njk
courseId: S1-sql-injection
tags:
  - exercises
  - practice
date: 2025-12-08T16:41:58.216230
---
## Exercise 1: Basic SQL Injection Attack Simulation
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Implement a simple program that simulates an SQL injection attack on a mock database. The goal is to demonstrate how an attacker can manipulate SQL queries through user input.

### Starter Code
```python
# Mock database of users
mock_database = {
    "user1": "password1",
    "user2": "password2"
}

def authenticate_user(username, password):
    # TODO: Implement a simple SQL query simulation
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    return query

# Test the function with normal parameters
print(authenticate_user("user1", "password1"))  # Expected output: SQL query string
```

### Requirements
- Implement the `authenticate_user` function to construct an SQL query string.
- Handle a case where an SQL injection attempt is made (e.g., `username = "user1' OR '1'='1"`).
- Ensure the output displays the constructed SQL query.

### Test Cases
```python
# Example test cases
assert authenticate_user("user1", "password1") == "SELECT * FROM users WHERE username = 'user1' AND password = 'password1'"
assert authenticate_user("user1' OR '1'='1", "anything") == "SELECT * FROM users WHERE username = 'user1' OR '1'='1' AND password = 'anything'"
```

### Hints
- Remember to format the SQL query correctly with single quotes.
- Think about how SQL injection can change the logic of the query.

---

## Exercise 2: Detecting SQL Injection Patterns
**Difficulty:** Intermediate  
**Time Estimate:** 40 minutes

### Objective
Create a function that detects potential SQL injection patterns in user input.

### Starter Code
```python
import re

def detect_sql_injection(user_input):
    # TODO: Implement detection of SQL injection patterns
    pattern = r"(SELECT|INSERT|UPDATE|DELETE|--|;|'|\"|OR|AND|#)"
    if re.search(pattern, user_input, re.IGNORECASE):
        return True
    return False

# Test the function with some inputs
print(detect_sql_injection("SELECT * FROM users;"))  # Expected output: True
```

### Requirements
- Implement the `detect_sql_injection` function to check for SQL keywords and patterns.
- Return `True` if a potential SQL injection is detected, and `False` otherwise.
- Test with various inputs demonstrating both safe and unsafe strings.

### Test Cases
```python
# Example test cases
assert detect_sql_injection("SELECT * FROM users;") == True
assert detect_sql_injection("Hello World!") == False
assert detect_sql_injection("user' OR '1'='1") == True
```

### Hints
- Use regular expressions to effectively match different SQL keywords.
- Consider edge cases where the input might look benign but contains SQL commands.

---

## Exercise 3: Implementing Parameterized Queries
**Difficulty:** Intermediate  
**Time Estimate:** 50 minutes

### Objective
Refactor the previous code to use parameterized queries to prevent SQL injection.

### Starter Code
```python
import sqlite3

def create_user_table():
    conn = sqlite3.connect(':memory:')  # In-memory database for testing
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'password1')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user2', 'password2')")
    conn.commit()
    return conn

def authenticate_user(username, password, conn):
    # TODO: Implement parameterized query to prevent SQL injection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return cursor.fetchone() is not None

# Create the user table for testing
conn = create_user_table()
print(authenticate_user("user1", "password1", conn))  # Expected output: True
```

### Requirements
- Use parameterized queries in the `authenticate_user` function to safely handle user inputs.
- Return `True` if the user is authenticated and `False` otherwise.
- Create a test database structure to simulate user authentication.

### Test Cases
```python
# Example test cases
assert authenticate_user("user1", "password1", conn) == True
assert authenticate_user("user1' OR '1'='1", "anything", conn) == False
assert authenticate_user("user3", "password3", conn) == False
```

### Hints
- Look into using placeholders (`?`) in your SQL query to prevent injection.
- Remember to handle database connections and cursors properly to avoid memory leaks.

---

## Exercise 4: Logging SQL Injection Attempts
**Difficulty:** Intermediate  
**Time Estimate:** 60 minutes

### Objective
Extend the previous exercise to log any detected SQL injection attempts.

### Starter Code
```python
import sqlite3

def create_user_table():
    conn = sqlite3.connect(':memory:')  # In-memory database for testing
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'password1')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user2', 'password2')")
    conn.commit()
    return conn

def log_attempt(username):
    # TODO: Implement logging of detected SQL injection attempts
    print(f"SQL Injection attempt detected for username: {username}")

def authenticate_user(username, password, conn):
    # TODO: Implement parameterized query and logging
    if detect_sql_injection(username):
        log_attempt(username)
        return False
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return cursor.fetchone() is not None

# Create the user table for testing
conn = create_user_table()
print(authenticate_user("user1' OR '1'='1", "anything", conn))  # Expected output: False
```

### Requirements
- Implement the `log_attempt` function to log SQL injection attempts.
- Modify `authenticate_user` to log whenever a suspicious username is detected.
- Test with different inputs to ensure logging works correctly.

### Test Cases
```python
# Example test cases
assert authenticate_user("user1' OR '1'='1", "anything", conn) == False  # Should log an attempt
assert authenticate_user("user2", "password2", conn) == True  # Should not log
```

### Hints
- Think about how to combine the detection and logging functions effectively.
- Ensure that your logging mechanism is not too verbose but captures critical events.

---

This series of exercises progressively introduces SQL injection concepts, detection, prevention techniques, and logging, allowing students to build practical skills in securing applications against SQL injection vulnerabilities.