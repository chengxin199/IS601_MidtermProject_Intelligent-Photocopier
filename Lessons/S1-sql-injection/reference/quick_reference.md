---
title: Introduction to sql injection - Quick Reference
layout: layouts/course.njk
courseId: S1-sql-injection
tags:
  - reference
  - quick-guide
date: 2025-12-08T16:41:06.946761
---
# Quick Reference Guide: Introduction to SQL Injection

## Course Overview
- **Duration:** 3-4 hours
- **Level:** Intermediate
- **Topics Covered:**
  - Introduction
  - Core Concepts
  - Advanced Techniques
  - Best Practices
  - Summary

---

## 1. Introduction
SQL Injection (SQLi) is a code injection technique that exploits vulnerabilities in an application's software by allowing attackers to execute arbitrary SQL code.

### Key Points:
- **Impact:** Unauthorized data access, data manipulation, and potential data loss.
- **Targets:** Web applications that use SQL databases.

---

## 2. Core Concepts

### A. SQL Injection Types
- **In-band SQLi:** Directly retrieves data using the same communication channel.
  - **Example:** `SELECT * FROM users WHERE username = 'admin' OR '1'='1';`
  
- **Inferential SQLi:** No data is returned; attacker gathers information based on application behavior.
  - **Example:** `SELECT * FROM users WHERE username = 'admin' AND 1=1;` (true) vs. `AND 1=2;` (false)

- **Out-of-band SQLi:** Data is retrieved using a different channel, often when in-band methods are blocked.

### B. Common SQL Injection Patterns
- **Tautology:** Always true condition.
  - Example: `username' OR '1'='1' --`
  
- **Union-based:** Combines results from multiple SELECT statements.
  - Example: `UNION SELECT username, password FROM users;`

- **Commenting:** Ignoring the rest of the query.
  - Example: `username' --`

---

## 3. Advanced Techniques

### A. Error-based SQLi
- Exploits error messages to gather information about the database structure.
  - Example: `SELECT * FROM users WHERE id = 1; --`

### B. Blind SQL Injection
- No visible outputs; relies on the application’s response.
  - **Boolean-based:** Manipulates true/false conditions.
  - **Time-based:** Uses delays to infer information.
    - Example: `IF(1=1, SLEEP(5), 0);`

### C. Bypassing Filters
- Techniques to evade security measures (e.g., using different encodings).
  - Example: URL encoding: `%27` for `'`

---

## 4. Best Practices

### A. Prevention Techniques
- **Parameterized Queries:** Use prepared statements to prevent SQL injection.
  - Example (Python with SQLite):
    ```python
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    ```

- **Stored Procedures:** Encapsulate SQL queries.
  - Example:
    ```sql
    CREATE PROCEDURE GetUser(IN username VARCHAR(255))
    BEGIN
      SELECT * FROM users WHERE username = username;
    END;
    ```

- **Input Validation:** Sanitize and validate user inputs.

### B. Security Measures
- **Web Application Firewalls (WAF):** Monitor and filter HTTP requests.
- **Regular Security Audits:** Conduct vulnerability assessments.

---

## 5. Troubleshooting Quick Fixes

### A. Identifying SQL Injection Vulnerabilities
- **Check for user inputs:** Any input fields (login forms, search boxes).
- **Analyze error messages:** Look for database errors in responses.

### B. Fixing SQL Injection Issues
- **Refactor code:** Replace vulnerable queries with parameterized queries.
- **Update libraries:** Ensure database drivers and libraries are up-to-date.

### C. Testing for SQL Injection
- **Automated Tools:** Use tools like SQLMap for testing.
- **Manual Testing:** Craft payloads and observe application behavior.

---

## Summary
SQL Injection is a critical security vulnerability that can lead to severe consequences if not addressed. Understanding its core concepts, recognizing patterns, employing best practices, and implementing preventive measures are essential for securing web applications against SQL injection attacks. Always validate inputs and use prepared statements to mitigate risks.