---
title: Advance system design - Practice Solution
layout: layouts/course.njk
courseId: S1-system-design-analysis
tags:
  - solutions
  - code
date: 2025-12-05T02:00:55.560266
---
# Advanced System Design Practice Solutions

## Learning Objectives
- Master key concepts
- Apply practical techniques
- Build real-world projects

---

## Exercise 1: Design a URL Shortener

### Overview
In this exercise, we will create a simple URL shortener. The basic functionality will take a long URL and return a shortened version. The enhanced version will include error handling and validation to ensure that the input is a valid URL.

### Basic Implementation

```python
import hashlib

class URLShortener:
    def __init__(self):
        # This dictionary will store the mapping of short URLs to long URLs
        self.url_map = {}

    def shorten_url(self, long_url):
        """
        Shorten the provided long URL.

        Args:
            long_url (str): The long URL to shorten.

        Returns:
            str: A shortened URL.
        """
        # Generate a unique hash for the long URL
        url_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]
        short_url = f"http://short.url/{url_hash}"
        
        # Store the mapping
        self.url_map[short_url] = long_url
        return short_url

# Sample usage
url_shortener = URLShortener()
short_url = url_shortener.shorten_url("https://www.example.com/some/long/url")
print(short_url)  # Outputs: http://short.url/xxxxx
```

### Enhanced Implementation

```python
import hashlib
import re

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def is_valid_url(self, url):
        """
        Validate if the given URL is valid.

        Args:
            url (str): URL to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IP...
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

    def shorten_url(self, long_url):
        """
        Shorten the provided long URL with validation.

        Args:
            long_url (str): The long URL to shorten.

        Returns:
            str: A shortened URL or an error message.
        """
        if not self.is_valid_url(long_url):
            raise ValueError("Invalid URL provided.")
        
        url_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]
        short_url = f"http://short.url/{url_hash}"
        
        self.url_map[short_url] = long_url
        return short_url

# Sample usage
try:
    url_shortener = URLShortener()
    short_url = url_shortener.shorten_url("https://www.example.com/some/long/url")
    print(short_url)  # Outputs: http://short.url/xxxxx
except ValueError as e:
    print(e)
```

### Testing the Solution

```python
def test_url_shortener():
    url_shortener = URLShortener()
    
    # Test valid URL shortening
    assert url_shortener.shorten_url("https://www.example.com") == "http://short.url/5d414"
    assert url_shortener.shorten_url("https://www.example.com") == "http://short.url/5d414"
    
    # Test invalid URL
    try:
        url_shortener.shorten_url("invalid-url")
    except ValueError as e:
        assert str(e) == "Invalid URL provided."
    
    print("All tests passed.")

# Run test
test_url_shortener()
```

### Explanation
- **Design Decisions**: We used a dictionary to map short URLs to long URLs for easy retrieval. The MD5 hash function generates a unique identifier for each URL, ensuring that the shortened version remains consistent.
- **Key Concepts**: URL validation is crucial for user input. We used regex to validate the URL format before processing it.
- **Complexity Analysis**: The time complexity for shortening a URL is O(1) for hash generation and storage. The space complexity is O(n) for storing the URL mappings.

### Key Takeaways
- Always validate user input to prevent errors.
- Use hashing for unique identifiers while keeping them short.
- Maintain clean code with comments for clarity, especially in production environments.

--- 

This document provides a comprehensive solution for designing a URL shortener system, demonstrating both basic and enhanced implementations, along with testing strategies and best practices for real-world applicability.