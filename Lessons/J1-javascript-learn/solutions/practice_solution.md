---
title: introduction to javascript - Practice Solution
layout: layouts/course.njk
courseId: J1-javascript-learn
tags:
  - solutions
  - code
date: 2025-12-04T15:55:32.558822
---
# Introduction to JavaScript: Comprehensive Practice Solutions

This document provides detailed practice solutions for core JavaScript concepts, demonstrating mastery of key ideas, application of practical techniques, and building real-world projects.

---

## Exercise 1: Create a Function to Reverse a String

### Overview

The goal is to implement a function that reverses a given string. This exercise reinforces understanding of strings, array methods, and function creation in JavaScript. The basic implementation uses simple built-in methods; the enhanced version adds input validation and error handling.

---

### Basic Implementation

```javascript
/**
 * Reverses the input string.
 * @param {string} str - The string to reverse.
 * @returns {string} - The reversed string.
 */
function reverseString(str) {
  // Convert string to array, reverse it, then join back to string
  return str.split('').reverse().join('');
}
```

---

### Enhanced Implementation

```javascript
/**
 * Reverses the input string with input validation.
 * @param {string} str - The string to reverse.
 * @returns {string} - The reversed string.
 * @throws {TypeError} - If input is not a string.
 */
function reverseString(str) {
  // Validate input type
  if (typeof str !== 'string') {
    throw new TypeError('Input must be a string');
  }
  // Reverse the string by splitting, reversing and joining
  return str.split('').reverse().join('');
}
```

---

### Testing the Solution

```javascript
// Testing helper function
function testReverseString() {
  const tests = [
    { input: 'hello', expected: 'olleh' },
    { input: 'JavaScript', expected: 'tpircSavaJ' },
    { input: '', expected: '' },
    { input: 'a', expected: 'a' },
    { input: '12345', expected: '54321' }
  ];

  tests.forEach(({ input, expected }, index) => {
    const result = reverseString(input);
    console.assert(result === expected, `Test ${index + 1} failed: expected "${expected}", got "${result}"`);
  });

  // Test error handling
  try {
    reverseString(12345);
    console.error('Error test failed: Did not throw error for non-string input');
  } catch (e) {
    console.assert(e instanceof TypeError, 'Error test failed: Incorrect error type');
  }

  console.log('All tests passed!');
}

testReverseString();
```

---

### Explanation

- **Design decisions:** Using `split('')`, `reverse()`, and `join('')` is the most straightforward method to reverse a string in JavaScript.
- **Key concepts:** String manipulation, array methods, type checking.
- **Complexity:** Time complexity is O(n), where n is the length of the string, due to splitting and reversing operations.

---

### Key Takeaways

- Always validate function inputs to prevent unexpected behavior.
- JavaScript strings can be manipulated as arrays for many operations.
- Clear error messages improve debugging and maintainability.
- Writing tests ensures your function behaves as expected for different inputs.

---

## Exercise 2: Implement a Simple To-Do List Application (Array Manipulation)

### Overview

This exercise demonstrates managing a list of tasks using arrays and objects in JavaScript. Users can add, remove, and list to-dos. The basic version covers adding and listing; the enhanced version adds removal and error handling.

---

### Basic Implementation

```javascript
/**
 * To-Do List manager with add and list functionality.
 */
function ToDoList() {
  this.tasks = [];
}

/**
 * Adds a new task to the list.
 * @param {string} task - Task description.
 */
ToDoList.prototype.addTask = function(task) {
  this.tasks.push(task);
};

/**
 * Lists all tasks.
 * @returns {string[]} - Array of tasks.
 */
ToDoList.prototype.listTasks = function() {
  return this.tasks;
};
```

---

### Enhanced Implementation

```javascript
/**
 * To-Do List manager with add, remove, and list functionality with validation.
 */
function ToDoList() {
  this.tasks = [];
}

/**
 * Adds a new task to the list.
 * @param {string} task - Task description.
 * @throws {TypeError} - If task is not a non-empty string.
 */
ToDoList.prototype.addTask = function(task) {
  if (typeof task !== 'string' || task.trim() === '') {
    throw new TypeError('Task must be a non-empty string');
  }
  this.tasks.push(task.trim());
};

/**
 * Removes a task by index.
 * @param {number} index - The index of the task to remove.
 * @throws {RangeError} - If index is out of bounds.
 * @throws {TypeError} - If index is not a number.
 */
ToDoList.prototype.removeTask = function(index) {
  if (typeof index !== 'number' || !Number.isInteger(index)) {
    throw new TypeError('Index must be an integer');
  }
  if (index < 0 || index >= this.tasks.length) {
    throw new RangeError('Index out of bounds');
  }
  this.tasks.splice(index, 1);
};

/**
 * Lists all tasks.
 * @returns {string[]} - Array of tasks.
 */
ToDoList.prototype.listTasks = function() {
  // Return a shallow copy to prevent external modification
  return [...this.tasks];
};
```

---

### Testing the Solution

```javascript
function testToDoList() {
  const todo = new ToDoList();

  // Test adding tasks
  todo.addTask('Buy groceries');
  todo.addTask('Pay bills');
  console.assert(todo.listTasks().length === 2, 'Should have 2 tasks');

  // Test trimming and validation
  try {
    todo.addTask('');
    console.error('Empty task test failed: Did not throw error');
  } catch (e) {
    console.assert(e instanceof TypeError, 'Empty task test failed: Wrong error type');
  }

  // Test removing tasks
  todo.removeTask(0);
  console.assert(todo.listTasks()[0] === 'Pay bills', 'First task should now be "Pay bills"');

  // Test removing invalid index
  try {
    todo.removeTask(10);
    console.error('Invalid index test failed: Did not throw error');
  } catch (e) {
    console.assert(e instanceof RangeError, 'Invalid index test failed: Wrong error type');
  }

  // Test removing non-integer index
  try {
    todo.removeTask('one');
    console.error('Non-integer index test failed: Did not throw error');
  } catch (e) {
    console.assert(e instanceof TypeError, 'Non-integer index test failed: Wrong error type');
  }

  console.log('All ToDoList tests passed!');
}

testToDoList();
```

---

### Explanation

- **Design decisions:** Used a constructor function with prototype methods to simulate classes (pre-ES6).
- **Key concepts:** Object-oriented programming, array manipulation, input validation.
- **Complexity:** Adding/removing tasks are O(1) and O(n) respectively (due to splice).

---

### Key Takeaways

- Use prototypes or ES6 classes for reusable object methods.
- Always validate inputs (type, content, range).
- Return copies of internal data structures to prevent external mutation.
- Test edge cases like invalid inputs and empty states.

---

## Exercise 3: Fetch Data from an API and Display Results (Asynchronous JavaScript)

### Overview

This exercise shows how to fetch data asynchronously using the Fetch API and display results. The basic implementation fetches and logs data; the enhanced version includes error handling and async/await syntax.

---

### Basic Implementation

```javascript
/**
 * Fetches JSON data from a given URL and logs it.
 * @param {string} url - The API endpoint.
 */
function fetchData(url) {
  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data);
    });
}
```

---

### Enhanced Implementation

```javascript
/**
 * Fetches JSON data asynchronously and handles errors.
 * @param {string} url - The API endpoint.
 * @returns {Promise<Object>} - The fetched JSON data.
 * @throws {Error} - If fetching or parsing fails.
 */
async function fetchData(url) {
  if (typeof url !== 'string' || url.trim() === '') {
    throw new TypeError('URL must be a non-empty string');
  }
  
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed to fetch data:', error);
    throw error;  // Rethrow so callers can handle if needed
  }
}
```

---

### Testing the Solution

```javascript
async function testFetchData() {
  const validUrl = 'https://jsonplaceholder.typicode.com/posts/1';
  const invalidUrl = 'https://jsonplaceholder.typicode.com/invalid-endpoint';

  try {
    const data = await fetchData(validUrl);
    console.assert(data.id === 1, 'Data ID should be 1');
  } catch (e) {
    console.error('Valid URL test failed:', e);
  }

  try {
    await fetchData(invalidUrl);
    console.error('Invalid URL test failed: Did not throw error');
  } catch (e) {
    console.assert(e instanceof Error, 'Invalid URL test failed: Wrong error type');
  }

  try {
    await fetchData('');
    console.error('Empty URL test failed: Did not throw error');
  } catch (e) {
    console.assert(e instanceof TypeError, 'Empty URL test failed: Wrong error type');
  }

  console.log('All fetchData tests passed!');
}

testFetchData();
```

---

### Explanation

- **Design decisions:** Used `async/await` for cleaner asynchronous code.
- **Key concepts:** Promises, async/await, Fetch API, error handling.
- **Complexity:** Network-bound, time depends on response.

---

### Key Takeaways

- Use async/await for readable asynchronous code.
- Always check HTTP response status before processing.
- Validate inputs to avoid runtime errors.
- Catch and handle errors to improve user experience.

---

# Summary

This document presented production-quality JavaScript solutions covering string manipulation, object-oriented programming with arrays, and asynchronous API calls. Each solution includes basic and enhanced versions with proper error handling and comprehensive tests demonstrating best practices for intermediate JavaScript developers.