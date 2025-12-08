---
title: Introduction to javascript - Practice Solution
layout: layouts/course.njk
courseId: J2-javascript-learning
permalink: /Lessons/J2-javascript-learning/index.html
tags:
  - solutions
  - code
date: 2025-12-08T17:28:05.529264
---
# Introduction to JavaScript Practice Solutions

This document provides a comprehensive guide to mastering JavaScript through practical exercises. Each exercise demonstrates key concepts, practical techniques, and culminates in building real-world projects. The document is structured to help learners progressively enhance their skills.

## Exercise 1: Basic Calculator

### Overview
We will create a simple calculator that can perform basic arithmetic operations: addition, subtraction, multiplication, and division.

### Basic Implementation
```javascript
// Basic Calculator Implementation
function calculator(num1, num2, operation) {
    // Perform the requested arithmetic operation based on the value of 'operation'
    switch (operation) {
        case 'add':
            return num1 + num2; // Addition
        case 'subtract':
            return num1 - num2; // Subtraction
        case 'multiply':
            return num1 * num2; // Multiplication
        case 'divide':
            return num1 / num2; // Division
        default:
            return 'Invalid operation'; // Error for unsupported operation
    }
}

// Example usage
console.log(calculator(5, 3, 'add')); // Outputs: 8
```

### Enhanced Implementation
```javascript
// Enhanced Calculator Implementation with Error Handling
function enhancedCalculator(num1, num2, operation) {
    // Validate input types
    if (typeof num1 !== 'number' || typeof num2 !== 'number') {
        throw new Error('Both num1 and num2 must be numbers.');
    }
    
    // Perform the requested operation
    switch (operation) {
        case 'add':
            return num1 + num2;
        case 'subtract':
            return num1 - num2;
        case 'multiply':
            return num1 * num2;
        case 'divide':
            if (num2 === 0) {
                throw new Error('Division by zero is not allowed.'); // Prevent division by zero
            }
            return num1 / num2;
        default:
            throw new Error('Invalid operation. Supported operations: add, subtract, multiply, divide.');
    }
}

// Example usage with error handling
try {
    console.log(enhancedCalculator(10, 5, 'divide')); // Outputs: 2
    console.log(enhancedCalculator(10, 0, 'divide')); // Throws error
} catch (error) {
    console.error(error.message); // Output error message
}
```

### Testing the Solution
```javascript
// Test cases for the enhanced calculator function
function testEnhancedCalculator() {
    console.assert(enhancedCalculator(5, 3, 'add') === 8, 'Test Case 1 Failed');
    console.assert(enhancedCalculator(5, 3, 'subtract') === 2, 'Test Case 2 Failed');
    console.assert(enhancedCalculator(5, 3, 'multiply') === 15, 'Test Case 3 Failed');
    console.assert(enhancedCalculator(6, 3, 'divide') === 2, 'Test Case 4 Failed');
    
    try {
        enhancedCalculator(5, 0, 'divide');
    } catch (error) {
        console.assert(error.message === 'Division by zero is not allowed.', 'Test Case 5 Failed');
    }
    
    try {
        enhancedCalculator(5, 3, 'modulus');
    } catch (error) {
        console.assert(error.message === 'Invalid operation. Supported operations: add, subtract, multiply, divide.', 'Test Case 6 Failed');
    }
    
    console.log('All test cases passed!');
}

// Run the tests
testEnhancedCalculator();
```

### Explanation
- **Design Decisions**: The basic implementation uses a switch statement for clarity. The enhanced version adds input validation to ensure robustness.
- **Key Concepts**: Understanding of functions, switch-case statements, error handling with try-catch, and assertions for testing.
- **Complexity Analysis**: Both implementations have a time complexity of O(1), as they only perform a constant amount of work regardless of input size.

### Key Takeaways
- Always validate inputs to avoid runtime errors.
- Use descriptive error messages to assist debugging.
- Employ testing to ensure code reliability and correctness.

---

This Markdown document provides a structured approach to learning JavaScript, focusing on both basic and enhanced solutions for real-world applications. Each section is designed to help learners understand critical concepts and best practices.