---
title: InTRODUCTION to javascript - Exercise Instructions
layout: layouts/course.njk
courseId: J1-javascript-learning
tags:
  - exercises
  - practice
date: 2025-12-08T16:25:27.266408
---
## Exercise 1: Hello, JavaScript!
**Difficulty:** Beginner  
**Time Estimate:** 10 minutes

### Objective
Implement a function that returns a greeting message. The function should take a name as input and return a string that says "Hello, [name]!".

### Starter Code
```python
def greet(name):
    # TODO: Implement this
    pass
```

### Requirements
- The function should accept a single argument, `name`, which is a string.
- If the name is empty, return "Hello, World!".
- The function should return the greeting message in the format specified.

### Test Cases
```python
assert greet("Alice") == "Hello, Alice!"
assert greet("") == "Hello, World!"
assert greet("Bob") == "Hello, Bob!"
```

### Hints
- You can use string concatenation to build the greeting message.
- Consider using an if statement to check if the name is empty.

---

## Exercise 2: Simple Calculator
**Difficulty:** Beginner  
**Time Estimate:** 15 minutes

### Objective
Create a simple calculator function that takes two numbers and an operator (as a string) and returns the result of the operation. Support addition, subtraction, multiplication, and division.

### Starter Code
```python
def calculator(num1, num2, operator):
    # TODO: Implement this
    pass
```

### Requirements
- The function should accept two numbers and an operator as inputs.
- The operator can be "+", "-", "*", or "/".
- Handle division by zero by returning "Error: Division by zero".

### Test Cases
```python
assert calculator(10, 5, "+") == 15
assert calculator(10, 5, "-") == 5
assert calculator(10, 5, "*") == 50
assert calculator(10, 0, "/") == "Error: Division by zero"
```

### Hints
- Use if-elif statements to check which operation to perform based on the operator.
- Remember to handle the division case carefully to avoid division by zero.

---

## Exercise 3: Count Vowels
**Difficulty:** Beginner  
**Time Estimate:** 20 minutes

### Objective
Write a function that counts the number of vowels in a given string. The function should be case-insensitive.

### Starter Code
```python
def count_vowels(input_string):
    # TODO: Implement this
    pass
```

### Requirements
- The function should accept a single string input.
- Count both uppercase and lowercase vowels (a, e, i, o, u).
- Return the total count of vowels.

### Test Cases
```python
assert count_vowels("Hello World") == 3
assert count_vowels("Python Programming") == 4
assert count_vowels("") == 0
assert count_vowels("AEIOUaeiou") == 10
```

### Hints
- You can use a loop to iterate through the characters of the string.
- Use a set to store the vowels for easy checking.

---

## Exercise 4: FizzBuzz
**Difficulty:** Beginner  
**Time Estimate:** 25 minutes

### Objective
Implement a function that prints numbers from 1 to n (inclusive), but for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".

### Starter Code
```python
def fizz_buzz(n):
    # TODO: Implement this
    pass
```

### Requirements
- The function should accept a single integer `n`.
- Print the results directly instead of returning them.
- Handle cases where n is less than 1 by printing "Input must be a positive integer."

### Test Cases
```python
fizz_buzz(15)  # Expected output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
```

### Hints
- Use a loop to iterate from 1 to n.
- Use if-elif statements to check for multiples of 3 and 5.

---

## Exercise 5: Palindrome Checker
**Difficulty:** Beginner  
**Time Estimate:** 30 minutes

### Objective
Create a function that checks if a given string is a palindrome (reads the same backward as forward).

### Starter Code
```python
def is_palindrome(input_string):
    # TODO: Implement this
    pass
```

### Requirements
- The function should accept a single string input.
- Ignore spaces, punctuation, and capitalization when checking for palindromes.
- Return `True` if the string is a palindrome and `False` otherwise.

### Test Cases
```python
assert is_palindrome("A man a plan a canal Panama") == True
assert is_palindrome("Hello") == False
assert is_palindrome("Racecar") == True
assert is_palindrome("Was it a car or a cat I saw") == True
```

### Hints
- You may want to use the `str.replace()` method to remove spaces and punctuation.
- Consider using the `str.lower()` method to normalize the case before checking.