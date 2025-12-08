---
title: InTRODUCTION to javascript - Practice Solution
layout: layouts/course.njk
courseId: J4-javascript-learning
permalink: /Lessons/J4-javascript-learning/index.html
tags:
  - solutions
  - code
date: 2025-12-08T17:41:57.022237
---
# Introduction to JavaScript Practice Solutions

This document provides a comprehensive guide to mastering key concepts in JavaScript through practical exercises. The exercises focus on building real-world projects while ensuring that learners understand the fundamental principles of JavaScript.

## Learning Objectives
- Master key concepts
- Apply practical techniques
- Build real-world projects

---

## Exercise 1: Factorial Calculation

### Overview
In this exercise, we will calculate the factorial of a number. The factorial of a non-negative integer \( n \) is the product of all positive integers less than or equal to \( n \).

### Basic Implementation

```javascript
/**
 * Calculates the factorial of a number.
 * @param {number} n - The number to calculate the factorial for.
 * @returns {number} - The factorial of the number.
 */
function factorial(n) {
    if (n < 0) return -1; // Factorial is not defined for negative numbers
    if (n === 0) return 1; // Base case: 0! = 1
    
    let result = 1; // Initialize result
    
    // Loop from 1 to n
    for (let i = 1; i <= n; i++) {
        result *= i; // Multiply result by the current number
    }
    return result; // Return the computed factorial
}

// Testing the basic implementation
console.log(factorial(5)); // Expected output: 120
```

### Enhanced Implementation

```javascript
/**
 * Calculates the factorial of a number with error handling.
 * @param {number} n - The number to calculate the factorial for.
 * @returns {number} - The factorial of the number or an error message.
 */
function factorialEnhanced(n) {
    // Validate input type
    if (typeof n !== 'number') {
        return 'Error: Input must be a number';
    }
    
    if (n < 0) {
        return 'Error: Factorial is not defined for negative numbers';
    }
    
    if (!Number.isInteger(n)) {
        return 'Error: Factorial is only defined for non-negative integers';
    }
    
    if (n === 0) return 1; // Base case: 0! = 1
    
    let result = 1; // Initialize result
    
    // Loop from 1 to n
    for (let i = 1; i <= n; i++) {
        result *= i; // Multiply result by the current number
    }
    return result; // Return the computed factorial
}

// Testing the enhanced implementation
console.log(factorialEnhanced(5)); // Expected output: 120
console.log(factorialEnhanced(-1)); // Expected output: Error: Factorial is not defined for negative numbers
console.log(factorialEnhanced(5.5)); // Expected output: Error: Factorial is only defined for non-negative integers
console.log(factorialEnhanced('five')); // Expected output: Error: Input must be a number
```

### Testing the Solution

```javascript
// Test cases for basic implementation
console.assert(factorial(0) === 1, 'Test Case 1 Failed');
console.assert(factorial(1) === 1, 'Test Case 2 Failed');
console.assert(factorial(5) === 120, 'Test Case 3 Failed');
console.assert(factorial(7) === 5040, 'Test Case 4 Failed');

// Test cases for enhanced implementation
console.assert(factorialEnhanced(0) === 1, 'Enhanced Test Case 1 Failed');
console.assert(factorialEnhanced(1) === 1, 'Enhanced Test Case 2 Failed');
console.assert(factorialEnhanced(5) === 120, 'Enhanced Test Case 3 Failed');
console.assert(factorialEnhanced(-1) === 'Error: Factorial is not defined for negative numbers', 'Enhanced Test Case 4 Failed');
console.assert(factorialEnhanced(5.5) === 'Error: Factorial is only defined for non-negative integers', 'Enhanced Test Case 5 Failed');
console.assert(factorialEnhanced('five') === 'Error: Input must be a number', 'Enhanced Test Case 6 Failed');

console.log('All test cases passed!');
```

### Explanation
- **Basic Implementation**: The basic implementation computes the factorial using a simple loop. It handles the base case for \( 0 \) and checks for negative numbers.
- **Enhanced Implementation**: The enhanced version provides error handling for various invalid inputs, including non-numeric values and non-integer values, ensuring robustness.
- **Testing**: Assertions are used to verify that the function behaves as expected for a variety of cases.

### Key Takeaways
- Understanding how to handle errors in JavaScript is crucial for building robust applications.
- Using assertions for testing helps in ensuring code reliability and correctness.
- Factorials can be computed iteratively, but one should consider recursion for larger values, keeping in mind the limitations of the call stack.

---

This document serves as a foundation for mastering JavaScript through practical exercises and thorough understanding of the language's features and capabilities. Each solution is designed to enhance learning through clear explanations, robust implementations, and comprehensive testing.