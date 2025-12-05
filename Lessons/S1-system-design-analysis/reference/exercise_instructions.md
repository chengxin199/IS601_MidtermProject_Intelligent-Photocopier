---
title: Advance system design - Exercise Instructions
layout: layouts/course.njk
courseId: S1-system-design-analysis
tags:
  - exercises
  - practice
date: 2025-12-05T02:00:28.957532
---
## Exercise 1: Design a URL Shortener
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Implement a simple URL shortener service. The service should take a long URL and return a shortened version of it. Additionally, it should allow users to retrieve the original URL from the shortened version.

### Starter Code
```python
class URLShortener:
    def __init__(self):
        # TODO: Initialize a storage for the URLs
        self.url_map = {}
        self.base_url = "http://short.ly/"

    def shorten(self, long_url):
        # TODO: Implement URL shortening logic
        pass

    def retrieve(self, short_url):
        # TODO: Implement URL retrieval logic
        pass
```

### Requirements
- The `shorten` method should generate a unique identifier for the long URL and store it.
- The `retrieve` method should return the original URL based on the shortened version.
- Handle cases where the short URL does not exist.

### Test Cases
```python
url_shortener = URLShortener()
short_url = url_shortener.shorten("https://www.example.com")
assert url_shortener.retrieve(short_url) == "https://www.example.com"
assert url_shortener.retrieve("http://short.ly/nonexistent") == None  # Handle non-existent short URL
```

### Hints
- Consider using a hash function or counter to create unique identifiers.
- Ensure the mapping between short and long URLs is bi-directional.

---

## Exercise 2: Implement a Simple Cache
**Difficulty:** Advanced  
**Time Estimate:** 40 minutes

### Objective
Develop a simple in-memory caching system that supports `get`, `set`, and `delete` operations. The cache should expire entries after a given time.

### Starter Code
```python
import time

class SimpleCache:
    def __init__(self):
        # TODO: Initialize the cache storage
        self.cache = {}

    def set(self, key, value, ttl):
        # TODO: Store the value with the given key and expiration time
        pass

    def get(self, key):
        # TODO: Retrieve the value for the key if it hasn't expired
        pass

    def delete(self, key):
        # TODO: Remove the key from the cache
        pass
```

### Requirements
- The `set` method should take a time-to-live (TTL) argument to determine how long the entry should remain in the cache.
- The `get` method should return `None` for expired entries.
- Implement the `delete` method to remove entries from the cache.

### Test Cases
```python
cache = SimpleCache()
cache.set("key1", "value1", 5)
assert cache.get("key1") == "value1"
time.sleep(6)
assert cache.get("key1") is None  # After TTL expires
cache.delete("key1")
assert cache.get("key1") is None  # Ensure it's deleted
```

### Hints
- Use a dictionary to store cache entries along with their expiration timestamps.
- Use time comparison to determine if an entry is expired.

---

## Exercise 3: Create a Simple Distributed Task Queue
**Difficulty:** Advanced  
**Time Estimate:** 60 minutes

### Objective
Build a basic distributed task queue system that allows tasks to be added to a queue and processed by worker threads. Each worker should process tasks concurrently.

### Starter Code
```python
import threading
import queue
import time

class TaskQueue:
    def __init__(self):
        # TODO: Initialize the task queue
        self.task_queue = queue.Queue()

    def add_task(self, task):
        # TODO: Add a task to the queue
        pass

    def worker(self):
        # TODO: Implement the worker logic to process tasks
        while True:
            task = self.task_queue.get()
            if task is None:
                break
            # TODO: Execute the task
            self.task_queue.task_done()

    def start_workers(self, num_workers):
        # TODO: Start multiple worker threads
        for _ in range(num_workers):
            threading.Thread(target=self.worker).start()
```

### Requirements
- The `add_task` method should enqueue tasks.
- The `worker` method should handle processing of tasks from the queue.
- Implement a method to start multiple worker threads.

### Test Cases
```python
def example_task(n):
    time.sleep(1)  # Simulate a task taking time
    return n * n

task_queue = TaskQueue()
task_queue.start_workers(3)

for i in range(10):
    task_queue.add_task(example_task(i))

# Wait for all tasks to be processed
task_queue.task_queue.join()
```

### Hints
- Use the `queue.Queue` for thread-safe operations.
- Use `queue.task_done()` to signal task completion.

---

## Exercise 4: Rate Limiter Implementation
**Difficulty:** Advanced  
**Time Estimate:** 45 minutes

### Objective
Create a rate limiter class that restricts how many times a user can make requests in a given time frame.

### Starter Code
```python
import time

class RateLimiter:
    def __init__(self, rate: int, per: int):
        # TODO: Initialize rate limit parameters
        self.rate = rate
        self.per = per
        self.requests = []

    def allow_request(self):
        # TODO: Implement the logic to check if the request is allowed
        pass
```

### Requirements
- The constructor should accept the maximum number of requests (`rate`) allowed in a time frame (`per` seconds).
- The `allow_request` method should return `True` if the request is allowed, `False` otherwise.

### Test Cases
```python
rate_limiter = RateLimiter(2, 5)  # 2 requests per 5 seconds
assert rate_limiter.allow_request() == True
assert rate_limiter.allow_request() == True
assert rate_limiter.allow_request() == False  # Third request should be denied

time.sleep(5)  # Wait for the time window to reset
assert rate_limiter.allow_request() == True  # Should allow after reset
```

### Hints
- Use a list to track the timestamps of requests.
- Remove timestamps that are outside the allowed time window.

---

These exercises progressively build on system design concepts, incorporating practical implementations that mimic real-world scenarios. Each exercise includes clear objectives, starter code, requirements, test cases, and helpful hints to guide learners through the implementation process.