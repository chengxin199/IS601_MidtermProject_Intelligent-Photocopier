---
title: Intro for flask api - Practice Solution
layout: layouts/course.njk
courseId: F3-flask-api
permalink: /Lessons/F3-flask-api/practice-solution.html
tags:
  - solutions
  - code
date: 2025-12-08T18:12:54.462785
---
# Intro to Flask API: Comprehensive Practice Solutions

This document aims to provide a comprehensive guide for building a simple RESTful API using Flask. We will cover key concepts, practical techniques, and real-world applications. The exercises will include both basic and enhanced implementations, with error handling, testing, and alternative approaches.

---

## Learning Objectives

- Master key concepts of Flask and RESTful APIs
- Apply practical techniques to implement a Flask API
- Build real-world projects to solidify understanding

---

## Exercise 1: Create a Basic Flask API

### Overview
In this exercise, we will create a simple Flask API that allows us to perform basic CRUD (Create, Read, Update, Delete) operations on a collection of items.

### Basic Implementation

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for items
items = []

@app.route('/items', methods=['GET'])
def get_items():
    """Retrieve the list of items."""
    return jsonify(items), 200

@app.route('/items', methods=['POST'])
def add_item():
    """Add a new item to the list."""
    item = request.json.get('item')
    items.append(item)
    return jsonify({'message': 'Item added', 'item': item}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

### Enhanced Implementation

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for items
items = []

@app.route('/items', methods=['GET'])
def get_items():
    """Retrieve the list of items."""
    return jsonify(items), 200

@app.route('/items', methods=['POST'])
def add_item():
    """Add a new item to the list with error handling."""
    if not request.json or 'item' not in request.json:
        abort(400, description="Invalid request: 'item' is required.")
    
    item = request.json['item']
    items.append(item)
    return jsonify({'message': 'Item added', 'item': item}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

### Testing the Solution

```python
import requests

# Test GET
response = requests.get('http://127.0.0.1:5000/items')
assert response.status_code == 200
assert response.json() == []

# Test POST
response = requests.post('http://127.0.0.1:5000/items', json={'item': 'Test Item'})
assert response.status_code == 201
assert response.json() == {'message': 'Item added', 'item': 'Test Item'}

# Test error handling
response = requests.post('http://127.0.0.1:5000/items', json={})
assert response.status_code == 400
assert 'Invalid request' in response.text
```

### Explanation

- **Key Concepts**: We utilize Flask's routing system to define API endpoints. The `jsonify` function helps format responses as JSON.
- **Error Handling**: In the enhanced version, we check for valid input and return a 400 error if the input is invalid.
- **Complexity**: The time complexity for adding and retrieving items is O(1) for both operations.

### Key Takeaways

- Always validate input data to avoid errors.
- Use appropriate HTTP status codes to indicate the result of API calls.
- Testing APIs with tools like `requests` helps ensure functionality.

---

## Exercise 2: Update and Delete Items

### Overview
In this exercise, we will enhance our Flask API to include functionality for updating and deleting items.

### Basic Implementation

```python
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an existing item."""
    if item_id < 0 or item_id >= len(items):
        return jsonify({'message': 'Item not found'}), 404
    
    item = request.json.get('item')
    items[item_id] = item
    return jsonify({'message': 'Item updated', 'item': item}), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an item."""
    if item_id < 0 or item_id >= len(items):
        return jsonify({'message': 'Item not found'}), 404
    
    removed_item = items.pop(item_id)
    return jsonify({'message': 'Item deleted', 'item': removed_item}), 200
```

### Enhanced Implementation

```python
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an existing item with error handling."""
    if item_id < 0 or item_id >= len(items):
        abort(404, description="Item not found.")
    
    if not request.json or 'item' not in request.json:
        abort(400, description="Invalid request: 'item' is required.")
    
    item = request.json['item']
    items[item_id] = item
    return jsonify({'message': 'Item updated', 'item': item}), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an item with error handling."""
    if item_id < 0 or item_id >= len(items):
        abort(404, description="Item not found.")
    
    removed_item = items.pop(item_id)
    return jsonify({'message': 'Item deleted', 'item': removed_item}), 200
```

### Testing the Solution

```python
# Test updating an item
response = requests.put('http://127.0.0.1:5000/items/0', json={'item': 'Updated Item'})
assert response.status_code == 200
assert response.json() == {'message': 'Item updated', 'item': 'Updated Item'}

# Test deleting an item
response = requests.delete('http://127.0.0.1:5000/items/0')
assert response.status_code == 200
assert response.json() == {'message': 'Item deleted', 'item': 'Updated Item'}

# Test error handling for update
response = requests.put('http://127.0.0.1:5000/items/999', json={'item': 'Non-existent Item'})
assert response.status_code == 404

# Test error handling for delete
response = requests.delete('http://127.0.0.1:5000/items/999')
assert response.status_code == 404
```

### Explanation

- **Key Concepts**: The `PUT` and `DELETE` methods allow updating and removing resources. We utilize the item ID to identify which item to modify or delete.
- **Error Handling**: Both methods check if the item ID is valid before proceeding and respond with appropriate status codes.
- **Complexity**: The time complexity for updating and deleting items is O(n) in the worst case due to the need to shift items in the list.

### Key Takeaways

- Implementing RESTful principles in APIs enhances usability and clarity.
- Proper error handling significantly improves the robustness of the API.
- Testing edge cases ensures that your API behaves as expected under various conditions.

---

This document provides a foundational understanding of building a Flask API, highlighting both basic and enhanced implementations while emphasizing best practices and testing strategies.