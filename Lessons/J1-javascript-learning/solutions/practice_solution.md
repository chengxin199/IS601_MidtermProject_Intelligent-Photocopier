---
title: InTRODUCTION to javascript - Practice Solution
layout: layouts/course.njk
courseId: J1-javascript-learning
tags:
  - solutions
  - code
date: 2025-12-08T15:47:39.440188
---
# Introduction to JavaScript

This document serves as a comprehensive practice solution for the key concepts related to JavaScript. It is structured to guide learners through understanding basic and enhanced techniques while applying them to real-world scenarios. 

## Learning Objectives
- Master key concepts of JavaScript.
- Apply practical techniques in real-world projects.
- Build and test code effectively.

---

## Exercise 1: Simple Function to Calculate Factorial

### Overview
The factorial of a non-negative integer \( n \) is the product of all positive integers less than or equal to \( n \). This solution implements a function that calculates the factorial of a number both in a basic and an enhanced manner with error handling.

### Basic Implementation

```javascript
// Function to calculate the factorial of a number
function factorial(n) {
    // Initial result is 1 (0! = 1)
    let result = 1;
    
    // Loop from 1 to n to calculate the factorial
    for (let i = 1; i <= n; i++) {
        result *= i; // Multiply result by the current number
    }
    
    // Return the computed factorial
    return result;
}

// Example usage
console.log(factorial(5)); // Output: 120
```

### Enhanced Implementation

```javascript
// Function to calculate the factorial of a number with error handling
function factorial(n) {
    // Validate the input
    if (typeof n !== 'number' || n < 0 || !Number.isInteger(n)) {
        throw new Error('Input must be a non-negative integer.');
    }
    
    // Initial result is 1 (0! = 1)
    let result = 1;
    
    // Loop from 1 to n to calculate the factorial
    for (let i = 1; i <= n; i++) {
        result *= i; // Multiply result by the current number
    }
    
    // Return the computed factorial
    return result;
}

// Example usage with error handling
try {
    console.log(factorial(5)); // Output: 120
    console.log(factorial(-1)); // This will throw an error
} catch (error) {
    console.error(error.message); // Output: Input must be a non-negative integer.
}
```

### Testing the Solution

```javascript
// Test cases for the factorial function
function testFactorial() {
    console.assert(factorial(0) === 1, 'Test Case 1 Failed'); // 0! = 1
    console.assert(factorial(1) === 1, 'Test Case 2 Failed'); // 1! = 1
    console.assert(factorial(5) === 120, 'Test Case 3 Failed'); // 5! = 120
    console.assert(factorial(3) === 6, 'Test Case 4 Failed'); // 3! = 6
    console.assert(factorial(10) === 3628800, 'Test Case 5 Failed'); // 10! = 3628800

    try {
        factorial(-5); // Should throw an error
    } catch (e) {
        console.assert(e.message === 'Input must be a non-negative integer.', 'Test Case 6 Failed');
    }

    console.log('All test cases passed!');
}

// Run the tests
testFactorial();
```

### Explanation
- **Design Decisions**: The basic implementation uses a simple for-loop to compute the factorial, while the enhanced version includes input validation to ensure the function only processes non-negative integers.
- **Complexity Analysis**: Both implementations have a time complexity of O(n) due to the single loop iteration through the range of numbers. The space complexity is O(1) since only a single variable is used to store the result.
  
### Key Takeaways
- Always validate input data to avoid unexpected errors.
- Testing is crucial; ensure edge cases are handled effectively.
- Comment your code to improve readability and maintainability.

---

## Exercise 2: String Reversal Function

### Overview
This exercise demonstrates how to reverse a string using both a basic approach and an enhanced version with error handling.

### Basic Implementation

```javascript
// Function to reverse a string
function reverseString(str) {
    // Split the string into an array, reverse it, and then join back to string
    return str.split('').reverse().join('');
}

// Example usage
console.log(reverseString("Hello")); // Output: "olleH"
```

### Enhanced Implementation

```javascript
// Function to reverse a string with error handling
function reverseString(str) {
    // Validate the input
    if (typeof str !== 'string') {
        throw new Error('Input must be a string.');
    }
    
    // Split the string into an array, reverse it, and then join back to string
    return str.split('').reverse().join('');
}

// Example usage with error handling
try {
    console.log(reverseString("Hello")); // Output: "olleH"
    console.log(reverseString(123)); // This will throw an error
} catch (error) {
    console.error(error.message); // Output: Input must be a string.
}
```

### Testing the Solution

```javascript
// Test cases for the string reversal function
function testReverseString() {
    console.assert(reverseString("Hello") === "olleH", 'Test Case 1 Failed');
    console.assert(reverseString("JavaScript") === "tpircSavaJ", 'Test Case 2 Failed');
    console.assert(reverseString("") === "", 'Test Case 3 Failed'); // Edge case: empty string

    try {
        reverseString(123); // Should throw an error
    } catch (e) {
        console.assert(e.message === 'Input must be a string.', 'Test Case 4 Failed');
    }

    console.log('All test cases passed!');
}

// Run the tests
testReverseString();
```

### Explanation
- **Design Decisions**: The basic implementation utilizes JavaScript's built-in methods for string manipulation. The enhanced version checks for valid input types.
- **Complexity Analysis**: The time complexity is O(n) due to the string manipulation operations, and the space complexity is also O(n) because of the creation of an array during the split operation.

### Key Takeaways
- Ensure inputs are validated to prevent runtime errors.
- Utilize built-in functions effectively to simplify code.
- Include test cases for each function to verify correctness and robustness. 

---

This document serves as a foundational guide for mastering JavaScript concepts through practical exercises, emphasizing the importance of clean code, error handling, and testing.