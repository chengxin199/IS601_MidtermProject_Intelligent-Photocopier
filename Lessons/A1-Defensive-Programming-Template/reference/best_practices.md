---
title: Defensive Programming - Best Practices
layout: layouts/course.njk
courseId: A1-Defensive-Programming-Template
tags:
  - reference
  - best-practices
date: 2025-11-17T20:03:21.601596
---
# Defensive Programming Best Practices

## Core Principles

### 1. Fail Fast and Fail Clearly
```python
# Good - fails immediately with clear message
def process_user_data(user_id, data):
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError(f"Invalid user ID: {user_id}. Must be positive integer.")

    if not isinstance(data, dict):
        raise TypeError(f"Data must be a dictionary, got {type(data).__name__}")

    # Process data...

# Bad - fails later with unclear error
def process_user_data(user_id, data):
    # No validation, might fail deep in processing
    result = complicated_processing(user_id, data)
    return result
```

### 2. Validate at Boundaries
```python
# Good - validate at API boundaries
@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    # Validate early
    if user_id <= 0:
        return jsonify({"error": "Invalid user ID"}), 400

    try:
        user = user_service.get_user(user_id)
        return jsonify(user.to_dict())
    except UserNotFoundError:
        return jsonify({"error": "User not found"}), 404

# Bad - no boundary validation
@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    # Let errors propagate from deep in the stack
    user = user_service.get_user(user_id)
    return jsonify(user.to_dict())
```

### 3. Use EAFP (Easier to Ask for Forgiveness than Permission)
```python
# Good - EAFP approach
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError(f"Cannot divide {a} by zero")
    except TypeError:
        raise TypeError("Both arguments must be numbers")

# Less ideal - LBYL approach (can have race conditions)
def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero")
    return a / b
```

## Design by Contract

### Preconditions
```python
def withdraw_money(account, amount):
    """Withdraw money from account.

    Preconditions:
    - account must be valid and active
    - amount must be positive
    - account must have sufficient balance
    """
    # Check preconditions
    if not account or not account.is_active:
        raise ValueError("Account must be valid and active")

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if account.balance < amount:
        raise ValueError("Insufficient funds")

    # Perform operation
    account.balance -= amount
    return account.balance
```

### Postconditions
```python
def calculate_interest(principal, rate, time):
    """Calculate compound interest.

    Postconditions:
    - result >= principal (for positive rate)
    - result > 0 (for positive principal)
    """
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if time < 0:
        raise ValueError("Time cannot be negative")

    result = principal * (1 + rate) ** time

    # Verify postconditions
    if rate >= 0:
        assert result >= principal, "Result should be >= principal for non-negative rate"
    assert result > 0, "Result should be positive for positive principal"

    return result
```

### Invariants
```python
class BankAccount:
    """Bank account with invariants."""

    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self._balance = initial_balance
        self.transaction_history = []
        self._check_invariants()

    def _check_invariants(self):
        """Check class invariants."""
        assert self._balance >= 0, "Balance cannot be negative"
        assert self.account_number, "Account number cannot be empty"
        assert isinstance(self.transaction_history, list), "History must be a list"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        old_balance = self._balance
        self._balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")

        # Verify invariants still hold
        self._check_invariants()
        assert self._balance == old_balance + amount, "Balance calculation error"

    @property
    def balance(self):
        return self._balance
```

## Guard Clauses Pattern

### Before: Nested Conditionals
```python
def process_order(order):
    if order is not None:
        if order.is_valid():
            if order.customer is not None:
                if order.customer.is_active():
                    if order.items:
                        if order.total > 0:
                            # Deep nesting makes this hard to read
                            return fulfill_order(order)
                        else:
                            raise ValueError("Order total must be positive")
                    else:
                        raise ValueError("Order must have items")
                else:
                    raise ValueError("Customer is not active")
            else:
                raise ValueError("Order must have a customer")
        else:
            raise ValueError("Order is not valid")
    else:
        raise ValueError("Order cannot be None")
```

### After: Guard Clauses
```python
def process_order(order):
    """Process an order with guard clauses."""
    # Guard clauses handle exceptional cases early
    if order is None:
        raise ValueError("Order cannot be None")

    if not order.is_valid():
        raise ValueError("Order is not valid")

    if order.customer is None:
        raise ValueError("Order must have a customer")

    if not order.customer.is_active():
        raise ValueError("Customer is not active")

    if not order.items:
        raise ValueError("Order must have items")

    if order.total <= 0:
        raise ValueError("Order total must be positive")

    # Happy path is clear and unindented
    return fulfill_order(order)
```

## Error Handling Patterns

### 1. Error Boundaries
```python
from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)

@contextmanager
def error_boundary(operation_name, **context):
    """Create an error boundary for operations."""
    try:
        logger.info(f"Starting {operation_name}", extra=context)
        yield
        logger.info(f"Completed {operation_name}", extra=context)
    except Exception as e:
        logger.error(
            f"Error in {operation_name}: {e}",
            extra={**context, "error_type": type(e).__name__},
            exc_info=True
        )
        raise

# Usage
def process_file(filename):
    with error_boundary("file_processing", filename=filename):
        data = load_file(filename)
        result = process_data(data)
        save_result(result)
        return result
```

### 2. Retry with Backoff
```python
import time
import random
from functools import wraps

def retry(max_attempts=3, backoff_factor=1.0, exceptions=(Exception,)):
    """Retry decorator with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e

                    if attempt == max_attempts - 1:
                        break

                    delay = backoff_factor * (2 ** attempt) + random.uniform(0, 1)
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay:.2f}s")
                    time.sleep(delay)

            raise last_exception
        return wrapper
    return decorator

# Usage
@retry(max_attempts=3, exceptions=(ConnectionError, TimeoutError))
def fetch_data(url):
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()
```

### 3. Graceful Degradation
```python
def get_user_preferences(user_id):
    """Get user preferences with fallback to defaults."""
    try:
        # Try to get from primary source
        return preference_service.get_preferences(user_id)
    except ServiceUnavailableError:
        logger.warning(f"Preference service unavailable for user {user_id}")
        try:
            # Fallback to cache
            return cache.get_preferences(user_id)
        except CacheError:
            logger.warning(f"Cache also unavailable for user {user_id}")
            # Final fallback to defaults
            return get_default_preferences()
```

## Input Validation Patterns

### 1. Validation with Context
```python
class ValidationError(Exception):
    """Validation error with context."""
    def __init__(self, message, field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value

def validate_email(email, field_name="email"):
    """Validate email with context."""
    if not email:
        raise ValidationError(
            "Email cannot be empty",
            field=field_name,
            value=email
        )

    if '@' not in email:
        raise ValidationError(
            "Email must contain @ symbol",
            field=field_name,
            value=email
        )

    # More validation...
    return True
```

### 2. Batch Validation
```python
from dataclasses import dataclass
from typing import List

@dataclass
class ValidationResult:
    is_valid: bool
    errors: List[str]

    def add_error(self, error: str):
        self.is_valid = False
        self.errors.append(error)

def validate_user_data(data):
    """Validate user data and collect all errors."""
    result = ValidationResult(is_valid=True, errors=[])

    if not data.get('email'):
        result.add_error("Email is required")
    elif '@' not in data['email']:
        result.add_error("Email must contain @ symbol")

    if not data.get('age'):
        result.add_error("Age is required")
    elif not isinstance(data['age'], int) or data['age'] < 0:
        result.add_error("Age must be a positive integer")

    if not data.get('name'):
        result.add_error("Name is required")
    elif len(data['name']) < 2:
        result.add_error("Name must be at least 2 characters")

    return result
```

## Logging Best Practices

### 1. Structured Logging
```python
import logging
import json

class StructuredFormatter(logging.Formatter):
    """JSON formatter for structured logging."""

    def format(self, record):
        log_data = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }

        # Add extra fields
        if hasattr(record, 'user_id'):
            log_data['user_id'] = record.user_id
        if hasattr(record, 'request_id'):
            log_data['request_id'] = record.request_id

        return json.dumps(log_data)

# Usage
logger = logging.getLogger(__name__)
logger.info(
    "User login successful",
    extra={'user_id': 12345, 'request_id': 'req-abc-123'}
)
```

### 2. Safe Context Logging
```python
def safe_log_context(**kwargs):
    """Create safe logging context by filtering sensitive data."""
    sensitive_keys = {
        'password', 'token', 'secret', 'key', 'auth',
        'api_key', 'private', 'credential'
    }

    safe_context = {}
    for key, value in kwargs.items():
        if any(sensitive in key.lower() for sensitive in sensitive_keys):
            safe_context[key] = '[REDACTED]'
        else:
            safe_context[key] = value

    return safe_context

# Usage
def authenticate_user(username, password, api_key):
    context = safe_log_context(
        username=username,
        password=password,
        api_key=api_key,
        action='authentication'
    )

    logger.info("Starting authentication", extra=context)
    # {'username': 'john', 'password': '[REDACTED]', 'api_key': '[REDACTED]', 'action': 'authentication'}
```

## Performance Considerations

### 1. Assertion Performance
```python
# Assertions can be disabled with -O flag
# Use them for debugging, not for user input validation

def expensive_check():
    """Expensive validation that should only run in debug mode."""
    return all(validate_item(item) for item in large_dataset)

def process_data(data):
    # This assertion will be removed in optimized mode
    assert expensive_check(), "Data integrity check failed"

    # Use exceptions for runtime validation
    if not data:
        raise ValueError("Data cannot be empty")

    return process(data)
```

### 2. Exception Performance
```python
# Exceptions are expensive - don't use for control flow
# Good - check condition first
def get_config_value(config, key, default=None):
    if key in config:
        return config[key]
    return default

# Bad - exception for normal flow
def get_config_value(config, key, default=None):
    try:
        return config[key]
    except KeyError:
        return default
```

## Summary Checklist

When implementing defensive programming:

- [ ] Validate inputs at function boundaries
- [ ] Use specific exception types with clear messages
- [ ] Implement guard clauses to reduce nesting
- [ ] Add logging at error boundaries
- [ ] Include context in error messages
- [ ] Use assertions for internal consistency checks
- [ ] Implement proper error recovery strategies
- [ ] Consider performance implications
- [ ] Write tests for error paths
- [ ] Document contracts (pre/postconditions)
