---
title: Introduction to javascript - Exercise Instructions
layout: layouts/course.njk
courseId: J2-javascript-learning
permalink: /Lessons/J2-javascript-learning/index.html
tags:
  - exercises
  - practice
date: 2025-12-08T17:27:47.037491
---
## Exercise 1: Basic Arithmetic Operations
**Difficulty:** Beginner  
**Time Estimate:** 15 minutes

### Objective
Implement a function that performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.

### Starter Code
```python
def calculate(operation, num1, num2):
    # TODO: Implement addition, subtraction, multiplication, and division
    # If operation is 'add', return num1 + num2
    # If operation is 'subtract', return num1 - num2
    # If operation is 'multiply', return num1 * num2
    # If operation is 'divide', return num1 / num2 (handle division by zero)
    pass
```

### Requirements
- Implement addition, subtraction, multiplication, and division.
- Handle division by zero by returning a specific message (e.g., "Cannot divide by zero").
- Ensure the function returns an appropriate message for unsupported operations.

### Test Cases
```python
assert calculate('add', 5, 3) == 8
assert calculate('subtract', 5, 3) == 2
assert calculate('multiply', 5, 3) == 15
assert calculate('divide', 6, 3) == 2
assert calculate('divide', 6, 0) == "Cannot divide by zero"
assert calculate('modulus', 6, 3) == "Unsupported operation"
```

### Hints
- Use if-elif statements to check for the operation type.
- Remember to handle the division case separately to avoid division by zero errors.

---

## Exercise 2: Simple Temperature Converter
**Difficulty:** Intermediate  
**Time Estimate:** 20 minutes

### Objective
Create a function that converts temperatures between Celsius and Fahrenheit.

### Starter Code
```python
def temperature_converter(value, unit):
    # TODO: Implement temperature conversion
    # If unit is 'C', convert to Fahrenheit using (value * 9/5) + 32
    # If unit is 'F', convert to Celsius using (value - 32) * 5/9
    # Handle invalid unit input gracefully
    pass
```

### Requirements
- Convert Celsius to Fahrenheit and vice versa.
- Validate the input unit and return an error message for unsupported units.
- Allow for decimal values in temperature.

### Test Cases
```python
assert temperature_converter(0, 'C') == 32
assert temperature_converter(32, 'F') == 0
assert temperature_converter(100, 'C') == 212
assert temperature_converter(212, 'F') == 100
assert temperature_converter(100, 'K') == "Unsupported unit"
```

### Hints
- Use a simple if-elif structure to handle the unit conversion.
- You can use Python’s float type to handle decimal values.

---

## Exercise 3: Word Counter
**Difficulty:** Intermediate  
**Time Estimate:** 25 minutes

### Objective
Develop a function that counts the occurrences of each word in a given string.

### Starter Code
```python
def word_counter(text):
    # TODO: Split the text into words and count occurrences
    # Use a dictionary to keep track of word counts
    # Ignore case by converting everything to lowercase
    pass
```

### Requirements
- Split the input text into words and count how many times each word appears.
- The function should ignore case sensitivity (e.g., "Hello" and "hello" count as the same word).
- Return the counts as a dictionary.

### Test Cases
```python
assert word_counter("Hello world hello") == {'hello': 2, 'world': 1}
assert word_counter("This is a test. This test is only a test.") == {'this': 2, 'is': 2, 'a': 2, 'test.': 1, 'only': 1}
assert word_counter("") == {}
```

### Hints
- Use the `str.split()` method to break the text into words.
- Consider using the `collections.Counter` class from the Python standard library to simplify counting.

---

## Exercise 4: Simple To-Do List
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Implement a simple to-do list manager that can add, remove, and list tasks.

### Starter Code
```python
class TodoList:
    def __init__(self):
        # TODO: Initialize an empty list to hold tasks
        self.tasks = []

    def add_task(self, task):
        # TODO: Add a task to the list
        pass

    def remove_task(self, task):
        # TODO: Remove a task from the list, if it exists
        pass

    def list_tasks(self):
        # TODO: Return the current list of tasks
        pass
```

### Requirements
- The `add_task` method should append a new task.
- The `remove_task` method should remove a task if it exists and handle cases where the task is not found.
- The `list_tasks` method should return a list of current tasks.

### Test Cases
```python
todo = TodoList()
todo.add_task("Buy milk")
todo.add_task("Go to gym")
assert todo.list_tasks() == ["Buy milk", "Go to gym"]

todo.remove_task("Buy milk")
assert todo.list_tasks() == ["Go to gym"]

todo.remove_task("Not in the list")  # Should not raise an error
assert todo.list_tasks() == ["Go to gym"]
```

### Hints
- Use list methods `append` and `remove` to manage the tasks.
- To check if a task exists, use the `in` keyword.

---

These exercises will help students master JavaScript concepts through practical coding tasks. Each exercise builds on the previous one, incrementally increasing in complexity and requiring students to apply their understanding in a hands-on manner.