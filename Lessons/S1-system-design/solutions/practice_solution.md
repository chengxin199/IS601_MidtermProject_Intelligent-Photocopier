---
title: introduction to system design - Practice Solution
layout: layouts/course.njk
courseId: S1-system-design
tags:
  - solutions
  - code
date: 2025-12-05T01:22:20.772963
---
# Introduction to System Design - Practice Solution Document

## Learning Objectives
- Master key concepts
- Apply practical techniques
- Build real-world projects

---

## Exercise 1: URL Shortener

### Overview
In this exercise, we will build a simple URL shortener. The basic functionality will allow the user to shorten a given URL. The enhanced version will include error handling and validation for the URL format.

### Basic Implementation

```python
import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "http://short.ly/"

    def shorten_url(self, original_url):
        # Generate a random string of fixed length
        short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        # Store the mapping of short ID to original URL
        self.url_mapping[short_id] = original_url
        return self.base_url + short_id

# Example usage
url_shortener = URLShortener()
short_url = url_shortener.shorten_url("https://www.example.com")
print(short_url)
```

### Enhanced Implementation

```python
import random
import string
import re

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "http://short.ly/"

    def is_valid_url(self, url):
        # Basic URL validation using regex
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

    def shorten_url(self, original_url):
        # Validate the URL before shortening
        if not self.is_valid_url(original_url):
            raise ValueError("Invalid URL format")
        
        # Generate a random string of fixed length
        short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        # Store the mapping of short ID to original URL
        self.url_mapping[short_id] = original_url
        return self.base_url + short_id

# Example usage
try:
    url_shortener = URLShortener()
    short_url = url_shortener.shorten_url("https://www.example.com")
    print(short_url)
except ValueError as e:
    print(e)
```

### Testing the Solution

```python
def test_url_shortener():
    url_shortener = URLShortener()

    # Test valid URL shortening
    short_url = url_shortener.shorten_url("https://www.example.com")
    assert short_url.startswith(url_shortener.base_url), "Short URL should start with base URL"

    # Test URL mapping exists
    original_url = url_shortener.url_mapping[short_url.split("/")[-1]]
    assert original_url == "https://www.example.com", "The original URL should match"

    # Test invalid URL raises ValueError
    try:
        url_shortener.shorten_url("invalid_url")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected outcome

test_url_shortener()
print("All tests passed!")
```

### Explanation
- **Design Decisions**: The system maps a short ID to the original URL using a dictionary for O(1) retrieval time. A regular expression is used for basic URL validation.
- **Key Concepts**: URL shortening, mapping, error handling, and validation.
- **Complexity Analysis**:
  - Time Complexity: O(1) for both inserting and retrieving a URL.
  - Space Complexity: O(n), where n is the number of unique URLs stored.

### Key Takeaways
- Implement error handling to manage invalid inputs.
- Use regular expressions for input validation.
- Ensure code is modular and testable by separating concerns.

---

## Exercise 2: Simple Rate Limiter

### Overview
This exercise involves designing a simple rate limiter that restricts the number of requests a user can make to a service in a given time window. The basic version will simply count requests, while the enhanced version will include error handling and a more flexible time window configuration.

### Basic Implementation

```python
import time

class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []

    def is_allowed(self):
        current_time = time.time()
        # Remove old requests
        self.requests = [req for req in self.requests if req > current_time - self.time_window]

        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True
        return False

# Example usage
rate_limiter = RateLimiter(5, 60)  # 5 requests per minute
for i in range(10):
    print(rate_limiter.is_allowed())  # Should print True for the first 5, then False
```

### Enhanced Implementation

```python
import time

class RateLimiter:
    def __init__(self, max_requests, time_window):
        if max_requests <= 0 or time_window <= 0:
            raise ValueError("max_requests and time_window must be positive integers")
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []

    def is_allowed(self):
        current_time = time.time()
        # Remove old requests
        self.requests = [req for req in self.requests if req > current_time - self.time_window]

        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True
        return False

# Example usage
try:
    rate_limiter = RateLimiter(5, 60)
    for i in range(10):
        print(rate_limiter.is_allowed())  # Should print True for the first 5, then False
except ValueError as e:
    print(e)
```

### Testing the Solution

```python
def test_rate_limiter():
    rate_limiter = RateLimiter(5, 10)  # 5 requests every 10 seconds
    results = []

    # Simulate 7 requests
    for _ in range(7):
        results.append(rate_limiter.is_allowed())
        time.sleep(1)  # Wait 1 second between requests

    # The first 5 should be allowed, the last 2 should be denied
    assert results[:5] == [True] * 5, "First 5 requests should be allowed"
    assert results[5:] == [False, False], "Last 2 requests should be denied"

test_rate_limiter()
print("All tests passed!")
```

### Explanation
- **Design Decisions**: The rate limiter uses a sliding window approach, storing request timestamps and filtering out old requests to maintain the count.
- **Key Concepts**: Rate limiting, time windows, request counting, error handling.
- **Complexity Analysis**:
  - Time Complexity: O(n) for filtering requests.
  - Space Complexity: O(n) for storing request timestamps.

### Key Takeaways
- Implement error handling for invalid configurations.
- Use an efficient data structure to maintain state.
- Test edge cases, such as exceeding the request limit.

---

This document provides a structured approach to understanding and implementing key concepts in system design. Each exercise features both basic and enhanced implementations, with thorough explanations and testing strategies.