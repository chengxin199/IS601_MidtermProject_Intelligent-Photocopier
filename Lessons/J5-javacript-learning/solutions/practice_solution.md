---
title: Advance javascript - Practice Solution
layout: layouts/course.njk
courseId: J5-javacript-learning
permalink: /Lessons/J5-javacript-learning/practice-solution.html
tags:
  - solutions
  - code
date: 2025-12-08T17:57:52.302190
---
# Advanced JavaScript Practice Solutions

## Learning Objectives
- Master key concepts of advanced JavaScript
- Apply practical techniques in real-world scenarios
- Build real-world projects with robust error handling

---

## Exercise 1: Debounce Function

### Overview
A debounce function limits the rate at which a function can fire. This is especially useful when dealing with events like scrolling or resizing, where frequent calls can hurt performance.

### Basic Implementation
This is a simple debounce function that delays the execution of a function until after a specified wait time.

```javascript
/**
 * Debounce function that delays the execution of a function
 * until after wait milliseconds have passed since the last time
 * it was invoked.
 * 
 * @param {function} func - The function to debounce
 * @param {number} wait - The time to wait in milliseconds
 * @returns {function} A debounced version of the function
 */
function debounce(func, wait) {
    let timeout; // Variable to hold the timeout reference

    return function(...args) {
        const context = this; // Preserve the context of 'this'
        
        // Clear the previous timeout if it exists
        clearTimeout(timeout);

        // Set a new timeout
        timeout = setTimeout(() => {
            func.apply(context, args); // Call the function with the correct context and arguments
        }, wait);
    };
}

// Example usage
const log = () => console.log('Function executed!');
const debouncedLog = debounce(log, 2000);
window.addEventListener('resize', debouncedLog);
```

### Enhanced Implementation
The enhanced version includes error handling to ensure proper input types.

```javascript
function debounce(func, wait) {
    if (typeof func !== 'function') {
        throw new TypeError('First argument must be a function');
    }
    if (typeof wait !== 'number') {
        throw new TypeError('Second argument must be a number');
    }

    let timeout;

    return function(...args) {
        const context = this;
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            func.apply(context, args);
        }, wait);
    };
}
```

### Testing the Solution
We can use a simple test to verify our debounce function.

```javascript
// Test case for debounce function
const log = jest.fn(); // Mock function to track calls
const debouncedLog = debounce(log, 1000);

// Simulate rapid calls
debouncedLog();
debouncedLog();
debouncedLog();

// Wait for the debounce time
setTimeout(() => {
    expect(log).toHaveBeenCalledTimes(1); // Should only be called once
}, 1100);
```

### Explanation
- **Design Decisions**: The debounce function takes in a function and a wait time, ensuring that it only invokes the function after the specified time has passed without additional calls.
- **Error Handling**: The enhanced version checks for the correct types of arguments, throwing errors if the inputs are not as expected.
- **Complexity Analysis**: The time complexity is O(n) where n is the number of rapid calls made. The space complexity is O(1) since we only use a single timeout variable.

### Key Takeaways
- Debouncing is crucial for optimizing performance in event handling.
- Validating inputs is essential to prevent runtime errors.
- Using `setTimeout` allows us to control function execution timing effectively.

---

## Exercise 2: Throttle Function

### Overview
A throttle function ensures that a function is only executed at most once in a specified time interval. This is beneficial for events that can trigger rapidly, like scroll or resize events.

### Basic Implementation
A basic throttle function that restricts a function's execution frequency.

```javascript
/**
 * Throttle function that only allows a function to be called
 * at most once every wait milliseconds.
 * 
 * @param {function} func - The function to throttle
 * @param {number} wait - The time to wait in milliseconds
 * @returns {function} A throttled version of the function
 */
function throttle(func, wait) {
    let lastTime = 0; // Record the last time the function was invoked

    return function(...args) {
        const now = Date.now(); // Get the current time
        if (now - lastTime >= wait) {
            lastTime = now; // Update lastTime
            func.apply(this, args); // Call the function with correct context and arguments
        }
    };
}

// Example usage
const log = () => console.log('Throttled function executed!');
const throttledLog = throttle(log, 2000);
window.addEventListener('scroll', throttledLog);
```

### Enhanced Implementation
The enhanced version adds error handling for input validation.

```javascript
function throttle(func, wait) {
    if (typeof func !== 'function') {
        throw new TypeError('First argument must be a function');
    }
    if (typeof wait !== 'number') {
        throw new TypeError('Second argument must be a number');
    }

    let lastTime = 0;

    return function(...args) {
        const now = Date.now();
        if (now - lastTime >= wait) {
            lastTime = now;
            func.apply(this, args);
        }
    };
}
```

### Testing the Solution
We can test the throttle function using Jest.

```javascript
const log = jest.fn();
const throttledLog = throttle(log, 1000);

// Simulate rapid calls
throttledLog();
throttledLog();
throttledLog();

// Wait for the throttle time
setTimeout(() => {
    expect(log).toHaveBeenCalledTimes(1); // Should only be called once
}, 1100);
```

### Explanation
- **Design Decisions**: The throttle function maintains a timestamp of the last invocation and only allows execution if the specified time has passed.
- **Error Handling**: The function checks input types to ensure proper usage.
- **Complexity Analysis**: The time complexity is O(n) for n rapid calls, and the space complexity is O(1).

### Key Takeaways
- Throttling helps in improving performance by limiting function execution frequency.
- Proper input validation is necessary to prevent unexpected behavior or crashes.

---

## Conclusion

This document provides a comprehensive solution for advanced JavaScript concepts through practical exercises involving debounce and throttle functions. Each solution emphasizes clean code practices, error handling, and testing to ensure functionality and reliability.