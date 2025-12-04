---
title: introduction to javascript - Exercise Instructions
layout: layouts/course.njk
courseId: J1-javascript-learn
tags:
  - exercises
  - practice
date: 2025-12-04T15:54:55.215654
---
## Exercise 1: Basic Calculator Functions  
**Difficulty:** Beginner  
**Time Estimate:** 15 minutes  

### Objective  
Implement simple JavaScript functions for addition, subtraction, multiplication, and division. Learn function syntax, parameters, and return values.

### Starter Code  
```python
# TODO: Implement JavaScript functions as strings

add_function = """
function add(a, b) {
    // TODO: return the sum of a and b
}
"""

subtract_function = """
function subtract(a, b) {
    // TODO: return the difference (a - b)
}
"""

multiply_function = """
function multiply(a, b) {
    // TODO: return the product of a and b
}
"""

divide_function = """
function divide(a, b) {
    // TODO: return the quotient (a / b)
    // Handle division by zero by returning null
}
"""
```

### Requirements  
- Each function takes two numeric parameters and returns their calculated value.  
- The divide function must return `null` if dividing by zero.  
- Assume inputs are always numbers (no type checking needed).  

### Test Cases  
```python
assert "return a + b" in add_function
assert "return a - b" in subtract_function
assert "return a * b" in multiply_function
assert "return null" in divide_function  # division by zero check
```

### Hints  
- Use the `return` statement in each function.  
- Check if `b === 0` in divide function before dividing.  
- Remember JavaScript uses `===` for strict equality.


## Exercise 2: String Manipulation Utility  
**Difficulty:** Intermediate  
**Time Estimate:** 25 minutes  

### Objective  
Create a JavaScript function that takes a string and returns the string reversed and in uppercase. Practice string methods and chaining.

### Starter Code  
```python
reverse_uppercase_function = """
function reverseUppercase(str) {
    // TODO: Reverse the string and convert to uppercase
    // Example: "hello" -> "OLLEH"
}
"""
```

### Requirements  
- Input is a non-empty string.  
- Output is the string reversed and fully uppercase.  
- Use built-in string and array methods.  

### Test Cases  
```python
assert '"OLLEH"' in reverse_uppercase_function
assert '"DLROW"' in reverse_uppercase_function
```

### Hints  
- Strings can be split into arrays using `.split('')`.  
- Use `.reverse()` array method and then `.join('')` to convert back.  
- Use `.toUpperCase()` to change case.


## Exercise 3: Simple To-Do List Object  
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes  

### Objective  
Build a JavaScript object representing a to-do list with methods to add, remove, and list tasks. Understand objects, arrays, and method declarations.

### Starter Code  
```python
todo_list_code = """
const todoList = {
    tasks: [],
    
    addTask: function(task) {
        // TODO: Add task string to tasks array
    },
    
    removeTask: function(task) {
        // TODO: Remove task string from tasks array if it exists
    },
    
    listTasks: function() {
        // TODO: Return a copy of the tasks array
    }
};
"""
```

### Requirements  
- `addTask` appends a task string to `tasks`.  
- `removeTask` deletes the first matching task; do nothing if not found.  
- `listTasks` returns a new array with current tasks (not a reference).  
- Tasks are simple strings.  

### Test Cases  
```python
assert "this.tasks.push(task)" in todo_list_code
assert "this.tasks.indexOf(task)" in todo_list_code
assert "this.tasks.slice()" in todo_list_code or "this.tasks.concat()" in todo_list_code
```

### Hints  
- Use `.push()` to add items to an array.  
- Use `.indexOf()` and `.splice()` to remove an item.  
- Return a copy using `.slice()` or `.concat()` to avoid exposing internal array.


## Exercise 4: Event Listener and DOM Manipulation  
**Difficulty:** Intermediate  
**Time Estimate:** 40 minutes  

### Objective  
Write JavaScript code that adds a click event listener to a button. When clicked, it changes the text content of a paragraph element. Practice DOM selection and event handling.

### Starter Code  
```python
dom_event_code = """
// TODO: Select button with id "myButton"
// TODO: Select paragraph with id "myParagraph"

// TODO: Add click event listener to the button
// When clicked, change paragraph text to "Button Clicked!"
"""
```

### Requirements  
- Use `document.getElementById()` to select elements.  
- Use `.addEventListener()` to attach the click event.  
- Change paragraph `.textContent` when button is clicked.  

### Test Cases  
```python
assert "getElementById('myButton')" in dom_event_code
assert "getElementById('myParagraph')" in dom_event_code
assert ".addEventListener('click'" in dom_event_code
assert "textContent = 'Button Clicked!'" in dom_event_code
```

### Hints  
- Make sure to select elements before adding events.  
- The event listener callback is a function with no parameters (or event parameter if needed).  
- Changing `.textContent` updates visible text.


## Exercise 5: Fetch API and Async/Await  
**Difficulty:** Advanced  
**Time Estimate:** 50 minutes  

### Objective  
Create an async JavaScript function that fetches JSON data from a public API and logs the result. Practice promises, async/await, and error handling.

### Starter Code  
```python
fetch_data_function = """
async function fetchData(url) {
    try {
        // TODO: Fetch data from the URL
        // TODO: Parse response as JSON
        // TODO: Return the JSON data
    } catch (error) {
        // TODO: Log error message
        // TODO: Return null on failure
    }
}
"""
```

### Requirements  
- Use `fetch()` API to get data from `url`.  
- Use `await` to wait for response and JSON parsing.  
- Use try/catch to handle network or parsing errors.  
- Log errors with `console.error()`.  
- Return JSON data on success, `null` on failure.  

### Test Cases  
```python
assert "await fetch(url)" in fetch_data_function
assert "await response.json()" in fetch_data_function
assert "console.error" in fetch_data_function
assert "return null" in fetch_data_function
```

### Hints  
- Remember to check if response.ok before parsing JSON.  
- Use `throw new Error()` to trigger catch on bad responses if desired.  
- Async functions always return a promise.  

---

These exercises build foundational JavaScript skills incrementally and include practical, real-world tasks. They use Python strings to represent JavaScript starter code for teaching purposes.