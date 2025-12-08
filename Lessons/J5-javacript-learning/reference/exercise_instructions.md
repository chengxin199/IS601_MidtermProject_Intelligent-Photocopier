---
title: Advance javascript - Exercise Instructions
layout: layouts/course.njk
courseId: J5-javacript-learning
permalink: /Lessons/J5-javacript-learning/exercise-instructions.html
tags:
  - exercises
  - practice
date: 2025-12-08T17:57:25.522159
---
## Exercise 1: Asynchronous Data Fetching
**Difficulty:** Advanced  
**Time Estimate:** 30 minutes

### Objective
Implement a function that fetches data from an API asynchronously, processes the retrieved data, and returns the results.

### Starter Code
```python
import aiohttp
import asyncio

async def fetch_data(url):
    # TODO: Implement this function to fetch data from the given URL
    pass

async def process_data(url):
    # TODO: Call fetch_data and process the returned data
    pass

# Entry point to run the async function
if __name__ == "__main__":
    url = "https://api.example.com/data"
    # TODO: Use asyncio to run process_data
```

### Requirements
- Fetch data from the provided API endpoint using `aiohttp`.
- Process the returned JSON data (e.g., filter or transform it).
- Handle network errors gracefully (e.g., timeouts, connection errors).

### Test Cases
```python
# Test cases for fetch_data and process_data
assert await fetch_data("https://api.example.com/data") is not None
assert await process_data("https://api.example.com/data") == expected_processed_data
```

### Hints
- Use `async with` for managing the session in aiohttp.
- Remember to handle potential exceptions when making network requests.

---

## Exercise 2: Dynamic Form Validation
**Difficulty:** Advanced  
**Time Estimate:** 40 minutes

### Objective
Create a dynamic form validation function that validates user input based on a schema.

### Starter Code
```python
def validate_form(data, schema):
    # TODO: Implement form validation based on the provided schema
    pass

# Example schema
schema = {
    'username': {'type': 'string', 'required': True},
    'age': {'type': 'integer', 'required': False},
}

# Example user input
user_input = {
    'username': 'JohnDoe',
    'age': 30
}
```

### Requirements
- Validate that required fields are present.
- Check types for each field based on the schema.
- Return a list of validation errors, if any.

### Test Cases
```python
# Test cases for validate_form
assert validate_form(user_input, schema) == []
assert validate_form({'username': ''}, schema) == ['username is required']
assert validate_form({'username': 123}, schema) == ['username must be a string']
```

### Hints
- Use Python's built-in `type()` to check data types.
- Consider using `try...except` blocks to handle type conversion errors.

---

## Exercise 3: Custom Error Handling Middleware
**Difficulty:** Advanced  
**Time Estimate:** 50 minutes

### Objective
Implement a custom error handling middleware for a web framework that catches exceptions and formats error responses.

### Starter Code
```python
class CustomErrorMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        # TODO: Implement error handling logic
        pass

# Example usage in a web application
app = CustomErrorMiddleware(your_web_app)

async def example_route():
    # TODO: Route logic that may raise an exception
    pass
```

### Requirements
- Catch different types of exceptions (e.g., 404, 500).
- Return a JSON response with an appropriate status code and message.
- Log the error details to the console.

### Test Cases
```python
# Test cases for error handling
assert await app.handle_request(404) == {'error': 'Not Found'}
assert await app.handle_request(500) == {'error': 'Internal Server Error'}
```

### Hints
- Use Python's built-in logging module to log errors.
- Familiarize yourself with the web framework’s response object for sending responses.

---

## Exercise 4: Real-time Chat Application
**Difficulty:** Advanced  
**Time Estimate:** 60 minutes

### Objective
Build a real-time chat application using WebSockets to send and receive messages.

### Starter Code
```python
import websockets
import asyncio

connected_clients = set()

async def chat_handler(websocket, path):
    # TODO: Implement the chat handling logic
    pass

# Start the WebSocket server
start_server = websockets.serve(chat_handler, 'localhost', 6789)

async def main():
    async with start_server:
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
```

### Requirements
- Handle new connections and disconnections.
- Broadcast messages to all connected clients.
- Store and display a history of messages.

### Test Cases
```python
# Test cases for chat functionality
# (This would typically involve setting up WebSocket clients to send and receive messages)
```

### Hints
- Use `async for` to receive messages from the WebSocket.
- Consider using a list or dictionary to manage the chat history.

---

## Exercise 5: API Rate Limiting
**Difficulty:** Advanced  
**Time Estimate:** 45 minutes

### Objective
Implement a rate limiting decorator that restricts the number of function calls to a specified limit over a time window.

### Starter Code
```python
import time
from functools import wraps

def rate_limiter(max_calls, period):
    # TODO: Implement rate limiting logic
    pass

@rate_limiter(max_calls=5, period=60)
def api_call():
    # TODO: Simulate an API call
    return "API call successful"

# Example usage
for _ in range(10):
    print(api_call())  # Test the rate limiter
```

### Requirements
- Ensure that the API can only be called a specified number of times in the given time period.
- If the limit is exceeded, raise an exception or return an error message.

### Test Cases
```python
# Test cases for rate_limiter
# (You may need to use time.sleep to test the rate limiting function)
```

### Hints
- Use a dictionary to track the number of calls made within the time window.
- Consider using `time.time()` to manage the timing of calls.