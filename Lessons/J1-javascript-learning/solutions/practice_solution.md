---
title: InTRODUCTION to javascript - Practice Solution
layout: layouts/course.njk
courseId: J1-javascript-learning
permalink: /Lessons/J1-javascript-learning/index.html
tags:
  - solutions
  - code
date: 2025-12-08T17:18:00.458986
---
```markdown
# InTRODUCTION to JavaScript

## Learning Objectives
- Master key concepts
- Apply practical techniques
- Build real-world projects

---

## Exercise 1: Create a Simple Calculator

### Overview
In this exercise, we will create a simple calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division. We will implement both a basic version and an enhanced version that includes error handling for invalid inputs.

### Basic Implementation

```javascript
// Basic Calculator Implementation
function calculator(a, b, operation) {
    // Check the operation type and perform the corresponding calculation
    switch (operation) {
        case 'add':
            return a + b;
        case 'subtract':
            return a - b;
        case 'multiply':
            return a * b;
        case 'divide':
            return a / b; // Note: No error handling for division by zero
        default:
            return 'Invalid operation'; // Fallback for unknown operations
    }
}

// Example usage
console.log(calculator(5, 3, 'add'));      // Output: 8
console.log(calculator(5, 3, 'subtract')); // Output: 2
console.log(calculator(5, 3, 'multiply')); // Output: 15
console.log(calculator(5, 0, 'divide'));   // Output: Infinity
console.log(calculator(5, 3, 'modulus'));  // Output: Invalid operation
```

### Enhanced Implementation

```javascript
// Enhanced Calculator Implementation with Error Handling
function enhancedCalculator(a, b, operation) {
    // Validate inputs
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new Error('Both a and b must be numbers.');
    }
    if (!['add', 'subtract', 'multiply', 'divide'].includes(operation)) {
        throw new Error('Invalid operation. Choose from add, subtract, multiply, or divide.');
    }

    // Perform calculation with proper error handling for division by zero
    switch (operation) {
        case 'add':
            return a + b;
        case 'subtract':
            return a - b;
        case 'multiply':
            return a * b;
        case 'divide':
            if (b === 0) {
                throw new Error('Division by zero is not allowed.');
            }
            return a / b;
        default:
            return 'Invalid operation'; // Fallback for unknown operations
    }
}

// Example usage with error handling
try {
    console.log(enhancedCalculator(5, 3, 'add'));      // Output: 8
    console.log(enhancedCalculator(5, 3, 'subtract')); // Output: 2
    console.log(enhancedCalculator(5, 3, 'multiply')); // Output: 15
    console.log(enhancedCalculator(5, 0, 'divide'));   // Throws error
} catch (error) {
    console.error(error.message); // Output: Division by zero is not allowed.
}
```

### Testing the Solution

```javascript
// Testing the Enhanced Calculator
function testEnhancedCalculator() {
    console.assert(enhancedCalculator(5, 3, 'add') === 8, 'Test Case 1 Failed');
    console.assert(enhancedCalculator(5, 3, 'subtract') === 2, 'Test Case 2 Failed');
    console.assert(enhancedCalculator(5, 3, 'multiply') === 15, 'Test Case 3 Failed');
    console.assert(enhancedCalculator(5, 2, 'divide') === 2.5, 'Test Case 4 Failed');

    try {
        enhancedCalculator(5, 0, 'divide');
        console.error('Test Case 5 Failed: Expected error for division by zero');
    } catch (error) {
        console.assert(error.message === 'Division by zero is not allowed.', 'Test Case 5 Passed');
    }

    try {
        enhancedCalculator(5, 'a', 'add');
        console.error('Test Case 6 Failed: Expected error for invalid input');
    } catch (error) {
        console.assert(error.message === 'Both a and b must be numbers.', 'Test Case 6 Passed');
    }

    console.log('All test cases completed.');
}

testEnhancedCalculator();
```

### Explanation
- **Design Decisions**: The basic implementation uses a `switch` statement to determine the operation based on the input. The enhanced version adds input validation to ensure both operands are numbers and the operation is valid.
- **Key Concepts**: The solution demonstrates the use of functions, switch statements, and error handling in JavaScript.
- **Complexity Analysis**: Time complexity is O(1) as each operation is performed in constant time; however, input validation adds a minimal overhead.

### Key Takeaways
1. Always validate inputs to prevent runtime errors.
2. Use clear error messages to help users understand what went wrong.
3. Write tests to ensure your functions behave as expected.
4. Consider edge cases (like division by zero) in your implementations.
5. Document your code to clarify logic and usage for future developers.
```