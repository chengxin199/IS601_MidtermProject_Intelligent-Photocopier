# Lesson Content: Defensive Programming, Errors, and Contracts

## Module 1: EAFP vs LBYL (45 minutes)

### 1.1 Understanding the Paradigms

#### LBYL (Look Before You Leap)
```python
# Check before acting
if 'key' in dictionary:
    value = dictionary['key']
else:
    value = default_value

# File operations
if os.path.exists(filename):
    with open(filename, 'r') as f:
        content = f.read()
```

**Characteristics:**
- Explicit checks before operations
- More defensive, prevents errors
- Can lead to race conditions
- Common in languages like C

#### EAFP (Easier to Ask for Forgiveness than Permission)
```python
# Act first, handle exceptions
try:
    value = dictionary['key']
except KeyError:
    value = default_value

# File operations
try:
    with open(filename, 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = default_content
```

**Characteristics:**
- Pythonic approach
- Handles edge cases naturally
- Atomic operations
- Better performance in success cases

### 1.2 When to Use Each

**Use LBYL when:**
- Cost of exception is high
- External validation is needed
- User input validation
- Resource availability checks

**Use EAFP when:**
- Normal case is expected to succeed
- Atomic operations needed
- Race conditions are possible
- Following Python idioms

### 1.3 Performance Considerations
```python
import timeit

# LBYL approach
def lbyl_lookup(data, key):
    if key in data:
        return data[key]
    return None

# EAFP approach
def eafp_lookup(data, key):
    try:
        return data[key]
    except KeyError:
        return None

# EAFP is typically faster when key exists
```

## Module 2: Contracts and Assertions (60 minutes)

### 2.1 Design by Contract

#### Preconditions
```python
def divide(dividend, divisor):
    """Divide two numbers.

    Preconditions:
    - divisor must not be zero
    - both parameters must be numbers
    """
    assert isinstance(dividend, (int, float)), "Dividend must be a number"
    assert isinstance(divisor, (int, float)), "Divisor must be a number"
    assert divisor != 0, "Divisor cannot be zero"

    return dividend / divisor
```

#### Postconditions
```python
def calculate_discount(price, discount_percent):
    """Calculate discounted price.

    Postconditions:
    - result is always <= original price
    - result is always >= 0
    """
    assert 0 <= discount_percent <= 100, "Discount must be between 0-100%"

    result = price * (1 - discount_percent / 100)

    assert result <= price, "Discounted price cannot exceed original"
    assert result >= 0, "Price cannot be negative"

    return result
```

#### Invariants
```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._check_invariants()

    def _check_invariants(self):
        """Account invariants that must always hold."""
        assert self._balance >= 0, "Balance cannot be negative"

    def deposit(self, amount):
        assert amount > 0, "Deposit amount must be positive"
        self._balance += amount
        self._check_invariants()

    def withdraw(self, amount):
        assert amount > 0, "Withdrawal amount must be positive"
        assert amount <= self._balance, "Insufficient funds"
        self._balance -= amount
        self._check_invariants()
```

### 2.2 Guard Clauses

#### Before: Nested Conditions
```python
def process_order(order):
    if order is not None:
        if order.is_valid():
            if order.customer.is_active():
                if order.total > 0:
                    # Process the order
                    return process_payment(order)
                else:
                    raise ValueError("Order total must be positive")
            else:
                raise ValueError("Customer account is inactive")
        else:
            raise ValueError("Invalid order")
    else:
        raise ValueError("Order cannot be None")
```

#### After: Guard Clauses
```python
def process_order(order):
    # Guard clauses handle edge cases early
    if order is None:
        raise ValueError("Order cannot be None")

    if not order.is_valid():
        raise ValueError("Invalid order")

    if not order.customer.is_active():
        raise ValueError("Customer account is inactive")

    if order.total <= 0:
        raise ValueError("Order total must be positive")

    # Happy path is clear and unindented
    return process_payment(order)
```

### 2.3 Assertions vs Exceptions

**Use Assertions for:**
- Development-time checks
- Internal consistency
- Invariants
- Debugging aids

**Use Exceptions for:**
- Runtime error handling
- User input validation
- External system failures
- Recoverable errors

```python
def factorial(n):
    # Assertion for internal consistency (development check)
    assert isinstance(n, int), "Internal error: n should be int"

    # Exception for user input validation (runtime check)
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n <= 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    # Assertion for postcondition (development check)
    assert result > 0, "Internal error: factorial should be positive"

    return result
```

## Module 3: Exception Handling (60 minutes)

### 3.1 Python Exception Hierarchy

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      |    +-- OverflowError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- ValueError
      +-- TypeError
      +-- RuntimeError
      +-- OSError
           +-- FileNotFoundError
           +-- PermissionError
```

### 3.2 Custom Exceptions

```python
# Base exception for your application
class CalculatorError(Exception):
    """Base exception for calculator operations."""
    pass

# Specific exceptions
class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is attempted."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""
    pass

class InvalidInputError(CalculatorError):
    """Raised when invalid input is provided."""

    def __init__(self, message, input_value=None):
        super().__init__(message)
        self.input_value = input_value

# Usage
def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError(
            f"Both operands must be numbers, got {type(a)} and {type(b)}",
            input_value=(a, b)
        )

    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")

    return a / b
```

### 3.3 Error Boundaries and Context

```python
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)

@contextmanager
def error_boundary(operation_name, **context):
    """Provide error boundary with logging context."""
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
        with open(filename) as f:
            return f.read()
```

## Module 4: Logging and Error Messages (45 minutes)

### 4.1 Actionable Error Messages

```python
# Bad: Vague error messages
def load_config(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except Exception:
        raise ValueError("Configuration error")

# Good: Specific, actionable messages
def load_config(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Configuration file '{filename}' not found. "
            f"Please ensure the file exists and you have read permissions."
        )
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON in configuration file '{filename}' at line {e.lineno}, "
            f"column {e.colno}: {e.msg}"
        )
    except PermissionError:
        raise PermissionError(
            f"Permission denied reading configuration file '{filename}'. "
            f"Please check file permissions."
        )
```

### 4.2 Logging Best Practices

```python
import logging
from typing import Any, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def safe_log_context(**kwargs: Any) -> Dict[str, Any]:
    """Create logging context, filtering sensitive data."""
    sensitive_keys = {'password', 'token', 'secret', 'key'}

    safe_context = {}
    for key, value in kwargs.items():
        if any(sensitive in key.lower() for sensitive in sensitive_keys):
            safe_context[key] = '[REDACTED]'
        else:
            safe_context[key] = value

    return safe_context

def authenticate_user(username, password):
    context = safe_log_context(username=username, password=password)

    try:
        logger.info("Attempting user authentication", extra=context)
        # Authentication logic here
        user = perform_authentication(username, password)
        logger.info("User authentication successful", extra=context)
        return user
    except AuthenticationError as e:
        logger.warning(
            f"Authentication failed: {e}",
            extra={**context, "error_type": type(e).__name__}
        )
        raise
    except Exception as e:
        logger.error(
            f"Unexpected error during authentication: {e}",
            extra=context,
            exc_info=True
        )
        raise
```

## Module 5: Practical Patterns (60 minutes)

### 5.1 Sentinel Values vs Exceptions

```python
# Sentinel pattern
MISSING = object()  # Sentinel value

def get_value(data, key, default=MISSING):
    """Get value with optional default."""
    if key not in data:
        if default is MISSING:
            raise KeyError(f"Key '{key}' not found and no default provided")
        return default
    return data[key]

# Exception pattern
def get_value_strict(data, key):
    """Get value, always raise on missing key."""
    try:
        return data[key]
    except KeyError:
        raise KeyError(f"Required key '{key}' not found in data")
```

### 5.2 Validation Patterns

```python
from typing import Union, List
from dataclasses import dataclass

@dataclass
class ValidationResult:
    is_valid: bool
    errors: List[str]

    def add_error(self, error: str):
        self.is_valid = False
        self.errors.append(error)

def validate_email(email: str) -> ValidationResult:
    """Validate email format."""
    result = ValidationResult(is_valid=True, errors=[])

    if not email:
        result.add_error("Email cannot be empty")
        return result

    if '@' not in email:
        result.add_error("Email must contain @ symbol")

    if email.count('@') > 1:
        result.add_error("Email can only contain one @ symbol")

    local, _, domain = email.partition('@')

    if not local:
        result.add_error("Email must have local part before @")

    if not domain:
        result.add_error("Email must have domain part after @")

    return result

# Usage with exceptions
def create_user(email: str, name: str):
    validation = validate_email(email)
    if not validation.is_valid:
        raise ValueError(f"Invalid email: {'; '.join(validation.errors)}")

    # Proceed with user creation
    return User(email=email, name=name)
```

### 5.3 Retry Patterns with Defensive Programming

```python
import time
import random
from typing import Callable, Any, Optional
from functools import wraps

def retry_with_backoff(
    max_attempts: int = 3,
    backoff_factor: float = 1.0,
    exceptions: tuple = (Exception,)
):
    """Retry decorator with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception: Optional[Exception] = None

            for attempt in range(max_attempts):
                try:
                    logger.debug(f"Attempt {attempt + 1} of {max_attempts} for {func.__name__}")
                    return func(*args, **kwargs)

                except exceptions as e:
                    last_exception = e

                    if attempt == max_attempts - 1:
                        logger.error(f"All {max_attempts} attempts failed for {func.__name__}")
                        break

                    delay = backoff_factor * (2 ** attempt) + random.uniform(0, 1)
                    logger.warning(
                        f"Attempt {attempt + 1} failed for {func.__name__}: {e}. "
                        f"Retrying in {delay:.2f} seconds..."
                    )
                    time.sleep(delay)

            # All attempts failed
            raise last_exception

        return wrapper
    return decorator

# Usage
@retry_with_backoff(max_attempts=3, exceptions=(ConnectionError, TimeoutError))
def fetch_data_from_api(url: str) -> dict:
    # API call that might fail
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()
```

## Hands-on Exercise Overview

You'll now practice these concepts by hardening an existing module. Choose from:

1. **Calculator module** - Add defensive programming to mathematical operations
2. **Configuration loader** - Harden file loading and parsing logic
3. **Custom module** - Apply concepts to your own code

For each module, you'll:
- Add precondition and postcondition checks
- Replace return codes with custom exceptions
- Implement guard clauses
- Add comprehensive logging
- Write tests for error scenarios

Ready to start practicing? Head to the `practice/` folder!
