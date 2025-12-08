---
title: Intro for flask api - Exercise Instructions
layout: layouts/course.njk
courseId: F3-flask-api
permalink: /Lessons/F3-flask-api/exercise-instructions.html
tags:
  - exercises
  - practice
date: 2025-12-08T18:12:21.680281
---
## Exercise 1: Building a Simple Flask API
**Difficulty:** Beginner  
**Time Estimate:** 30 minutes  

### Objective
Implement a basic Flask API that returns a welcome message when accessed at the root endpoint.

### Starter Code
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    # TODO: Implement a welcome message
    return "Welcome to the Flask API!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- The API should return a simple welcome message when the root URL is accessed.
- Ensure the API runs in debug mode for easier error tracking.

### Test Cases
```python
# Test case to verify the welcome message
# You can use a tool like Postman or curl to test the API
# Expected output when accessing the root endpoint: "Welcome to the Flask API!"
```

### Hints
- Make sure you have Flask installed (`pip install Flask`).
- Run the application and navigate to `http://127.0.0.1:5000/` in your web browser.

---

## Exercise 2: Creating a User Registration Endpoint
**Difficulty:** Intermediate  
**Time Estimate:** 45 minutes  

### Objective
Enhance the Flask API by adding an endpoint that accepts user registration data and returns a success message.

### Starter Code
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # TODO: Extract user data from request and return a success message
    return jsonify(message="User registered successfully!")

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- The endpoint should accept a JSON payload containing `username` and `password`.
- Return a JSON response with a success message.
- Handle cases where the user data is incomplete and return a relevant error message.

### Test Cases
```python
# Test case to verify successful user registration
response = client.post('/register', json={"username": "testuser", "password": "testpass"})
assert response.json == {"message": "User registered successfully!"}

# Test case for missing username
response = client.post('/register', json={"password": "testpass"})
assert response.status_code == 400  # Bad request
assert response.json == {"error": "Username is required."}
```

### Hints
- Use `request.get_json()` to extract JSON data from the request.
- Validate input data before processing it.

---

## Exercise 3: Implementing a Simple In-Memory Storage
**Difficulty:** Intermediate  
**Time Estimate:** 60 minutes  

### Objective
Add an in-memory storage feature to keep track of registered users and return the list of registered users.

### Starter Code
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = []

@app.route('/register', methods=['POST'])
def register():
    # TODO: Implement user registration and store user in the users list
    return jsonify(message="User registered successfully!")

@app.route('/users', methods=['GET'])
def get_users():
    # TODO: Return the list of registered users
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Store each registered user in a list called `users`.
- Implement the `/users` endpoint to return the list of registered users in JSON format.
- Ensure the user registration does not allow duplicate usernames.

### Test Cases
```python
# Test case for user registration
client.post('/register', json={"username": "testuser", "password": "testpass"})
response = client.get('/users')
assert response.json == [{"username": "testuser"}]

# Test case for duplicate username
response = client.post('/register', json={"username": "testuser", "password": "newpass"})
assert response.status_code == 400  # Bad request
assert response.json == {"error": "Username already exists."}
```

### Hints
- Use a simple check to see if the username already exists in the `users` list.
- Remember to structure the user data as dictionaries before appending to the list.

---

## Exercise 4: Adding User Authentication
**Difficulty:** Advanced  
**Time Estimate:** 90 minutes  

### Objective
Enhance the Flask API to include user authentication using token-based authentication.

### Starter Code
```python
from flask import Flask, request, jsonify
import jwt  # You may need to install PyJWT
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

users = []

@app.route('/register', methods=['POST'])
def register():
    # TODO: Implement registration logic
    return jsonify(message="User registered successfully!")

@app.route('/login', methods=['POST'])
def login():
    # TODO: Implement login logic and return JWT token
    return jsonify(token="your_token")

@app.route('/protected', methods=['GET'])
def protected():
    # TODO: Implement protection for this route using JWT
    return jsonify(message="This is a protected route")

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Implement a `/login` endpoint that verifies user credentials and returns a JWT token.
- Protect the `/protected` endpoint so that it can only be accessed with a valid JWT token.
- Handle token expiration and return relevant error messages.

### Test Cases
```python
# Test case for user login and token retrieval
response = client.post('/login', json={"username": "testuser", "password": "testpass"})
assert 'token' in response.json

# Test case for accessing protected route without token
response = client.get('/protected')
assert response.status_code == 401  # Unauthorized

# Test case for accessing protected route with valid token
token = response.json['token']
response = client.get('/protected', headers={"Authorization": f"Bearer {token}"})
assert response.json == {"message": "This is a protected route"}
```

### Hints
- Use the `jwt.encode()` function to generate a token and `jwt.decode()` to verify it.
- Ensure you handle exceptions for invalid tokens and expired tokens appropriately.

---

These exercises will guide students from a basic understanding of Flask API development to more advanced topics like user authentication, giving them a solid foundation in building real-world projects.