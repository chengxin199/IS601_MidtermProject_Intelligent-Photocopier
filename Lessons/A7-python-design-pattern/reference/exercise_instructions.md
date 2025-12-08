---
title: Advanced python design pattern - Exercise Instructions
layout: layouts/course.njk
courseId: A7-python-design-pattern
permalink: /Lessons/A7-python-design-pattern/exercise-instructions.html
tags:
  - exercises
  - practice
date: 2025-12-08T21:32:58.922253
---
## Exercise 1: Singleton Pattern Implementation
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Implement a Singleton pattern to ensure that a class has only one instance and provide a global point of access to it.

### Starter Code
```python
class Singleton:
    _instance = None

    def __new__(cls):
        # TODO: Implement the Singleton pattern here
        pass

    def some_business_logic(self):
        # Placeholder for business logic
        return "Business Logic Executed"
```

### Requirements
- Ensure that only one instance of the `Singleton` class can be created.
- Add a method `some_business_logic` that returns a string indicating that business logic was executed.
- Test that multiple instantiations return the same instance.

### Test Cases
```python
singleton1 = Singleton()
singleton2 = Singleton()

assert singleton1 is singleton2  # Both should refer to the same instance
assert singleton1.some_business_logic() == "Business Logic Executed"
```

### Hints
- Use the `__new__` method to control the instance creation.
- Consider storing the instance in a class variable to ensure only one instance is created.

---

## Exercise 2: Observer Pattern Implementation
**Difficulty:** Advanced  
**Time Estimate:** 45 minutes

### Objective
Create an Observer pattern where multiple observers can subscribe to an event and be notified when it occurs.

### Starter Code
```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        # TODO: Implement the attach method
        pass

    def detach(self, observer):
        # TODO: Implement the detach method
        pass

    def notify(self, message):
        # TODO: Implement the notify method
        pass


class Observer:
    def update(self, message):
        # TODO: Implement the update method to handle notifications
        pass
```

### Requirements
- Implement `attach`, `detach`, and `notify` methods in `Subject`.
- Implement the `update` method in `Observer` to print the notification message.
- Create a simple test to demonstrate that observers receive notifications when the subject's state changes.

### Test Cases
```python
subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello Observers!")  # Both observers should receive this message

# Check if the observers print the expected output
# Note: You may want to use a context manager or mock to verify printed output
```

### Hints
- Use a list to keep track of the observers.
- In the `notify` method, iterate over the observers and call their `update` methods.

---

## Exercise 3: Strategy Pattern Implementation
**Difficulty:** Advanced  
**Time Estimate:** 60 minutes

### Objective
Implement the Strategy pattern to allow for dynamic selection of algorithms at runtime.

### Starter Code
```python
class Strategy:
    def execute(self, data):
        # TODO: Define the interface for strategies
        pass


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        # TODO: Implement algorithm A
        pass


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        # TODO: Implement algorithm B
        pass


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        # TODO: Allow changing strategy
        pass

    def perform_strategy(self, data):
        return self._strategy.execute(data)
```

### Requirements
- Implement at least two concrete strategies (`ConcreteStrategyA` and `ConcreteStrategyB`).
- The `perform_strategy` method should apply the selected strategy to the provided data.
- Demonstrate the ability to switch strategies at runtime.

### Test Cases
```python
data = [1, 2, 3, 4]

context = Context(ConcreteStrategyA())
assert context.perform_strategy(data) == "Result from Strategy A"  # Replace with actual expected result

context.set_strategy(ConcreteStrategyB())
assert context.perform_strategy(data) == "Result from Strategy B"  # Replace with actual expected result
```

### Hints
- Identify the common interface for strategies and ensure each concrete strategy implements that.
- Use a simple algorithm (e.g., sorting, summing) for illustration.

---

## Exercise 4: Factory Method Pattern Implementation
**Difficulty:** Advanced  
**Time Estimate:** 50 minutes

### Objective
Create a Factory Method that allows creating objects without specifying the exact class of object that will be created.

### Starter Code
```python
class Product:
    def operation(self):
        # TODO: Define an operation for the product
        pass


class ConcreteProductA(Product):
    def operation(self):
        return "Result of ConcreteProductA"


class ConcreteProductB(Product):
    def operation(self):
        return "Result of ConcreteProductB"


class Creator:
    def factory_method(self):
        # TODO: Implement factory method
        pass

    def some_operation(self):
        product = self.factory_method()
        return product.operation()
```

### Requirements
- Implement the `factory_method` in the `Creator` class to instantiate `ConcreteProductA` or `ConcreteProductB` based on a parameter.
- Add a method `some_operation` that uses the product's operation.
- Test the factory method by creating both types of products.

### Test Cases
```python
creator_a = Creator()
assert creator_a.factory_method() == "Result of ConcreteProductA"  # Actual product creation logic needed

creator_b = Creator()
assert creator_b.factory_method() == "Result of ConcreteProductB"  # Actual product creation logic needed
```

### Hints
- Consider adding a parameter to the `factory_method` to decide which product to create.
- Use inheritance to implement different products.

---

## Exercise 5: Command Pattern Implementation
**Difficulty:** Advanced  
**Time Estimate:** 60 minutes

### Objective
Implement the Command pattern to encapsulate a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.

### Starter Code
```python
class Command:
    def execute(self):
        # TODO: Define the command interface
        pass


class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        # TODO: Call the appropriate method on the receiver
        pass


class Receiver:
    def action(self):
        return "Receiver Action Executed"


class Invoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        # TODO: Add command to the command list
        pass

    def execute_commands(self):
        for command in self._commands:
            command.execute()
```

### Requirements
- Implement the command interface and concrete command classes.
- Create a `Receiver` that performs actions.
- Add a way to store and execute multiple commands in the `Invoker`.

### Test Cases
```python
receiver = Receiver()
command = ConcreteCommand(receiver)
invoker = Invoker()

invoker.add_command(command)
invoker.execute_commands()  # Should output "Receiver Action Executed"
```

### Hints
- Use a list in the `Invoker` to store commands.
- Ensure each command has a reference to the receiver to invoke the correct method.

---

These exercises will help you master advanced Python design patterns through practical application, enhancing your understanding and enabling you to build real-world projects.