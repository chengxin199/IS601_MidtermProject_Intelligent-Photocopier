---
title: Defensive Programming - Quick Reference
layout: layouts/course.njk
courseId: A1-Defensive-Programming-Template
tags:
  - reference
  - quick-guide
date: 2025-11-17T20:03:21.602798
---
# Quick Reference: Defensive Programming Patterns

## Exception Hierarchy Template

```python
# Base exception for your module
class ModuleError(Exception):
    """Base exception for [module name] operations."""
    pass

# Input validation errors
class ValidationError(ModuleError):
    """Raised when input validation fails."""
    def __init__(self, message, field_name=None, field_value=None):
        super().__init__(message)
        self.field_name = field_name
        self.field_value = field_value

# Business logic errors
class BusinessRuleError(ModuleError):
    """Raised when business rules are violated."""
    pass

# External dependency errors
class ExternalServiceError(ModuleError):
    """Raised when external services fail."""
    pass
```

## Input Validation Checklist

```python
def validate_input(value, param_name):
    """Comprehensive input validation template."""

    # 1. Null/None check
    if value is None:
        raise ValidationError(f"{param_name} cannot be None")

    # 2. Type check
    if not isinstance(value, expected_type):
        raise ValidationError(
            f"{param_name} must be {expected_type.__name__}, got {type(value).__name__}"
        )

    # 3. Empty check (for collections/strings)
    if hasattr(value, '__len__') and len(value) == 0:
        raise ValidationError(f"{param_name} cannot be empty")

    # 4. Range check (for numbers)
    if isinstance(value, (int, float)):
        if value < min_value or value > max_value:
            raise ValidationError(f"{param_name} must be between {min_value} and {max_value}")

    # 5. Format check (for strings)
    if isinstance(value, str):
        if not re.match(pattern, value):
            raise ValidationError(f"{param_name} has invalid format")

    return value
```

## Guard Clause Pattern

```python
# Template for guard clauses
def function_with_guards(param1, param2, param3):
    """Function using guard clauses for early validation."""

    # Guard clause 1: Handle null cases
    if param1 is None:
        raise ValueError("param1 cannot be None")

    # Guard clause 2: Handle invalid types
    if not isinstance(param2, str):
        raise TypeError("param2 must be a string")

    # Guard clause 3: Handle business rule violations
    if param3 <= 0:
        raise ValueError("param3 must be positive")

    # Guard clause 4: Handle edge cases
    if len(param2.strip()) == 0:
        raise ValueError("param2 cannot be empty or whitespace")

    # Happy path - main logic is unindented and clear
    result = process_validated_inputs(param1, param2, param3)
    return result
```

## Contract Design Template

```python
def function_with_contract(input_value):
    """Function demonstrating design by contract.

    Preconditions:
    - input_value must be a positive integer
    - input_value must be less than 1000

    Postconditions:
    - result is always greater than input_value
    - result is always even

    Invariants:
    - Function never modifies global state
    """

    # Precondition checks
    assert isinstance(input_value, int), "Precondition: input must be integer"
    assert input_value > 0, "Precondition: input must be positive"
    assert input_value < 1000, "Precondition: input must be less than 1000"

    # Function logic
    result = input_value * 2 + 2

    # Postcondition checks
    assert result > input_value, "Postcondition: result must be greater than input"
    assert result % 2 == 0, "Postcondition: result must be even"

    return result
```

## Error Boundary Pattern

```python
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)

@contextmanager
def error_boundary(operation_name, **context):
    """Create error boundary with logging."""
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
def risky_operation(data):
    with error_boundary("data_processing", data_size=len(data)):
        return process_data(data)
```

## Safe Logging Pattern

```python
def create_safe_log_context(**kwargs):
    """Create logging context with sensitive data redacted."""
    sensitive_keywords = {
        'password', 'token', 'secret', 'key', 'auth',
        'credential', 'private', 'session'
    }

    safe_context = {}
    for key, value in kwargs.items():
        if any(sensitive in key.lower() for sensitive in sensitive_keywords):
            safe_context[key] = '[REDACTED]'
        elif isinstance(value, str) and len(value) > 50:
            safe_context[key] = value[:47] + '...'  # Truncate long values
        else:
            safe_context[key] = value

    return safe_context

# Usage
def authenticate_user(username, password, session_token):
    context = create_safe_log_context(
        username=username,
        password=password,
        session_token=session_token,
        action='authentication'
    )

    logger.info("User authentication attempt", extra=context)
```

## Testing Error Paths Template

```python
import pytest

class TestDefensiveProgramming:
    """Template for testing defensive programming features."""

    def test_null_input_validation(self):
        """Test null input handling."""
        with pytest.raises(ValidationError, match="cannot be None"):
            function_under_test(None)

    def test_invalid_type_validation(self):
        """Test type validation."""
        with pytest.raises(ValidationError, match="must be.*got"):
            function_under_test("invalid_type")

    def test_range_validation(self):
        """Test range validation."""
        with pytest.raises(ValidationError, match="must be between"):
            function_under_test(-1)  # Below minimum

        with pytest.raises(ValidationError, match="must be between"):
            function_under_test(1001)  # Above maximum

    def test_business_rule_validation(self):
        """Test business rule enforcement."""
        with pytest.raises(BusinessRuleError, match="specific business rule"):
            function_under_test(invalid_business_data)

    def test_error_context_included(self):
        """Test that errors include helpful context."""
        try:
            function_under_test(bad_input)
        except ValidationError as e:
            assert hasattr(e, 'field_name')
            assert hasattr(e, 'field_value')
            assert "helpful context" in str(e)

    def test_postcondition_validation(self):
        """Test that postconditions are enforced."""
        result = function_under_test(valid_input)
        assert result > 0, "Postcondition: result must be positive"
        assert isinstance(result, expected_type), "Postcondition: result type"
```

## Common Exception Types Quick Reference

| Situation | Exception Type | Example |
|-----------|---------------|---------|
| Wrong data type | `TypeError` | `TypeError("Expected int, got str")` |
| Invalid value | `ValueError` | `ValueError("Number must be positive")` |
| Missing file | `FileNotFoundError` | `FileNotFoundError("Config file not found")` |
| Missing key | `KeyError` | `KeyError("Required key 'database' missing")` |
| Permission denied | `PermissionError` | `PermissionError("Cannot write to file")` |
| Custom business rule | `CustomError` | `BusinessRuleError("Account inactive")` |

## Performance Considerations

```python
# ✅ GOOD: Check before expensive operation
def expensive_operation(data):
    if not data:  # Fast check first
        raise ValueError("Data cannot be empty")

    if not isinstance(data, list):  # Fast type check
        raise TypeError("Data must be a list")

    # Expensive validation only if needed
    return process_large_dataset(data)

# ❌ BAD: Expensive operation in every case
def expensive_operation(data):
    try:
        result = process_large_dataset(data)  # Always expensive
        return result
    except Exception:
        raise ValueError("Invalid data")
```

## Quick Decision Matrix

| Scenario | Use Assertion | Use Exception |
|----------|---------------|---------------|
| User input validation | ❌ | ✅ |
| Internal consistency check | ✅ | ❌ |
| Debug-time verification | ✅ | ❌ |
| Runtime error handling | ❌ | ✅ |
| Performance-critical path | Consider | ✅ |
| Public API boundary | ❌ | ✅ |
