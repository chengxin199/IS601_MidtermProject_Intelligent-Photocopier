# Python Exception Hierarchy Reference

## Built-in Exception Hierarchy

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

## Common Exception Types and Usage

### ValueError
Used when a function receives an argument with correct type but inappropriate value:
```python
def sqrt(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return x ** 0.5
```

### TypeError
Used when a function receives an argument of wrong type:
```python
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    return a + b
```

### FileNotFoundError
Used when a file operation fails because file doesn't exist:
```python
def load_config(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{filename}' not found")
```

### KeyError
Used when accessing a dictionary key that doesn't exist:
```python
def get_required_config(config, key):
    try:
        return config[key]
    except KeyError:
        raise KeyError(f"Required configuration key '{key}' not found")
```

## Best Practices for Exception Handling

### 1. Catch Specific Exceptions
```python
# Good
try:
    result = risky_operation()
except ValueError as e:
    handle_value_error(e)
except TypeError as e:
    handle_type_error(e)

# Bad
try:
    result = risky_operation()
except Exception:
    handle_any_error()  # Too broad
```

### 2. Use Exception Chaining
```python
# Good - preserves original error context
try:
    config = json.loads(text)
except json.JSONDecodeError as e:
    raise ConfigurationError(f"Invalid JSON in config: {e}") from e

# Also good - suppress original if not relevant
try:
    config = json.loads(text)
except json.JSONDecodeError:
    raise ConfigurationError("Invalid configuration format") from None
```

### 3. Include Helpful Context
```python
# Good
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError(f"Cannot divide {a} by zero")
    return a / b

# Bad
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b
```

### 4. Don't Use Exceptions for Control Flow
```python
# Bad
def get_first_item(items):
    try:
        return items[0]
    except IndexError:
        return None

# Good
def get_first_item(items):
    if not items:
        return None
    return items[0]
```

## Custom Exception Design Patterns

### 1. Module-Specific Base Exception
```python
class MyModuleError(Exception):
    """Base exception for MyModule operations."""
    pass

class ValidationError(MyModuleError):
    """Raised when validation fails."""
    pass

class ProcessingError(MyModuleError):
    """Raised when processing fails."""
    pass
```

### 2. Exception with Context Data
```python
class ValidationError(Exception):
    """Exception with validation context."""

    def __init__(self, message, field_name=None, field_value=None):
        super().__init__(message)
        self.field_name = field_name
        self.field_value = field_value

    def __str__(self):
        base = super().__str__()
        if self.field_name:
            return f"{base} (field: {self.field_name})"
        return base
```

### 3. Exception Hierarchy for Different Error Types
```python
class DatabaseError(Exception):
    """Base database exception."""
    pass

class ConnectionError(DatabaseError):
    """Database connection failed."""
    pass

class QueryError(DatabaseError):
    """Database query failed."""
    pass

class TransactionError(DatabaseError):
    """Database transaction failed."""
    pass
```

## Exception Handling Anti-Patterns

### 1. Silent Failures
```python
# Bad - silently ignores all errors
try:
    risky_operation()
except:
    pass

# Good - handle specific errors appropriately
try:
    risky_operation()
except ExpectedError as e:
    logger.warning(f"Expected error occurred: {e}")
    # Handle appropriately
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise
```

### 2. Generic Exception Messages
```python
# Bad
raise Exception("Something went wrong")

# Good
raise ValueError(f"Invalid input: expected positive number, got {value}")
```

### 3. Catching and Re-raising Without Adding Value
```python
# Bad
try:
    process_data()
except Exception as e:
    raise e  # No added value

# Good
try:
    process_data()
except ProcessingError as e:
    logger.error(f"Failed to process data for user {user_id}: {e}")
    raise  # Re-raise without 'e' to preserve traceback
```

## When to Use Assertions vs Exceptions

### Use Assertions For:
- Internal consistency checks
- Developer errors
- Debugging aids
- Invariants that should never be false

```python
def binary_search(arr, target):
    assert len(arr) > 0, "Array should not be empty"  # Internal check
    assert all(arr[i] <= arr[i+1] for i in range(len(arr)-1)), "Array should be sorted"
    # ... search logic
```

### Use Exceptions For:
- User input validation
- External system failures
- Recoverable errors
- Expected failure conditions

```python
def divide(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("First argument must be a number")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```
