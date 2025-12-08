---
title: InTRODUCTION to javascript - Exercise Instructions
layout: layouts/course.njk
courseId: J4-javascript-learning
permalink: /Lessons/J4-javascript-learning/index.html
tags:
  - exercises
  - practice
date: 2025-12-08T17:41:33.611796
---
## Exercise 1: Basic Variables and Data Types
**Difficulty:** Beginner  
**Time Estimate:** 15 minutes

### Objective
Implement a function that initializes and returns variables of different data types: string, integer, float, and boolean.

### Starter Code
```python
def initialize_variables():
    # TODO: Initialize a string variable
    my_string = "Hello, JavaScript!"
    
    # TODO: Initialize an integer variable
    my_integer = 42
    
    # TODO: Initialize a float variable
    my_float = 3.14
    
    # TODO: Initialize a boolean variable
    my_boolean = True
    
    return my_string, my_integer, my_float, my_boolean
```

### Requirements
- Return all initialized variables as a tuple.
- Ensure the function can handle the initialization of the different data types.

### Test Cases
```python
# Example test cases
assert initialize_variables() == ("Hello, JavaScript!", 42, 3.14, True)
```

### Hints
- Remember to use proper syntax for each data type.
- You can test the function by printing the results to see if they match your expectations.

---

## Exercise 2: Conditional Statements
**Difficulty:** Intermediate  
**Time Estimate:** 25 minutes

### Objective
Create a function that checks the age of a user and determines if they are an adult (18 years and older) or a minor (under 18).

### Starter Code
```python
def check_age(age):
    # TODO: Implement age check
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
```

### Requirements
- Return "Adult" if the input age is 18 or older.
- Return "Minor" if the input age is less than 18.
- Handle negative ages by returning "Invalid age".

### Test Cases
```python
# Example test cases
assert check_age(20) == "Adult"
assert check_age(15) == "Minor"
assert check_age(-5) == "Invalid age"
```

### Hints
- Make sure to consider edge cases, like exactly 18 years old.
- You can use the `elif` statement if you need to check for more conditions.

---

## Exercise 3: Loops and Iteration
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Write a function that takes a list of numbers and returns a new list containing only the even numbers.

### Starter Code
```python
def filter_even_numbers(numbers):
    # TODO: Initialize an empty list for even numbers
    even_numbers = []
    
    # TODO: Loop through the list and append even numbers to the new list
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    
    return even_numbers
```

### Requirements
- Use a loop to iterate through the input list.
- Check if each number is even and add it to the results list.
- Return the list of even numbers.

### Test Cases
```python
# Example test cases
assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
assert filter_even_numbers([10, 15, 20, 25]) == [10, 20]
assert filter_even_numbers([1, 3, 5]) == []
```

### Hints
- Remember that even numbers can be identified using the modulus operator (`%`).
- You can use list comprehensions for a more concise solution once you are comfortable.

---

## Exercise 4: Functions and Return Values
**Difficulty:** Intermediate  
**Time Estimate:** 35 minutes

### Objective
Create a function that takes a string and returns the string reversed.

### Starter Code
```python
def reverse_string(s):
    # TODO: Initialize an empty string for the reversed version
    reversed_s = ""
    
    # TODO: Loop through the original string in reverse order
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    
    return reversed_s
```

### Requirements
- Loop through the input string from the last character to the first.
- Use string concatenation to build the reversed string.
- Return the reversed string.

### Test Cases
```python
# Example test cases
assert reverse_string("hello") == "olleh"
assert reverse_string("JavaScript") == "tpircSavaJ"
assert reverse_string("") == ""
```

### Hints
- You can also explore using Python's slicing feature to reverse a string more efficiently.
- Pay attention to how loops work with string indices.

---

## Exercise 5: Basic Object Creation
**Difficulty:** Intermediate  
**Time Estimate:** 40 minutes

### Objective
Define a simple object (dictionary) that represents a person with properties like name, age, and city. Implement a function that returns the description of the person.

### Starter Code
```python
def create_person(name, age, city):
    # TODO: Create a dictionary for the person
    person = {
        "name": name,
        "age": age,
        "city": city
    }
    
    return person

def describe_person(person):
    # TODO: Create a description string
    return f"{person['name']} is {person['age']} years old and lives in {person['city']}."
```

### Requirements
- Use a dictionary to represent the person.
- The `describe_person` function should format and return a description based on the person's properties.

### Test Cases
```python
# Example test cases
person = create_person("Alice", 30, "New York")
assert describe_person(person) == "Alice is 30 years old and lives in New York."
```

### Hints
- Remember to use dictionary keys to access the values inside your object.
- Use formatted strings for clear and readable output.