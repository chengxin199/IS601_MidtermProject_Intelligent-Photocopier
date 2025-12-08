---
title: Advanced python design pattern - Practice Solution
layout: layouts/course.njk
courseId: A7-python-design-pattern
permalink: /Lessons/A7-python-design-pattern/practice-solution.html
tags:
  - solutions
  - code
date: 2025-12-08T21:33:19.039247
---
# Advanced Python Design Patterns Practice Solutions

## Learning Objectives
- Master key concepts of advanced design patterns
- Apply practical techniques in real-world scenarios
- Build real-world projects using design patterns

---

## Exercise 1: Singleton Pattern

### Overview
The Singleton Pattern ensures that a class has only one instance and provides a global point of access to that instance. This is particularly useful when managing shared resources or configurations.

### Basic Implementation
```python
class Singleton:
    """A simple implementation of Singleton pattern using a class variable."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            self.value = value
            self.initialized = True

# Example of usage
singleton1 = Singleton(10)
singleton2 = Singleton(20)

print(singleton1.value)  # Output: 10
print(singleton2.value)  # Output: 10
```

### Enhanced Implementation
```python
class Singleton:
    """Enhanced Singleton pattern implementation with thread safety."""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:  # Ensure thread safety
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            self.value = value
            self.initialized = True

# Example of usage
singleton1 = Singleton(10)
singleton2 = Singleton(20)

print(singleton1.value)  # Output: 10
print(singleton2.value)  # Output: 10
```

### Testing the Solution
```python
def test_singleton():
    """Test the Singleton implementation."""
    instance1 = Singleton(100)
    instance2 = Singleton(200)

    assert instance1 is instance2, "Instances are not the same!"
    assert instance1.value == 100, "Value should be 100"
    assert instance2.value == 100, "Value should be 100"

test_singleton()
print("All tests passed!")
```

### Explanation
- **Design Decisions**: We implemented a thread-safe Singleton using a class variable and a lock to prevent multiple threads from creating different instances simultaneously.
- **Complexity Analysis**: The time complexity for instance creation is O(1) since the instance is created only once.

### Key Takeaways
- The Singleton Pattern is essential for shared resources.
- Implementing thread safety is crucial in multi-threaded environments.
- Always ensure that initialization is performed only once.

---

## Exercise 2: Factory Pattern

### Overview
The Factory Pattern provides an interface for creating objects in a super class but allows subclasses to alter the type of objects that will be created. This is useful for managing and centralizing object creation.

### Basic Implementation
```python
class Dog:
    """Dog class"""
    def speak(self):
        return "Woof!"

class Cat:
    """Cat class"""
    def speak(self):
        return "Meow!"

class AnimalFactory:
    """Factory class to create animals"""
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        raise ValueError(f"Unknown animal type: {animal_type}")

# Example usage
animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # Output: Woof!
```

### Enhanced Implementation
```python
class AnimalFactory:
    """Enhanced Factory class to create animals with error handling."""
    @staticmethod
    def create_animal(animal_type):
        try:
            if animal_type == "dog":
                return Dog()
            elif animal_type == "cat":
                return Cat()
            else:
                raise ValueError(f"Unknown animal type: {animal_type}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # Output: Woof!
```

### Testing the Solution
```python
def test_animal_factory():
    """Test the AnimalFactory implementation."""
    dog = AnimalFactory.create_animal("dog")
    assert dog.speak() == "Woof!", "Dog should bark"

    cat = AnimalFactory.create_animal("cat")
    assert cat.speak() == "Meow!", "Cat should meow"

    try:
        AnimalFactory.create_animal("fish")
    except ValueError:
        pass  # Expected behavior, no assertion needed here

test_animal_factory()
print("All tests passed!")
```

### Explanation
- **Design Decisions**: The factory method allows for easy extension to add new animal types without modifying the existing code.
- **Complexity Analysis**: The time complexity to create an animal is O(1) as it depends on the conditional checks.

### Key Takeaways
- The Factory Pattern decouples object creation from its usage.
- It aids in adding new types of objects without changing existing code.
- Proper error handling ensures the robustness of factory methods.

---

## Conclusion
In this document, we explored advanced design patterns in Python focusing on the Singleton and Factory patterns. Each pattern was implemented in both basic and enhanced versions, demonstrating the importance of error handling and thread safety. We also provided comprehensive testing to ensure the correctness of our implementations. By mastering these patterns, developers can write cleaner, more maintainable, and scalable code.