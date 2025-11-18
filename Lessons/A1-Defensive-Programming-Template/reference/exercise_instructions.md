---
title: Defensive Programming - Exercise Instructions
layout: layouts/base.njk
tags:
  - exercises
date: 2025-11-17T20:03:21.602200
---
# Exercise Instructions: Defensive Programming

## Overview
This exercise will guide you through applying defensive programming principles to existing code. You'll work with two modules that have intentional weaknesses that you need to harden.

## Your Tasks

### Phase 1: Analysis (15 minutes)
1. **Study the provided modules**:
   - `calculator.py` - Basic calculator with math operations
   - `config_loader.py` - Configuration file loader and manager

2. **Identify vulnerabilities**:
   - What could go wrong with invalid inputs?
   - Where are error conditions not properly handled?
   - What assumptions are made about data?

3. **Plan your improvements**:
   - What exceptions should be created?
   - Where should guard clauses be added?
   - What contracts (pre/postconditions) are needed?

### Phase 2: Exception Design (20 minutes)
Create a custom exception hierarchy for each module:

```python
# Example for calculator.py
class CalculatorError(Exception):
    """Base exception for calculator operations."""
    pass

class InvalidInputError(CalculatorError):
    """Raised when input validation fails."""
    def __init__(self, message, input_value=None):
        super().__init__(message)
        self.input_value = input_value

class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""
    pass

# Add more specific exceptions...
```

### Phase 3: Input Validation (25 minutes)
Add comprehensive input validation to all functions:

1. **Type checking**: Ensure inputs are expected types
2. **Range validation**: Check for valid ranges (positive numbers, etc.)
3. **Null/empty checks**: Handle None, empty strings, empty collections
4. **Business rule validation**: Domain-specific rules

Example:
```python
def divide(a, b):
    # Type validation
    if not isinstance(a, (int, float)):
        raise InvalidInputError(f"First operand must be numeric, got {type(a).__name__}")

    if not isinstance(b, (int, float)):
        raise InvalidInputError(f"Second operand must be numeric, got {type(b).__name__}")

    # Business rule validation
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")

    return a / b
```

### Phase 4: Guard Clauses (15 minutes)
Refactor nested conditionals into guard clauses:

Before:
```python
def process_order(order):
    if order is not None:
        if order.is_valid():
            if order.customer is not None:
                # Deep nesting...
                return process(order)
            else:
                return "No customer"
        else:
            return "Invalid order"
    else:
        return "No order"
```

After:
```python
def process_order(order):
    if order is None:
        raise ValueError("Order cannot be None")

    if not order.is_valid():
        raise ValueError("Order is not valid")

    if order.customer is None:
        raise ValueError("Order must have a customer")

    # Happy path is clear
    return process(order)
```

### Phase 5: Contracts (20 minutes)
Add explicit preconditions and postconditions:

```python
def factorial(n):
    """Calculate factorial of n.

    Preconditions:
    - n must be a non-negative integer

    Postconditions:
    - result >= 1 for n >= 0
    - result == 1 for n == 0
    """
    # Precondition checks
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")

    # Calculate result
    if n <= 1:
        result = 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i

    # Postcondition checks
    assert result >= 1, "Factorial result must be at least 1"
    if n == 0:
        assert result == 1, "Factorial of 0 must be 1"

    return result
```

### Phase 6: Logging (15 minutes)
Add structured logging with security considerations:

```python
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

def safe_log_context(**kwargs: Any) -> Dict[str, Any]:
    """Create safe logging context, filtering sensitive data."""
    sensitive_keys = {'password', 'token', 'secret', 'key', 'api_key'}

    safe_context = {}
    for key, value in kwargs.items():
        if any(sensitive in key.lower() for sensitive in sensitive_keys):
            safe_context[key] = '[REDACTED]'
        else:
            safe_context[key] = value

    return safe_context

def load_config(filename):
    """Load configuration with proper logging."""
    context = safe_log_context(filename=filename)

    try:
        logger.info("Loading configuration", extra=context)
        # Load logic here...
        logger.info("Configuration loaded successfully", extra=context)
        return config
    except FileNotFoundError as e:
        logger.error(f"Configuration file not found: {e}", extra=context)
        raise
    except Exception as e:
        logger.error(f"Unexpected error loading config: {e}", extra=context, exc_info=True)
        raise
```

### Phase 7: Testing (30 minutes)
Write comprehensive tests for error scenarios:

```python
import pytest

class TestErrorHandling:
    def test_divide_by_zero(self):
        """Test division by zero raises appropriate exception."""
        with pytest.raises(DivisionByZeroError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_invalid_input_types(self):
        """Test invalid input types raise TypeError."""
        with pytest.raises(InvalidInputError):
            divide("10", 5)

        with pytest.raises(InvalidInputError):
            divide(10, "5")

    def test_error_context_included(self):
        """Test that errors include helpful context."""
        try:
            divide("invalid", 5)
        except InvalidInputError as e:
            assert "First operand must be numeric" in str(e)
            assert e.input_value is not None

    def test_contract_violations(self):
        """Test contract preconditions."""
        with pytest.raises(ValueError):
            factorial(-1)

        with pytest.raises(TypeError):
            factorial("5")
```

## Acceptance Criteria

Your implementation is complete when:

- [ ] **No bare except statements** - All exception handling is specific
- [ ] **Custom exceptions used** - Generic exceptions replaced with domain-specific ones
- [ ] **Input validation** - All functions validate inputs with clear error messages
- [ ] **Guard clauses** - Nested conditionals simplified with early returns/raises
- [ ] **Contracts implemented** - Key functions have explicit pre/postconditions
- [ ] **Secure logging** - Logs provide context without exposing sensitive data
- [ ] **Error tests written** - At least 2 new tests covering error scenarios
- [ ] **All tests pass** - Both existing and new tests execute successfully

## Tips for Success

1. **Start small**: Pick one function and harden it completely before moving on
2. **Think like an attacker**: What could go wrong? What edge cases exist?
3. **Be specific**: Replace generic errors with specific, actionable messages
4. **Test early**: Write tests as you implement defensive measures
5. **Review logs**: Ensure no sensitive data leaks into log messages

## Common Patterns to Apply

- **EAFP over LBYL**: Use try/except rather than extensive pre-checking
- **Fail fast**: Validate inputs early and fail with clear messages
- **Consistent error handling**: Use the same exception types for similar errors
- **Meaningful error messages**: Include context about what went wrong and how to fix it

## Next Steps

After completing this exercise:
1. Compare your solution with the reference implementation
2. Reflect on which defensive patterns were most valuable
3. Consider how to apply these patterns to your own projects
4. Think about automated tools that could help enforce these practices
