# Regular Expressions and Text Processing Course

## Course Overview
**Title:** Regular Expressions and Text Processing  
**Duration:** 3-4 hours  
**Level:** Intermediate  
**Description:** Parse and transform text safely and efficiently.  

### Learning Objectives
- Understand the `re` module, including patterns, groups, named groups, and flags.
- Differentiate between compile vs inline regex and understand pre-compilation for hot paths.
- Distinguish between validation and extraction techniques.
- Safely escape strings using raw strings.
- Recognize performance pitfalls and mitigate catastrophic backtracking.
- Identify when to prefer structured parsers over regular expressions.

---

## Module 1: Introduction and Fundamentals

### Learning Goals
- Understand what regular expressions are and their purpose in text processing.
- Familiarize with the Python `re` module and its basic functionalities.

### Theoretical Explanations
Regular expressions (regex) are sequences of characters that form search patterns. They are used for matching strings in text processing tasks such as validation, searching, and manipulation.

The Python `re` module provides a powerful way to work with regex and includes functions for searching, matching, and replacing strings.

### Code Examples
```python
import re

# Simple regex matching
pattern = r'\d+'  # Matches one or more digits
text = "There are 123 apples"

match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}")  # Output: Found: 123
```

### Practical Exercises
1. Write a regex pattern to match email addresses.
2. Create a function that checks if a string is a valid phone number.

### Real-World Applications
- Form validation (emails, phone numbers)
- Data extraction from logs
- Syntax highlighting in text editors

---

## Module 2: Core Concepts and Theory

### Learning Goals
- Grasp the core components of regex patterns, including groups and flags.
- Understand the difference between compile and inline regex.

### Theoretical Explanations
- **Groups**: Parentheses `()` are used to create groups in regex, which can capture parts of the matched text.
- **Flags**: Modifiers that change how the regex engine behaves (e.g., `re.IGNORECASE`).

### Code Examples
```python
# Using groups
pattern = r'(\d+)-(\d+)-(\d+)'  # Matches dates in format DD-MM-YYYY
text = "Today's date is 23-03-2023"

match = re.search(pattern, text)
if match:
    print(f"Day: {match.group(1)}, Month: {match.group(2)}, Year: {match.group(3)}")
```

### Practical Exercises
1. Write regex to extract the year, month, and day from a given date string.
2. Explore different flags available in the `re` module and their effects.

### Real-World Applications
- Extracting structured data from unstructured text
- Transforming data formats

---

## Module 3: Practical Implementation

### Learning Goals
- Implement regex for validation and data extraction.
- Recognize when to use raw strings for regex patterns.

### Theoretical Explanations
- **Validation vs Extraction**: Validation checks if a string conforms to a pattern, while extraction retrieves data from a string.

### Code Examples
```python
# Validation example
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Simple email validation
emails = ["test@example.com", "invalid-email"]

for email in emails:
    if re.match(email_pattern, email):
        print(f"{email} is valid.")
    else:
        print(f"{email} is invalid.")
```

### Practical Exercises
1. Create a function that validates URLs.
2. Write a script that extracts all hashtags from a given text.

### Real-World Applications
- Ensuring user input meets required formats
- Scraping data from web pages

---

## Module 4: Advanced Techniques

### Learning Goals
- Master advanced regex techniques including named groups and lookaheads/lookbehinds.
- Understand performance considerations and how to avoid catastrophic backtracking.

### Theoretical Explanations
- **Named Groups**: Use `(?P<name>...)` to assign names to groups for better readability.
- **Lookaheads/Lookbehinds**: Assertions that allow checking for patterns without including them in the match.

### Code Examples
```python
# Named groups example
pattern = r'(?P<username>\w+)@(?P<domain>[\w\.-]+)'
text = "Contact me at john.doe@example.com"

match = re.search(pattern, text)
if match:
    print(f"Username: {match.group('username')}, Domain: {match.group('domain')}")
```

### Performance Considerations
- Avoid overly complex patterns that may lead to catastrophic backtracking.
- Use pre-compilation for frequently used patterns.

### Practical Exercises
1. Create a regex that matches valid IPv4 addresses using named groups.
2. Analyze a regex pattern that leads to performance issues and refactor it.

### Real-World Applications
- Optimizing regex for large datasets
- Building efficient parsers

---

## Module 5: Best Practices and Patterns

### Learning Goals
- Identify best practices for using regex in Python.
- Learn when to choose structured parsers over regex.

### Theoretical Explanations
- Always use raw strings for regex patterns to avoid escape sequence issues.
- When to use structured parsers (e.g., `xml.etree.ElementTree` for XML, `json` module for JSON) instead of regex.

### Code Examples
```python
# Best practice: Using raw strings
pattern = r'\b\w+\b'  # Matches whole words
text = "Hello, world!"

matches = re.findall(pattern, text)
print(matches)  # Output: ['Hello', 'world']
```

### Common Pitfalls
- Not using raw strings can lead to confusion with escape characters.
- Overusing regex for tasks better suited for structured parsers.

### Practical Exercises
1. Refactor a regex-based solution to use a structured parser instead.
2. Create a checklist of best practices for regex usage.

### Real-World Applications
- Developing maintainable and efficient codebases
- Ensuring security and performance in applications

---

## Conclusion
By the end of this course, you will have a comprehensive understanding of regular expressions and their applications in text processing. You will be equipped with the necessary skills to implement regex safely and efficiently in your projects. Happy coding!