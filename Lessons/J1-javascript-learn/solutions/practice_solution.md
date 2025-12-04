---
title: introduction to javascript - Practice Solution
layout: layouts/course.njk
courseId: J1-javascript-learn
tags:
  - solutions
  - code
date: 2025-12-04T23:58:39.348994
---
# Introduction to JavaScript Practice Solutions

This document provides a comprehensive guide to mastering key JavaScript concepts through practical exercises. Each exercise is structured to enhance your understanding and application of JavaScript in real-world scenarios.

## Learning Objectives
- Master key concepts
- Apply practical techniques
- Build real-world projects

---

## Exercise 1: Basic Calculator

### Overview
In this exercise, we will create a basic calculator that performs addition, subtraction, multiplication, and division. We will first implement a simple version and then enhance it with error handling to make it more robust.

### Basic Implementation

```javascript
// Basic Calculator Implementation

function basicCalculator(num1, num2, operation) {
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
            return 'Invalid operation'; // Error for unknown operation
    }
}

// Testing the basic calculator
console.log(basicCalculator(5, 3, 'add'));      // Outputs: 8
console.log(basicCalculator(5, 3, 'subtract')); // Outputs: 2
console.log(basicCalculator(5, 3, 'multiply')); // Outputs: 15
console.log(basicCalculator(5, 3, 'divide'));   // Outputs: 1.6666666666666667
console.log(basicCalculator(5, 3, 'modulus'));   // Outputs: 'Invalid operation'
```

### Enhanced Implementation

```javascript
// Enhanced Calculator Implementation with Error Handling

function enhancedCalculator(num1, num2, operation) {
    // Validate input types
    if (typeof num1 !== 'number' || typeof num2 !== 'number') {
        return 'Error: Both inputs must be numbers';
    }

    switch (operation) {
        case 'add':
            return num1 + num2;
        case 'subtract':
            return num1 - num2;
        case 'multiply':
            return num1 * num2;
        case 'divide':
            if (num2 === 0) {
                return 'Error: Cannot divide by zero'; // Prevent division by zero
            }
            return num1 / num2;
        default:
            return 'Error: Invalid operation'; // Error for unknown operation
    }
}

// Testing the enhanced calculator
console.log(enhancedCalculator(5, 3, 'add'));      // Outputs: 8
console.log(enhancedCalculator(5, 3, 'subtract')); // Outputs: 2
console.log(enhancedCalculator(5, 3, 'multiply')); // Outputs: 15
console.log(enhancedCalculator(5, 3, 'divide'));   // Outputs: 1.6666666666666667
console.log(enhancedCalculator(5, 0, 'divide'));   // Outputs: 'Error: Cannot divide by zero'
console.log(enhancedCalculator(5, '3', 'add'));    // Outputs: 'Error: Both inputs must be numbers'
console.log(enhancedCalculator(5, 3, 'modulus'));   // Outputs: 'Error: Invalid operation'
```

### Testing the Solution

```javascript
// Testing Suite
function runTests() {
    console.assert(enhancedCalculator(5, 3, 'add') === 8, 'Test Case 1 Failed');
    console.assert(enhancedCalculator(5, 3, 'subtract') === 2, 'Test Case 2 Failed');
    console.assert(enhancedCalculator(5, 3, 'multiply') === 15, 'Test Case 3 Failed');
    console.assert(enhancedCalculator(5, 3, 'divide') === 1.6666666666666667, 'Test Case 4 Failed');
    console.assert(enhancedCalculator(5, 0, 'divide') === 'Error: Cannot divide by zero', 'Test Case 5 Failed');
    console.assert(enhancedCalculator(5, '3', 'add') === 'Error: Both inputs must be numbers', 'Test Case 6 Failed');
    console.assert(enhancedCalculator(5, 3, 'modulus') === 'Error: Invalid operation', 'Test Case 7 Failed');
    console.log('All test cases passed!');
}

runTests();
```

### Explanation
- **Design Decisions**: The basic calculator uses a switch statement to determine the operation to perform. The enhanced version adds input validation to ensure that the inputs are numbers and handles specific errors such as division by zero.
- **Key Concepts**: This exercise demonstrates the use of functions, conditionals, and error handling in JavaScript.
- **Complexity Analysis**: The time complexity of both implementations is O(1) since the operations do not depend on the size of the input.

### Key Takeaways
- Always validate inputs to ensure your function operates correctly.
- Use meaningful error messages to improve the usability of your functions.
- Testing is crucial to ensure your functions behave as expected.

---

## Exercise 2: FizzBuzz

### Overview
The FizzBuzz problem is a common coding exercise that requires printing numbers from 1 to a given limit, replacing multiples of three with "Fizz", multiples of five with "Buzz", and multiples of both with "FizzBuzz".

### Basic Implementation

```javascript
// Basic FizzBuzz Implementation

function fizzBuzz(limit) {
    let result = [];
    for (let i = 1; i <= limit; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            result.push('FizzBuzz'); // Multiple of both 3 and 5
        } else if (i % 3 === 0) {
            result.push('Fizz'); // Multiple of 3
        } else if (i % 5 === 0) {
            result.push('Buzz'); // Multiple of 5
        } else {
            result.push(i); // Number itself
        }
    }
    return result;
}

// Testing the basic FizzBuzz
console.log(fizzBuzz(15)); // Outputs: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
```

### Enhanced Implementation

```javascript
// Enhanced FizzBuzz Implementation with Input Validation

function enhancedFizzBuzz(limit) {
    // Validate input type
    if (typeof limit !== 'number' || limit <= 0) {
        return 'Error: Limit must be a positive number';
    }

    let result = [];
    for (let i = 1; i <= limit; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            result.push('FizzBuzz');
        } else if (i % 3 === 0) {
            result.push('Fizz');
        } else if (i % 5 === 0) {
            result.push('Buzz');
        } else {
            result.push(i);
        }
    }
    return result;
}

// Testing the enhanced FizzBuzz
console.log(enhancedFizzBuzz(15)); // Outputs: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
console.log(enhancedFizzBuzz(-5)); // Outputs: 'Error: Limit must be a positive number'
console.log(enhancedFizzBuzz('ten')); // Outputs: 'Error: Limit must be a positive number'
```

### Testing the Solution

```javascript
// Testing Suite for FizzBuzz
function runFizzBuzzTests() {
    console.assert(JSON.stringify(enhancedFizzBuzz(15)) === JSON.stringify([1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']), 'Test Case 1 Failed');
    console.assert(enhancedFizzBuzz(-5) === 'Error: Limit must be a positive number', 'Test Case 2 Failed');
    console.assert(enhancedFizzBuzz('ten') === 'Error: Limit must be a positive number', 'Test Case 3 Failed');
    console.log('All FizzBuzz test cases passed!');
}

runFizzBuzzTests();
```

### Explanation
- **Design Decisions**: The basic implementation uses a simple loop and conditionals. The enhanced version adds input validation to ensure the limit is a positive number.
- **Key Concepts**: This exercise illustrates loops, conditionals, and array manipulation in JavaScript.
- **Complexity Analysis**: The time complexity is O(n) where n is the limit, as we iterate through numbers from 1 to the limit.

### Key Takeaways
- Input validation is crucial for preventing runtime errors.
- Using arrays to store results can be useful for later processing or output.
- Always ensure your function has a clear return type and handles unexpected inputs gracefully.

---

This document provides a structured approach to mastering JavaScript through practical exercises. Each exercise illustrates key concepts while promoting best practices in coding and error handling.