---
title: introduction to javascript - Exercise Instructions
layout: layouts/course.njk
courseId: J1-javascript-learn
tags:
  - exercises
  - practice
date: 2025-12-04T23:58:11.572177
---
## Exercise 1: Basic Variables and Data Types
**Difficulty:** Beginner  
**Time Estimate:** 15 minutes

### Objective
Implement a function that takes a user's name and age as input and returns a greeting message with their name and a comment about their age.

### Starter Code
```python
def greet_user(name, age):
    # TODO: Implement this
    pass
```

### Requirements
- The greeting should say: "Hello, [name]! You are [age] years old."
- Handle cases where the name might be an empty string or the age is less than 0.

### Test Cases
```python
assert greet_user("Alice", 30) == "Hello, Alice! You are 30 years old."
assert greet_user("", 25) == "Hello, ! You are 25 years old."
assert greet_user("Bob", -5) == "Hello, Bob! You are -5 years old."
```

### Hints
- Use string formatting to construct your output message.
- Consider using an `if` statement to check for an empty string or negative age.


## Exercise 2: Control Structures
**Difficulty:** Intermediate  
**Time Estimate:** 25 minutes

### Objective
Create a function that checks if a number is even or odd and returns a corresponding message.

### Starter Code
```python
def check_even_odd(number):
    # TODO: Implement this
    pass
```

### Requirements
- If the number is even, return "The number [number] is even."
- If the number is odd, return "The number [number] is odd."
- Handle edge cases like extremely large or small numbers.

### Test Cases
```python
assert check_even_odd(4) == "The number 4 is even."
assert check_even_odd(7) == "The number 7 is odd."
assert check_even_odd(0) == "The number 0 is even."
assert check_even_odd(-2) == "The number -2 is even."
```

### Hints
- Use the modulus operator `%` to determine if a number is even or odd.
- Remember to consider how negative numbers behave with respect to even and odd.


## Exercise 3: Functions and Loops
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Implement a function that generates a list of squares of numbers from 1 to n.

### Starter Code
```python
def generate_squares(n):
    # TODO: Implement this
    pass
```

### Requirements
- Return a list containing squares of all numbers from 1 to n.
- If n is less than 1, return an empty list.

### Test Cases
```python
assert generate_squares(5) == [1, 4, 9, 16, 25]
assert generate_squares(0) == []
assert generate_squares(-3) == []
```

### Hints
- Use a `for` loop to iterate through the range of numbers.
- Make sure to append each square to a list and return it at the end.


## Exercise 4: Introduction to Data Structures
**Difficulty:** Intermediate  
**Time Estimate:** 35 minutes

### Objective
Create a function that takes a list of numbers and returns a dictionary with the count of each unique number.

### Starter Code
```python
def count_numbers(numbers):
    # TODO: Implement this
    pass
```

### Requirements
- The function should return a dictionary where the keys are the unique numbers and the values are their counts.
- Handle empty lists by returning an empty dictionary.

### Test Cases
```python
assert count_numbers([1, 2, 2, 3]) == {1: 1, 2: 2, 3: 1}
assert count_numbers([]) == {}
assert count_numbers([5, 5, 5, 5, 2]) == {5: 4, 2: 1}
```

### Hints
- Consider using a `for` loop to go through the list and a dictionary to keep track of counts.
- Check if a number is already a key in the dictionary to update the count.


## Exercise 5: Working with Strings
**Difficulty:** Intermediate  
**Time Estimate:** 40 minutes

### Objective
Write a function that takes a string and returns a new string with each word capitalized.

### Starter Code
```python
def capitalize_words(sentence):
    # TODO: Implement this
    pass
```

### Requirements
- Each word in the string should start with an uppercase letter.
- Handle cases with multiple spaces between words.

### Test Cases
```python
assert capitalize_words("hello world") == "Hello World"
assert capitalize_words("python programming") == "Python Programming"
assert capitalize_words("    leading spaces") == "    Leading Spaces"
assert capitalize_words("") == ""
```

### Hints
- Use the `split()` method to break the sentence into words.
- Use a loop or list comprehension to capitalize each word and then join them back into a single string.