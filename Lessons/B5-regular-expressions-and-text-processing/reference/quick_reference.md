# Quick Reference Guide: Regular Expressions and Text Processing

## Course Overview
- **Duration:** 3-4 hours
- **Level:** Intermediate

---

## Key Concepts

### What are Regular Expressions?
- **Definition:** A sequence of characters that defines a search pattern, primarily for string matching.
- **Use Cases:** Data validation, searching, replacing, and parsing text.

### Components of Regular Expressions
- **Literals:** Exact characters to match (e.g., `cat` matches "cat").
- **Metacharacters:** Special characters with specific meanings (e.g., `.`, `*`, `?`, `+`, `^`, `$`).

---

## Common Patterns and Syntax Examples

### Basic Syntax
- **`.`** - Matches any single character.
  - **Example:** `a.b` matches "acb", "axb", but not "ab".
  
- **`*`** - Matches 0 or more of the preceding element.
  - **Example:** `ab*c` matches "ac", "abc", "abbc".
  
- **`+`** - Matches 1 or more of the preceding element.
  - **Example:** `ab+c` matches "abc", "abbc", but not "ac".
  
- **`?`** - Matches 0 or 1 of the preceding element.
  - **Example:** `ab?c` matches "ac" or "abc".

### Character Classes
- **`[abc]`** - Matches any character in the brackets.
  - **Example:** `[aeiou]` matches any vowel.
  
- **`[^abc]`** - Matches any character NOT in the brackets.
  - **Example:** `[^aeiou]` matches any consonant.

### Anchors
- **`^`** - Asserts position at the start of a string.
  - **Example:** `^abc` matches "abc" at the beginning.
  
- **`$`** - Asserts position at the end of a string.
  - **Example:** `abc$` matches "abc" at the end.

### Quantifiers
- **`{n}`** - Matches exactly n occurrences.
  - **Example:** `a{3}` matches "aaa".
  
- **`{n,}`** - Matches n or more occurrences.
  - **Example:** `a{2,}` matches "aa", "aaa", etc.
  
- **`{n,m}`** - Matches between n and m occurrences.
  - **Example:** `a{1,3}` matches "a", "aa", or "aaa".

### Grouping and Alternation
- **`(abc)`** - Groups a pattern.
  - **Example:** `(abc)+` matches "abc", "abcabc".
  
- **`|`** - Acts as a logical OR.
  - **Example:** `cat|dog` matches either "cat" or "dog".

---

## Code Snippets

### Python Example
```python
import re

# Search for a pattern
pattern = r'\d{3}-\d{2}-\d{4}'  # Matches a SSN format
text = "My SSN is 123-45-6789"
match = re.search(pattern, text)

if match:
    print("Found:", match.group())
```

### JavaScript Example
```javascript
let text = "Contact: 555-1234";
let pattern = /\d{3}-\d{4}/; // Matches phone number format
let match = text.match(pattern);

if (match) {
    console.log("Found:", match[0]);
}
```

---

## Troubleshooting Quick Fixes

### Common Issues
- **Issue:** Pattern not matching expected text.
  - **Fix:** Check if you need to escape special characters (e.g., `.` becomes `\.`).
  
- **Issue:** Matching too much or too little.
  - **Fix:** Review quantifiers and ensure they fit your requirements (e.g., use `+` instead of `*` for one or more).

- **Issue:** Case sensitivity.
  - **Fix:** Use case-insensitive flags (e.g., `re.IGNORECASE` in Python or `i` flag in JavaScript).

### Debugging Tips
- Use online regex testers (e.g., regex101.com) to visualize and test your patterns.
- Break down complex expressions into smaller parts to isolate issues.

---

## Before You Start (Preflight)
- Ensure you have a basic understanding of programming concepts.
- Familiarize yourself with the development environment and language you will be using (Python, JavaScript, etc.).
- Install any necessary libraries (e.g., `re` for Python).

---

## Outcomes
- Understand and apply regular expressions for text processing tasks.
- Create and troubleshoot regex patterns effectively.
- Implement regex in programming languages for real-world applications.

---

This quick reference guide serves as a handy tool for applying regular expressions in text processing tasks. Keep it accessible during coding sessions for efficient problem-solving!