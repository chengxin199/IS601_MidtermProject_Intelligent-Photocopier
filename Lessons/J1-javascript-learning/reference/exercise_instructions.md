---
title: InTRODUCTION to javascript - Exercise Instructions
layout: layouts/course.njk
courseId: J1-javascript-learning
tags:
  - exercises
  - practice
date: 2025-12-08T15:47:09.685962
---
## Exercise 1: Variables and Data Types
**Difficulty:** Beginner  
**Time Estimate:** 15 minutes

### Objective
Implement a simple program that demonstrates the creation and manipulation of different data types in JavaScript, such as strings, numbers, and booleans.

### Starter Code
```javascript
function variableTypes() {
    // TODO: Declare variables of different types
    let name; // String
    let age; // Number
    let isStudent; // Boolean

    // TODO: Assign values to the variables
    name = "Alice";
    age = 25;
    isStudent = true;

    // TODO: Return a formatted string with the variable values
    return `Name: ${name}, Age: ${age}, Is Student: ${isStudent}`;
}
```

### Requirements
- Declare a variable for a name (string), age (number), and student status (boolean).
- Assign appropriate values to those variables.
- Return a string that includes all the variable values in a readable format.

### Test Cases
```javascript
console.assert(variableTypes() === "Name: Alice, Age: 25, Is Student: true", "Test Case 1 Failed");
```

### Hints
- Use backticks (`` ` ``) for template literals to easily include variables in strings.
- Make sure to use the correct data types when assigning values.

---

## Exercise 2: Conditional Statements
**Difficulty:** Intermediate  
**Time Estimate:** 20 minutes

### Objective
Create a function that checks a user's age and returns whether they are a child, teenager, or adult.

### Starter Code
```javascript
function checkAge(age) {
    // TODO: Implement age checking logic
    if (age < 13) {
        return "Child";
    } else if (age >= 13 && age < 20) {
        return "Teenager";
    } else {
        return "Adult";
    }
}
```

### Requirements
- Check if the age is less than 13, between 13 and 19, or 20 and above.
- Return the corresponding category as a string.

### Test Cases
```javascript
console.assert(checkAge(10) === "Child", "Test Case 1 Failed");
console.assert(checkAge(15) === "Teenager", "Test Case 2 Failed");
console.assert(checkAge(25) === "Adult", "Test Case 3 Failed");
```

### Hints
- Remember to use comparison operators correctly.
- Consider edge cases, such as exactly 13 or 20 years old.

---

## Exercise 3: Loops and Arrays
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Write a function that takes an array of numbers and returns the sum of all the even numbers in the array.

### Starter Code
```javascript
function sumEvenNumbers(numbers) {
    // TODO: Initialize a sum variable
    let sum = 0;

    // TODO: Loop through the array of numbers
    for (let i = 0; i < numbers.length; i++) {
        // TODO: Check if the number is even
        if (numbers[i] % 2 === 0) {
            sum += numbers[i]; // Add to sum if even
        }
    }

    // TODO: Return the total sum
    return sum;
}
```

### Requirements
- Loop through the given array and identify even numbers using the modulus operator.
- Accumulate the sum of the even numbers and return it.

### Test Cases
```javascript
console.assert(sumEvenNumbers([1, 2, 3, 4, 5]) === 6, "Test Case 1 Failed");
console.assert(sumEvenNumbers([10, 15, 20, 25]) === 30, "Test Case 2 Failed");
console.assert(sumEvenNumbers([1, 3, 5]) === 0, "Test Case 3 Failed");
```

### Hints
- Use the modulus operator `%` to check for even numbers.
- Make sure to initialize your sum variable before the loop starts.

---

## Exercise 4: Functions and Scope
**Difficulty:** Intermediate  
**Time Estimate:** 25 minutes

### Objective
Create a function that accepts a string and returns the number of vowels in that string. 

### Starter Code
```javascript
function countVowels(str) {
    // TODO: Define a variable to count vowels
    let count = 0;
    const vowels = "aeiouAEIOU"; // List of vowels

    // TODO: Loop through each character in the string
    for (let i = 0; i < str.length; i++) {
        // TODO: Check if the character is a vowel
        if (vowels.includes(str[i])) {
            count++; // Increment count if a vowel is found
        }
    }

    // TODO: Return the total count of vowels
    return count;
}
```

### Requirements
- Loop through each character in the string.
- Use a method to check if the character is in the list of vowels and count how many vowels exist.

### Test Cases
```javascript
console.assert(countVowels("hello") === 2, "Test Case 1 Failed");
console.assert(countVowels("Education") === 5, "Test Case 2 Failed");
console.assert(countVowels("rhythm") === 0, "Test Case 3 Failed");
```

### Hints
- Consider using the `includes` method to check for vowels.
- Remember that the function should be case insensitive.

---

## Exercise 5: Objects and JSON
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Create a function that takes an object representing a person and returns a string that describes the person.

### Starter Code
```javascript
function describePerson(person) {
    // TODO: Use object properties to create a description
    return `${person.name} is ${person.age} years old and lives in ${person.city}.`;
}

// Example person object
const person = {
    name: "John",
    age: 30,
    city: "New York"
};
```

### Requirements
- Access and use the properties of the person object to build the description.
- The function should be able to handle different person objects.

### Test Cases
```javascript
console.assert(describePerson({ name: "John", age: 30, city: "New York" }) === "John is 30 years old and lives in New York.", "Test Case 1 Failed");
console.assert(describePerson({ name: "Alice", age: 25, city: "Los Angeles" }) === "Alice is 25 years old and lives in Los Angeles.", "Test Case 2 Failed");
```

### Hints
- Use dot notation to access object properties.
- Make sure to format your string properly for readability.

These exercises will help students progressively build their JavaScript skills while applying practical techniques to real-world scenarios.