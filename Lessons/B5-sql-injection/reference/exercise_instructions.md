---
title: Advance sql injection - Exercise Instructions
layout: layouts/course.njk
courseId: B5-sql-injection
tags:
  - exercises
  - practice
date: 2025-12-03T19:43:34.155881
---
### Advanced SQL Injection Exercises

---

#### Exercise 1: Master Key Concepts of Advanced SQL Injection

**Objective:**
Understand and identify advanced SQL injection techniques such as blind SQLi, error-based, and time-based injections.

**Task:**
You are given access to a vulnerable web application that has a login form. Your task is to identify and exploit the SQL injection vulnerabilities using different injection types.

**Step-by-step Instructions:**
1. Access the login page of the test application.
2. Perform a classic SQL injection on the username field with `' OR '1'='1` to bypass authentication.
3. Attempt an error-based SQL injection by injecting payloads like `' OR 1=CONVERT(int,(SELECT @@version))--` to retrieve database version info from error messages.
4. Perform a blind SQL injection using time delays: inject `'; IF (SUBSTRING((SELECT TOP 1 name FROM sysobjects),1,1) = 'a') WAITFOR DELAY '00:00:05'--` and observe response times to infer data.
5. Document the type of injection used and the output/result observed.

**Acceptance Criteria:**
- Successfully bypass login using classic SQLi.
- Extracted database version or error details via error-based injection.
- Extracted at least one character of data using time-based blind SQLi.
- Detailed documentation of payloads and responses.

**Hints:**
- Use single quotes carefully to avoid syntax errors.
- Time-based injections require careful observation of response delays.
- Error messages can reveal database information; try to trigger them deliberately.

---

#### Exercise 2: Apply Practical Techniques to Extract Data

**Objective:**
Use advanced SQL injection techniques to enumerate database schema and extract sensitive data.

**Task:**
Using blind SQL injection, enumerate the names of tables in the database and extract the first user’s password hash from a `users` table.

**Step-by-step Instructions:**
1. Identify the injection point in the web application (e.g., search or login input).
2. Use blind SQLi Boolean conditions to enumerate the number of tables in the current database. Example payload snippet:
   ```sql
   ' AND (SELECT COUNT(*) FROM information_schema.tables) > 5 --
   ```
3. Use character-by-character extraction with blind SQLi to get table names from `information_schema.tables`.
4. Once you find the `users` table, extract the first username and password hash using the same blind SQLi technique.
5. Automate extraction using a script or tool if possible.

**Acceptance Criteria:**
- Correctly enumerated number of tables.
- Retrieved at least one table name accurately.
- Extracted the first username and password hash from the `users` table.
- Provided payloads and methodology used.

**Hints:**
- Boolean-based blind SQLi involves guessing characters one at a time.
- Use ASCII values and compare them in your payloads.
- Patience is key for blind SQLi as it’s slow by nature.

---

#### Exercise 3: Build a Real-World Project - SQL Injection Exploitation Tool

**Objective:**
Develop a simple command-line tool/script to automate blind SQL injection data extraction.

**Task:**
Create a Python script that accepts a vulnerable URL and an injection parameter, then extracts database information (e.g., database version, table names) using time-based blind SQL injection.

**Step-by-step Instructions:**
1. Set up your development environment with Python 3 and `requests` library.
2. Write a function to send HTTP requests with injected payloads and measure response time.
3. Implement logic to perform character-by-character extraction of a given string using time delays (e.g., 5 seconds delay for TRUE conditions).
4. Use the script to extract the database version from the web app.
5. Extend the script to extract table names from the database.
6. Document how to run the script and interpret results.

**Acceptance Criteria:**
- Python script successfully interacts with the vulnerable app.
- Correctly extracts and prints database version.
- Extracts at least one table name using blind SQLi automation.
- Code is clean, commented, and easy to run.

**Hints:**
- Use a timeout threshold slightly less than the delay you inject to detect TRUE conditions.
- Structure your script for easy modification of payloads and parameters.
- Test with smaller payloads to avoid long wait times during debugging.

---

#### Exercise 4: Advanced Challenge – Bypass WAF and Extract Data

**Objective:**
Learn techniques to evade Web Application Firewalls (WAFs) and perform advanced SQL injection.

**Task:**
You are provided with a vulnerable web app protected by a basic WAF that blocks common SQLi payload keywords (e.g., `UNION`, `SELECT`, `' OR 1=1`).

**Step-by-step Instructions:**
1. Identify what payloads get blocked by the WAF.
2. Research and test payload obfuscation techniques such as:
   - Using string concatenation (`SE'LE'CT`)
   - Using comments to split keywords (`SE/**/LECT`)
   - Encoding payloads in hexadecimal or Unicode
3. Use bypassed payloads to extract database version or dump user data.
4. Document the payloads blocked, bypass methods used, and results.

**Acceptance Criteria:**
- Identified at least 3 blocked keywords/payloads.
- Successfully bypassed WAF filtering using obfuscation techniques.
- Extracted at least one piece of database information despite WAF.
- Detailed report on bypass strategies and payload examples.

**Hints:**
- WAFs often rely on pattern matching; small changes can evade detection.
- Use online SQL encoder tools to generate encoded payloads.
- Test payloads incrementally to identify what triggers the WAF.

---

These exercises will progressively build your advanced SQL injection skills with hands-on practice, culminating in real-world exploitation and evasion techniques.
