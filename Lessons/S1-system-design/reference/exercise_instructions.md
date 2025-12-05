---
title: introduction to system design - Exercise Instructions
layout: layouts/course.njk
courseId: S1-system-design
tags:
  - exercises
  - practice
date: 2025-12-05T01:21:38.663563
---
## Exercise 1: Simple URL Shortener
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Implement a simple URL shortener that takes a long URL and generates a shortened version. The shortened URL should map back to the original URL.

### Starter Code
```python
class URLShortener:
    def __init__(self):
        # TODO: Initialize your data structures here
        self.url_mapping = {}
        self.base_url = "http://short.ly/"
        self.counter = 0

    def shorten(self, long_url):
        # TODO: Implement the logic to shorten the URL
        pass

    def retrieve(self, short_url):
        # TODO: Implement the logic to retrieve the original URL
        pass
```

### Requirements
- Implement a method `shorten(long_url)` that returns a shortened URL.
- Implement a method `retrieve(short_url)` that returns the original URL.
- Handle edge cases where the URL is invalid or the shortened URL does not exist.

### Test Cases
```python
shortener = URLShortener()
short_url = shortener.shorten("https://www.example.com")
assert short_url.startswith("http://short.ly/")

original_url = shortener.retrieve(short_url)
assert original_url == "https://www.example.com"

# Test for an invalid short URL
assert shortener.retrieve("http://short.ly/invalid") is None
```

### Hints
- You can use a dictionary to map short URLs to long URLs.
- Consider using a simple counter to generate unique short URLs.

---

## Exercise 2: Basic Rate Limiter
**Difficulty:** Advanced  
**Time Estimate:** 45 minutes

### Objective
Implement a rate limiter that restricts the number of requests a user can make to a service in a given time frame (e.g., 5 requests per minute).

### Starter Code
```python
import time

class RateLimiter:
    def __init__(self, limit, period):
        # TODO: Initialize the rate limit parameters
        self.limit = limit
        self.period = period
        self.requests = {}

    def is_allowed(self, user_id):
        # TODO: Implement the logic to check if the request is allowed
        pass
```

### Requirements
- Initialize the rate limiter with a limit and a period.
- Implement `is_allowed(user_id)` that returns `True` if the request is allowed and `False` otherwise.
- Handle edge cases for users who exceed their limits.

### Test Cases
```python
limiter = RateLimiter(5, 60)  # 5 requests per minute

# Simulate requests
user_id = "user123"
for _ in range(5):
    assert limiter.is_allowed(user_id) == True

# Sixth request should be denied
assert limiter.is_allowed(user_id) == False

time.sleep(60)  # Wait for the period to reset

# After waiting, requests should be allowed again
assert limiter.is_allowed(user_id) == True
```

### Hints
- Use a dictionary to track the timestamps of requests by each user.
- Clean up old requests that are outside the allowed time period.

---

## Exercise 3: Simple Message Queue
**Difficulty:** Advanced  
**Time Estimate:** 60 minutes

### Objective
Create a simple message queue system that allows sending and receiving messages with the ability to handle multiple producers and consumers.

### Starter Code
```python
from collections import deque
import threading

class MessageQueue:
    def __init__(self):
        # TODO: Initialize the message queue
        self.queue = deque()
        self.lock = threading.Lock()
    
    def send(self, message):
        # TODO: Implement the logic to send a message to the queue
        pass

    def receive(self):
        # TODO: Implement the logic to receive a message from the queue
        pass
```

### Requirements
- Implement a `send(message)` method that adds a message to the queue.
- Implement a `receive()` method that retrieves and removes a message from the queue.
- Ensure thread-safety for concurrent access to the queue.

### Test Cases
```python
mq = MessageQueue()

# Sending messages
mq.send("Hello")
mq.send("World")

# Receiving messages
assert mq.receive() == "Hello"
assert mq.receive() == "World"

# Test receiving from an empty queue should return None
assert mq.receive() is None
```

### Hints
- Use a `deque` from the `collections` module for efficient append and pop operations.
- Use a threading lock to manage access to the queue when multiple threads are involved.

---

## Exercise 4: Cache System with LRU Eviction
**Difficulty:** Advanced  
**Time Estimate:** 75 minutes

### Objective
Implement an LRU (Least Recently Used) cache that stores a fixed number of key-value pairs. When the cache reaches its limit, it should evict the least recently used item.

### Starter Code
```python
class LRUCache:
    def __init__(self, capacity):
        # TODO: Initialize the cache structure
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        # TODO: Implement the get logic
        pass

    def put(self, key, value):
        # TODO: Implement the put logic
        pass
```

### Requirements
- Implement a `get(key)` method that retrieves the value and updates its usage.
- Implement a `put(key, value)` method that adds or updates the key-value pair and manages cache eviction.
- Handle edge cases for getting a non-existent key.

### Test Cases
```python
cache = LRUCache(2)

# Adding items
cache.put(1, "A")
cache.put(2, "B")
assert cache.get(1) == "A"  # Returns "A"

# Adding a new item should evict the least recently used (key 2)
cache.put(3, "C")
assert cache.get(2) is None  # Key 2 should have been evicted

# Accessing key 1 makes it most recently used
cache.put(4, "D")  # This should evict key 1
assert cache.get(1) is None  # Key 1 should have been evicted
assert cache.get(3) == "C"
assert cache.get(4) == "D"
```

### Hints
- Consider using an `OrderedDict` from the `collections` module to maintain the order of keys based on access.
- Remember to update the order whenever a key is accessed or added.

---

By working through these exercises, students will gain a solid understanding of core system design concepts and practical implementations. Happy coding!