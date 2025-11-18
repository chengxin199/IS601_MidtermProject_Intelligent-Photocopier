---
title: Defensive Programming - Common Pitfalls
layout: layouts/base.njk
tags:
  - reference
date: 2025-11-17T20:03:21.601943
---
# Common Pitfalls in Defensive Programming

## 1. Exception Handling Anti-Patterns

### Over-catching Exceptions
```python
# BAD: Catching all exceptions hides bugs
try:
    result = complex_operation()
    process_result(result)
    save_to_database(result)
except Exception:
    return "Something went wrong"  # Too vague!

# GOOD: Catch specific exceptions
try:
    result = complex_operation()
    process_result(result)
    save_to_database(result)
except ValidationError as e:
    logger.warning(f"Validation failed: {e}")
    return f"Invalid data: {e}"
except DatabaseError as e:
    logger.error(f"Database error: {e}")
    return "Database temporarily unavailable"
except Exception as e:
    logger.error(f"Unexpected error: {e}", exc_info=True)
    raise  # Re-raise unexpected errors
```

### Using Exceptions for Control Flow
```python
# BAD: Using exceptions for normal program flow
def find_user_by_email(email):
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None  # Exception for normal case

# GOOD: Use conditional logic for expected cases
def find_user_by_email(email):
    users = User.objects.filter(email=email)
    return users.first() if users.exists() else None
```

### Bare Except Clauses
```python
# BAD: Bare except catches everything, including system exits
try:
    risky_operation()
except:  # Catches SystemExit, KeyboardInterrupt, etc.
    pass

# GOOD: Catch specific exceptions
try:
    risky_operation()
except (ValueError, TypeError) as e:
    logger.warning(f"Expected error: {e}")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise
```

## 2. Input Validation Problems

### Trusting User Input
```python
# BAD: No validation
def transfer_money(from_account, to_account, amount):
    from_account.balance -= amount
    to_account.balance += amount

# GOOD: Comprehensive validation
def transfer_money(from_account, to_account, amount):
    # Validate inputs
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be numeric")

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if from_account.balance < amount:
        raise ValueError("Insufficient funds")

    if from_account.id == to_account.id:
        raise ValueError("Cannot transfer to same account")

    # Perform transfer
    from_account.balance -= amount
    to_account.balance += amount
```

### Incomplete Validation
```python
# BAD: Only checking for None
def process_email(email):
    if email is not None:
        return email.lower().strip()

# GOOD: Comprehensive email validation
def process_email(email):
    if not email:
        raise ValueError("Email cannot be empty")

    if not isinstance(email, str):
        raise TypeError("Email must be a string")

    email = email.strip()

    if not email:
        raise ValueError("Email cannot be just whitespace")

    if '@' not in email:
        raise ValueError("Email must contain @ symbol")

    return email.lower()
```

### Not Validating Ranges
```python
# BAD: No range validation
def set_age(age):
    self.age = age

# GOOD: Range validation
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if age < 0:
        raise ValueError("Age cannot be negative")

    if age > 150:
        raise ValueError("Age cannot exceed 150")

    self.age = age
```

## 3. Logging Security Issues

### Logging Sensitive Information
```python
# BAD: Logging passwords and keys
def authenticate_user(username, password, api_key):
    logger.info(f"Authenticating user: {username} with password: {password}")
    logger.debug(f"Using API key: {api_key}")

# GOOD: Redact sensitive information
def authenticate_user(username, password, api_key):
    logger.info(f"Authenticating user: {username}")
    logger.debug(f"Using API key: {api_key[:8]}...")  # Only show prefix
```

### Information Disclosure in Error Messages
```python
# BAD: Revealing internal details
def get_user_file(user_id, filename):
    file_path = f"/internal/users/{user_id}/files/{filename}"
    try:
        with open(file_path) as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")  # Reveals internal structure

# GOOD: Generic user-facing messages
def get_user_file(user_id, filename):
    file_path = f"/internal/users/{user_id}/files/{filename}"
    try:
        with open(file_path) as f:
            return f.read()
    except FileNotFoundError:
        logger.warning(f"File not found: {file_path}")  # Log internally
        raise FileNotFoundError(f"Requested file not found")  # Generic message
```

### Unstructured Logging
```python
# BAD: Unstructured log messages
logger.info(f"User {user_id} performed action {action} at {timestamp}")

# GOOD: Structured logging
logger.info(
    "User action performed",
    extra={
        'user_id': user_id,
        'action': action,
        'timestamp': timestamp,
        'ip_address': request.remote_addr
    }
)
```

## 4. Contract Design Problems

### Over-using Assertions
```python
# BAD: Using assertions for user input validation
def withdraw_money(account, amount):
    assert amount > 0, "Amount must be positive"  # Will disappear in production!
    assert account.balance >= amount, "Insufficient funds"

    account.balance -= amount

# GOOD: Use exceptions for runtime validation
def withdraw_money(account, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    if account.balance < amount:
        raise ValueError("Insufficient funds")

    # Assertions for internal consistency only
    assert account.balance >= 0, "Balance should never be negative"

    account.balance -= amount
```

### Inconsistent Error Types
```python
# BAD: Using different exception types for similar errors
def divide(a, b):
    if b == 0:
        return None  # Sometimes return None

def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")  # Sometimes raise ValueError

def power(a, b):
    if b < 0 and a == 0:
        raise ArithmeticError("0 cannot be raised to negative power")  # Sometimes ArithmeticError

# GOOD: Consistent exception hierarchy
class MathError(Exception):
    """Base exception for math operations."""
    pass

class DivisionByZeroError(MathError):
    """Raised when division by zero is attempted."""
    pass

def divide(a, b):
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")

def modulo(a, b):
    if b == 0:
        raise DivisionByZeroError("Cannot perform modulo by zero")
```

## 5. Error Recovery Problems

### Silent Failures
```python
# BAD: Silently ignoring errors
def save_user_preferences(user_id, preferences):
    try:
        database.save(user_id, preferences)
    except DatabaseError:
        pass  # User never knows it failed!

# GOOD: Proper error handling with fallback
def save_user_preferences(user_id, preferences):
    try:
        database.save(user_id, preferences)
    except DatabaseError as e:
        logger.error(f"Failed to save preferences for user {user_id}: {e}")

        # Try fallback storage
        try:
            cache.save(user_id, preferences)
            logger.info(f"Saved preferences to cache for user {user_id}")
        except CacheError:
            # Final fallback - notify user
            raise UserServiceError("Unable to save preferences. Please try again later.")
```

### Not Providing Error Context
```python
# BAD: Generic error messages
def process_file(filename):
    try:
        data = load_file(filename)
        result = process_data(data)
        save_result(result)
    except Exception:
        raise ProcessingError("File processing failed")

# GOOD: Specific error context
def process_file(filename):
    try:
        data = load_file(filename)
    except FileNotFoundError:
        raise ProcessingError(f"Input file '{filename}' not found")
    except PermissionError:
        raise ProcessingError(f"No permission to read file '{filename}'")

    try:
        result = process_data(data)
    except ValidationError as e:
        raise ProcessingError(f"Data validation failed in file '{filename}': {e}")

    try:
        save_result(result)
    except Exception as e:
        raise ProcessingError(f"Failed to save results for file '{filename}': {e}")
```

## 6. Performance Pitfalls

### Expensive Validation in Hot Paths
```python
# BAD: Expensive validation on every call
def add_to_list(items, new_item):
    # Expensive validation on every add
    assert all(isinstance(item, str) for item in items), "All items must be strings"
    assert isinstance(new_item, str), "New item must be string"

    items.append(new_item)

# GOOD: Validate once, trust internal calls
class StringList:
    def __init__(self, items=None):
        self._items = []
        if items:
            for item in items:
                self.add(item)  # Validate each item once

    def add(self, item):
        if not isinstance(item, str):
            raise TypeError("Item must be a string")
        self._items.append(item)

    def _unsafe_add(self, item):
        """Internal method that skips validation."""
        self._items.append(item)
```

### Creating Exceptions in Normal Flow
```python
# BAD: Creating exceptions for expected conditions
def get_config_value(key):
    try:
        return config[key]
    except KeyError:
        return default_values[key]  # Exception creation is expensive

# GOOD: Use conditionals for expected conditions
def get_config_value(key):
    if key in config:
        return config[key]
    return default_values.get(key)
```

## 7. Testing Pitfalls

### Not Testing Error Paths
```python
# BAD: Only testing happy path
def test_divide():
    assert divide(10, 2) == 5

# GOOD: Test both success and error cases
def test_divide():
    # Happy path
    assert divide(10, 2) == 5

    # Error cases
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    with pytest.raises(TypeError):
        divide("10", 2)
```

### Testing Implementation Instead of Behavior
```python
# BAD: Testing internal implementation
def test_user_validation():
    user = User("john", "john@example.com", 25)
    assert hasattr(user, '_validated')  # Testing internal state

# GOOD: Testing external behavior
def test_user_validation():
    # Valid user should be created successfully
    user = User("john", "john@example.com", 25)
    assert user.name == "john"
    assert user.email == "john@example.com"

    # Invalid user should raise appropriate error
    with pytest.raises(ValidationError):
        User("", "invalid-email", -5)
```

## 8. Code Organization Problems

### Mixing Validation and Business Logic
```python
# BAD: Validation mixed with business logic
def process_order(order_data):
    # Validation mixed with processing
    if not order_data.get('customer_id'):
        raise ValueError("Customer ID required")

    customer = get_customer(order_data['customer_id'])

    if not order_data.get('items'):
        raise ValueError("Order items required")

    total = calculate_total(order_data['items'])

    if total <= 0:
        raise ValueError("Order total must be positive")

    # More validation mixed with processing...

# GOOD: Separate validation from business logic
def validate_order_data(order_data):
    """Validate order data structure."""
    errors = []

    if not order_data.get('customer_id'):
        errors.append("Customer ID required")

    if not order_data.get('items'):
        errors.append("Order items required")

    if errors:
        raise ValidationError(f"Invalid order data: {'; '.join(errors)}")

def process_order(order_data):
    """Process a validated order."""
    validate_order_data(order_data)

    customer = get_customer(order_data['customer_id'])
    total = calculate_total(order_data['items'])

    if total <= 0:
        raise ValueError("Order total must be positive")

    # Pure business logic...
```

## Prevention Strategies

### 1. Use Static Analysis Tools
```bash
# Flake8 for style and basic errors
flake8 --max-line-length=88 src/

# Pylint for deeper analysis
pylint src/

# Mypy for type checking
mypy src/
```

### 2. Code Review Checklist
- [ ] Are all inputs validated at boundaries?
- [ ] Are specific exceptions used instead of generic ones?
- [ ] Are error messages actionable and safe?
- [ ] Is sensitive data properly redacted in logs?
- [ ] Are contracts (pre/postconditions) clear?
- [ ] Are error paths tested?
- [ ] Is exception handling consistent?

### 3. Testing Strategy
```python
# Test error conditions systematically
class TestErrorHandling:
    def test_invalid_inputs(self):
        """Test all types of invalid inputs."""
        invalid_inputs = [None, "", [], {}, -1, "invalid"]
        for invalid_input in invalid_inputs:
            with pytest.raises((ValueError, TypeError)):
                process_function(invalid_input)

    def test_boundary_conditions(self):
        """Test edge cases and boundaries."""
        # Test minimum and maximum values
        # Test empty collections
        # Test exact boundary values
        pass

    def test_error_messages(self):
        """Test error messages are helpful."""
        try:
            invalid_operation()
        except ValueError as e:
            assert "specific helpful message" in str(e)
```

By avoiding these common pitfalls, your defensive programming will be more effective, secure, and maintainable.
