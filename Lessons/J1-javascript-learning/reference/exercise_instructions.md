---
title: InTRODUCTION to javascript - Exercise Instructions
layout: layouts/course.njk
courseId: J1-javascript-learning
permalink: /Lessons/J1-javascript-learning/index.html
tags:
  - exercises
  - practice
date: 2025-12-08T17:17:35.592065
---
## Exercise 1: Basic Variables and Data Types
**Difficulty:** Beginner  
**Time Estimate:** 15 minutes

### Objective
Implement a small program that declares variables of different data types, performs some basic operations, and prints results to the console.

### Starter Code
```python
def basic_variables():
    # TODO: Declare variables of different data types
    integer_var = 0
    float_var = 0.0
    string_var = ""
    boolean_var = False
    
    # TODO: Perform some basic operations
    integer_var = 10
    float_var = 5.5
    string_var = "Hello, World!"
    boolean_var = True
    
    # TODO: Print results
    print("Integer:", integer_var)
    print("Float:", float_var)
    print("String:", string_var)
    print("Boolean:", boolean_var)

basic_variables()
```

### Requirements
- Create variables for an integer, float, string, and boolean.
- Perform at least one operation with each variable (e.g., addition for integers, concatenation for strings).
- Ensure each variable's value is printed correctly.

### Test Cases
```python
# Since this is a print function, we will not have assert statements.
# However, you can run the function and verify the output manually.
basic_variables()  # Expected output:
# Integer: 10
# Float: 5.5
# String: Hello, World!
# Boolean: True
```

### Hints
- Use the `print()` function to display output.
- Remember to initialize your variables before using them.

---

## Exercise 2: Conditional Statements
**Difficulty:** Intermediate  
**Time Estimate:** 20 minutes

### Objective
Create a function that checks if a given number is positive, negative, or zero and returns a corresponding message.

### Starter Code
```python
def check_number(num):
    # TODO: Implement conditional statements to check the number
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Test the function with different numbers
print(check_number(5))    # Expected output: Positive
print(check_number(-3))   # Expected output: Negative
print(check_number(0))    # Expected output: Zero
```

### Requirements
- Implement conditional statements to check if `num` is positive, negative, or zero.
- Return a string message based on the check.

### Test Cases
```python
assert check_number(2) == "Positive"
assert check_number(-1) == "Negative"
assert check_number(0) == "Zero"
```

### Hints
- Use `if`, `elif`, and `else` to handle your conditions.
- Make sure to test edge cases like zero.

---

## Exercise 3: Loops and Lists
**Difficulty:** Intermediate  
**Time Estimate:** 25 minutes

### Objective
Write a function that takes a list of numbers and returns a new list containing only the even numbers.

### Starter Code
```python
def filter_even_numbers(numbers):
    even_numbers = []  # TODO: Initialize an empty list for even numbers
    # TODO: Use a loop to iterate through the numbers
    for number in numbers:
        if number % 2 == 0:  # TODO: Check if the number is even
            even_numbers.append(number)  # TODO: Add even number to the list
    
    return even_numbers

# Test the function with a sample list
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Expected output: [2, 4, 6]
```

### Requirements
- Iterate through the given list of numbers.
- Use the modulo operator to check for even numbers.
- Return a new list containing only the even numbers.

### Test Cases
```python
assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
assert filter_even_numbers([10, 15, 20, 25]) == [10, 20]
assert filter_even_numbers([0, -2, -3]) == [0, -2]
```

### Hints
- Use the `append()` method to add items to a list.
- Remember to initialize your even number list before the loop.

---

## Exercise 4: Functions and Return Values
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Create a function that calculates the factorial of a number using recursion.

### Starter Code
```python
def factorial(n):
    # TODO: Implement the base case for recursion
    if n == 0 or n == 1:
        return 1
    # TODO: Implement the recursive case
    return n * factorial(n - 1)

# Test the function with different inputs
print(factorial(5))  # Expected output: 120
print(factorial(0))  # Expected output: 1
```

### Requirements
- Implement a recursive function to calculate the factorial.
- Handle the base case for when `n` is 0 or 1.

### Test Cases
```python
assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(3) == 6
```

### Hints
- The factorial of a number `n` is `n * factorial(n-1)`.
- Don't forget to define the base case to stop the recursion.

---

## Exercise 5: Basic Object-Oriented Programming
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Define a simple class `Dog` with attributes for `name` and `age`, and a method that returns a description of the dog.

### Starter Code
```python
class Dog:
    def __init__(self, name, age):
        # TODO: Initialize name and age attributes
        self.name = name
        self.age = age
    
    def description(self):
        # TODO: Return a string describing the dog
        return f"{self.name} is {self.age} years old."

# Create a Dog instance and print its description
my_dog = Dog("Buddy", 4)
print(my_dog.description())  # Expected output: Buddy is 4 years old.
```

### Requirements
- Create a class with an `__init__` method to initialize attributes.
- Include a method that returns a string with the dog's name and age.

### Test Cases
```python
dog1 = Dog("Rex", 5)
assert dog1.description() == "Rex is 5 years old."

dog2 = Dog("Luna", 3)
assert dog2.description() == "Luna is 3 years old."
```

### Hints
- Use `self` to refer to instance attributes inside class methods.
- Make sure to create the class correctly before instantiating it.