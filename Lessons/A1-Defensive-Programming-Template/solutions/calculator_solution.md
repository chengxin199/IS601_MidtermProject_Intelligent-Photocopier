---
title: Defensive Programming - Solution
layout: layouts/base.njk
tags:
  - solutions
  - code
date: 2025-11-17T20:03:21.603079
---
# Reference Solutions

## Calculator Module Solution

The following shows how to apply defensive programming principles to the calculator module:

### Custom Exception Hierarchy

```python
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

class MathematicalError(CalculatorError):
    """Raised when a mathematical constraint is violated."""
    pass
```

### Improved Functions with Contracts

```python
import logging
from typing import Union, List

logger = logging.getLogger(__name__)

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Add two numbers.

    Preconditions:
    - Both a and b must be numeric types

    Postconditions:
    - Result is numeric
    """
    # Precondition checks
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError(
            f"Both operands must be numbers, got {type(a).__name__} and {type(b).__name__}",
            input_value=(a, b)
        )

    result = a + b

    # Postcondition check
    assert isinstance(result, (int, float)), "Result must be numeric"

    return result

def divide(a: Number, b: Number) -> Number:
    """Divide a by b.

    Preconditions:
    - Both a and b must be numeric types
    - b must not be zero

    Postconditions:
    - Result is numeric
    """
    # Input validation
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError(
            f"Both operands must be numbers, got {type(a).__name__} and {type(b).__name__}",
            input_value=(a, b)
        )

    # Division by zero check
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")

    result = a / b

    # Postcondition
    assert isinstance(result, (int, float)), "Result must be numeric"

    return result

def square_root(number: Number) -> float:
    """Calculate square root of a number.

    Preconditions:
    - number must be numeric and non-negative

    Postconditions:
    - result >= 0
    """
    if not isinstance(number, (int, float)):
        raise InvalidInputError(
            f"Input must be a number, got {type(number).__name__}",
            input_value=number
        )

    if number < 0:
        raise MathematicalError(
            f"Cannot calculate square root of negative number: {number}"
        )

    result = number ** 0.5

    # Postcondition
    assert result >= 0, "Square root result must be non-negative"

    return result
```

### Improved Calculator Class with Guard Clauses

```python
class Calculator:
    """A defensive calculator class with proper error handling."""

    def __init__(self):
        self.history: List[str] = []
        self._operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide,
            'power': power,
            'sqrt': square_root,
            'factorial': factorial
        }

    def calculate(self, operation: str, a: Number, b: Number = None) -> Number:
        """Perform a calculation with defensive programming.

        Args:
            operation: String name of operation
            a: First operand
            b: Second operand (optional for unary operations)

        Returns:
            Result of calculation

        Raises:
            InvalidInputError: When inputs are invalid
            CalculatorError: When calculation fails
        """
        # Guard clauses for early validation
        if not isinstance(operation, str):
            raise InvalidInputError(
                f"Operation must be a string, got {type(operation).__name__}",
                input_value=operation
            )

        if operation not in self._operations:
            raise InvalidInputError(
                f"Unknown operation: {operation}. "
                f"Available operations: {', '.join(self._operations.keys())}",
                input_value=operation
            )

        # Check for required operands
        unary_operations = {'sqrt', 'factorial'}
        binary_operations = {'add', 'subtract', 'multiply', 'divide', 'power'}

        if operation in binary_operations and b is None:
            raise InvalidInputError(
                f"Operation '{operation}' requires two operands",
                input_value=(operation, a, b)
            )

        if operation in unary_operations and b is not None:
            logger.warning(f"Operation '{operation}' ignores second operand: {b}")

        # Perform calculation with error boundary
        try:
            logger.debug(f"Performing {operation} with operands: a={a}, b={b}")

            if operation in unary_operations:
                result = self._operations[operation](a)
                calculation_str = f"{operation}({a}) = {result}"
            else:
                result = self._operations[operation](a, b)
                calculation_str = f"{operation}({a}, {b}) = {result}"

            self.history.append(calculation_str)
            logger.info(f"Calculation successful: {calculation_str}")

            return result

        except CalculatorError:
            # Re-raise calculator-specific errors
            raise
        except Exception as e:
            # Wrap unexpected errors
            logger.error(
                f"Unexpected error in calculation: {e}",
                extra={
                    "operation": operation,
                    "operands": (a, b),
                    "error_type": type(e).__name__
                },
                exc_info=True
            )
            raise CalculatorError(f"Calculation failed: {e}") from e
```

### Key Improvements Made:

1. **Custom Exception Hierarchy**: Clear, specific exceptions with context
2. **Input Validation**: Type checking with helpful error messages
3. **Guard Clauses**: Early returns/raises to reduce nesting
4. **Contracts**: Explicit pre/postconditions with assertions
5. **Logging**: Contextual logging without sensitive data exposure
6. **Error Boundaries**: Proper exception handling and wrapping

### Testing the Improved Code:

```python
def test_divide_by_zero_raises_exception():
    """Test that division by zero raises specific exception."""
    with pytest.raises(DivisionByZeroError, match="Cannot divide by zero"):
        divide(10, 0)

def test_invalid_input_includes_context():
    """Test that invalid input errors include helpful context."""
    try:
        add("not_a_number", 5)
    except InvalidInputError as e:
        assert "Both operands must be numbers" in str(e)
        assert e.input_value == ("not_a_number", 5)

def test_calculator_unknown_operation():
    """Test calculator handles unknown operations properly."""
    calc = Calculator()
    with pytest.raises(InvalidInputError, match="Unknown operation"):
        calc.calculate("invalid_op", 1, 2)
```

This solution demonstrates:
- **EAFP**: Using try/catch for operations that might fail
- **Contracts**: Clear preconditions and postconditions
- **Guard Clauses**: Early validation to reduce nesting
- **Custom Exceptions**: Meaningful error types with context
- **Defensive Logging**: Information without security risks
