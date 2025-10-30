"""
Tests for calculator module - Practice for defensive programming.

🎯 YOUR TASK: Apply defensive programming principles to calculator.py

This file contains basic tests for the calculator module. Your job is to:

1. **Study the hardened example**: See test_calculator_hardened.py for a complete
   implementation of defensive programming principles.

2. **Improve calculator.py**: Apply the following defensive programming techniques:
   - Add explicit pre-/post-condition checks and assertions
   - Replace ambiguous return codes with custom exceptions
   - Introduce guard clauses to simplify branching
   - Add logging at error boundaries with actionable context
   - Update tests to cover error scenarios and contracts

3. **Required improvements**:
   - Create custom exception hierarchy (CalculatorError, InvalidInputError, etc.)
   - Add input validation to all functions
   - Replace None returns with specific exceptions
   - Add guard clauses to reduce nesting
   - Implement secure logging without data leakage
   - Write comprehensive error path tests

4. **Acceptance criteria**:
   - [ ] Tests pass and include error-path coverage (>= 2 new tests)
   - [ ] No bare except statements; custom exceptions used where appropriate
   - [ ] Logs include context (inputs or IDs) without leaking secrets
   - [ ] Code demonstrates EAFP vs LBYL principles

📚 **Reference the hardened implementation** in test_calculator_hardened.py to see
how each defensive programming principle is applied in practice.

💡 **Start with one function**: Pick add() or divide() and apply all defensive
programming principles before moving to the next function.
"""

import os
import sys

import pytest

# Add the tests directory to path so we can import calculator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import logging
from typing import Union

import pytest
from calculator import (
    Calculator,
    add,
    calculate_compound_interest,
    divide,
    factorial,
    multiply,
    percentage,
    power,
    safe_divide,
    square_root,
    subtract,
)

# Set up logging for demonstration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# =============================================================================
# DEFENSIVE PROGRAMMING IMPLEMENTATION: Custom Exception Hierarchy
# =============================================================================


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
    """Raised when mathematical constraints are violated."""

    pass


class BusinessRuleError(CalculatorError):
    """Raised when business rules are violated."""

    pass


# =============================================================================
# DEFENSIVE PROGRAMMING IMPLEMENTATION: Hardened Calculator Functions
# =============================================================================

Number = Union[int, float]


def safe_log_context(**kwargs):
    """Create safe logging context without sensitive data."""
    safe_context = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, float)) and abs(value) > 1000000:
            safe_context[key] = f"[LARGE_NUMBER:{type(value).__name__}]"
        else:
            safe_context[key] = value
    return safe_context


def hardened_add(a: Number, b: Number) -> Number:
    """Add two numbers with defensive programming.

    Preconditions:
    - Both a and b must be numeric types
    - Result must not overflow

    Postconditions:
    - Result is numeric
    - Result equals a + b
    """
    # Guard clause: Type validation
    if not isinstance(a, (int, float)):
        raise InvalidInputError(
            f"First operand must be a number, got {type(a).__name__}", input_value=a
        )

    if not isinstance(b, (int, float)):
        raise InvalidInputError(
            f"Second operand must be a number, got {type(b).__name__}", input_value=b
        )

    # Log operation with safe context
    context = safe_log_context(operation="add", a=a, b=b)
    logger.debug("Performing addition", extra=context)

    try:
        result = a + b

        # Postcondition: Check for overflow
        if isinstance(a, int) and isinstance(b, int):
            if abs(result) > 2**63 - 1:
                raise MathematicalError("Integer overflow detected")

        # Postcondition: Result type validation
        assert isinstance(result, (int, float)), "Result must be numeric"

        logger.debug("Addition completed successfully", extra={**context, "result": result})
        return result

    except Exception as e:
        logger.error(f"Addition failed: {e}", extra=context)
        raise


def hardened_divide(a: Number, b: Number) -> Number:
    """Divide a by b with comprehensive error handling.

    Preconditions:
    - Both a and b must be numeric types
    - b must not be zero

    Postconditions:
    - Result is numeric
    - Result * b ≈ a (within floating point precision)
    """
    # Guard clauses for input validation
    if not isinstance(a, (int, float)):
        raise InvalidInputError(f"Dividend must be a number, got {type(a).__name__}", input_value=a)

    if not isinstance(b, (int, float)):
        raise InvalidInputError(f"Divisor must be a number, got {type(b).__name__}", input_value=b)

    if b == 0:
        raise DivisionByZeroError(f"Cannot divide {a} by zero")

    # Log operation
    context = safe_log_context(operation="divide", dividend=a, divisor=b)
    logger.debug("Performing division", extra=context)

    try:
        result = a / b

        # Postcondition: Verify result
        if abs(b) > 1e-10:  # Avoid division by very small numbers in verification
            verification = abs(result * b - a)
            if verification > abs(a) * 1e-10:  # Relative error check
                logger.warning(f"Division result verification failed: {verification}")

        assert isinstance(result, (int, float)), "Division result must be numeric"

        logger.debug("Division completed successfully", extra={**context, "result": result})
        return result

    except Exception as e:
        logger.error(f"Division failed: {e}", extra=context)
        raise


def hardened_factorial(n: int) -> int:
    """Calculate factorial with contract enforcement.

    Preconditions:
    - n must be a non-negative integer
    - n must be <= 20 (to prevent excessive computation)

    Postconditions:
    - result >= 1
    - result == 1 for n == 0
    - result > n for n > 1
    """
    # Guard clause: Type validation
    if not isinstance(n, int):
        raise InvalidInputError(
            f"Factorial input must be an integer, got {type(n).__name__}", input_value=n
        )

    # Guard clause: Range validation
    if n < 0:
        raise MathematicalError(f"Factorial not defined for negative numbers: {n}")

    # Guard clause: Business rule validation
    if n > 20:
        raise BusinessRuleError(f"Factorial calculation limited to n <= 20, got {n}")

    context = safe_log_context(operation="factorial", n=n)
    logger.debug("Calculating factorial", extra=context)

    try:
        # Calculate factorial
        if n <= 1:
            result = 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i

        # Postcondition checks
        assert result >= 1, f"Factorial result must be >= 1, got {result}"

        if n == 0:
            assert result == 1, f"Factorial of 0 must be 1, got {result}"
        elif n > 1:
            assert result > n, f"Factorial of {n} must be > {n}, got {result}"

        logger.debug("Factorial calculation completed", extra={**context, "result": result})
        return result

    except Exception as e:
        logger.error(f"Factorial calculation failed: {e}", extra=context)
        raise


class HardenedCalculator:
    """Calculator class with comprehensive defensive programming."""

    def __init__(self):
        self.history = []
        self._max_history = 100

        # Operation mapping with validation
        self._operations = {
            "add": (hardened_add, 2, "addition"),
            "subtract": (self._subtract, 2, "subtraction"),
            "multiply": (self._multiply, 2, "multiplication"),
            "divide": (hardened_divide, 2, "division"),
            "factorial": (hardened_factorial, 1, "factorial"),
        }

    def _subtract(self, a: Number, b: Number) -> Number:
        """Subtraction with input validation."""
        return hardened_add(a, -b)  # Reuse addition logic

    def _multiply(self, a: Number, b: Number) -> Number:
        """Multiplication with overflow protection."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise InvalidInputError("Both operands must be numbers")

        # Check for potential overflow
        if isinstance(a, int) and isinstance(b, int):
            if abs(a) > 1e6 and abs(b) > 1e6:
                raise BusinessRuleError("Multiplication may cause overflow")

        return a * b

    def calculate(self, operation: str, *args) -> Number:
        """Perform calculation with comprehensive error handling.

        Preconditions:
        - operation must be a valid operation name
        - args must match expected number for operation

        Postconditions:
        - result is stored in history
        - history size doesn't exceed maximum
        """
        # Guard clause: Operation validation
        if not isinstance(operation, str):
            raise InvalidInputError(
                f"Operation must be a string, got {type(operation).__name__}", input_value=operation
            )

        if operation not in self._operations:
            available_ops = ", ".join(self._operations.keys())
            raise InvalidInputError(
                f"Unknown operation '{operation}'. Available: {available_ops}",
                input_value=operation,
            )

        func, expected_args, operation_name = self._operations[operation]

        # Guard clause: Argument count validation
        if len(args) != expected_args:
            raise InvalidInputError(
                f"Operation '{operation}' requires {expected_args} arguments, got {len(args)}",
                input_value=args,
            )

        # Log calculation attempt
        context = safe_log_context(operation=operation, args=args, history_size=len(self.history))
        logger.info(f"Starting {operation_name} calculation", extra=context)

        try:
            # Perform calculation
            result = func(*args)

            # Store in history with size management
            if len(args) == 1:
                history_entry = f"{operation}({args[0]}) = {result}"
            else:
                history_entry = f"{operation}({', '.join(map(str, args))}) = {result}"

            self._add_to_history(history_entry)

            logger.info(
                f"{operation_name} calculation successful", extra={**context, "result": result}
            )
            return result

        except CalculatorError:
            # Re-raise calculator-specific errors
            logger.warning(f"{operation_name} calculation failed with known error", extra=context)
            raise
        except Exception as e:
            # Wrap unexpected errors
            logger.error(f"Unexpected error in {operation_name}: {e}", extra=context, exc_info=True)
            raise CalculatorError(f"Calculation failed unexpectedly: {e}") from e

    def _add_to_history(self, entry: str) -> None:
        """Add entry to history with size management."""
        self.history.append(entry)

        # Enforce maximum history size
        if len(self.history) > self._max_history:
            self.history = self.history[-self._max_history :]

    def get_history(self) -> list:
        """Get calculation history."""
        return self.history.copy()  # Return copy to prevent external modification

    def clear_history(self) -> None:
        """Clear calculation history."""
        logger.info(f"Clearing calculation history ({len(self.history)} entries)")
        self.history.clear()


# =============================================================================
# DEFENSIVE PROGRAMMING TESTS: Error Path and Contract Testing
# =============================================================================


class TestHardenedCalculator:
    """Comprehensive tests for defensive programming implementation."""

    def test_addition_input_validation(self):
        """Test addition input validation with specific error types."""
        with pytest.raises(InvalidInputError, match="First operand must be a number"):
            hardened_add("not_a_number", 5)

        with pytest.raises(InvalidInputError, match="Second operand must be a number"):
            hardened_add(5, None)

    def test_division_by_zero(self):
        """Test division by zero raises specific exception."""
        with pytest.raises(DivisionByZeroError, match="Cannot divide 10 by zero"):
            hardened_divide(10, 0)

    def test_factorial_contract_validation(self):
        """Test factorial precondition and postcondition enforcement."""
        # Test negative input (precondition violation)
        with pytest.raises(MathematicalError, match="not defined for negative"):
            hardened_factorial(-1)

        # Test non-integer input (precondition violation)
        with pytest.raises(InvalidInputError, match="must be an integer"):
            hardened_factorial(5.5)

        # Test business rule violation
        with pytest.raises(BusinessRuleError, match="limited to n <= 20"):
            hardened_factorial(25)

        # Test valid inputs and postconditions
        assert hardened_factorial(0) == 1  # Postcondition: factorial(0) == 1
        assert hardened_factorial(5) == 120  # Postcondition: result > n for n > 1

    def test_calculator_operation_validation(self):
        """Test calculator operation validation."""
        calc = HardenedCalculator()

        # Test unknown operation
        with pytest.raises(InvalidInputError, match="Unknown operation"):
            calc.calculate("unknown_op", 1, 2)

        # Test wrong argument count
        with pytest.raises(InvalidInputError, match="requires 2 arguments, got 1"):
            calc.calculate("add", 5)

        with pytest.raises(InvalidInputError, match="requires 1 arguments, got 2"):
            calc.calculate("factorial", 5, 3)

    def test_error_context_preservation(self):
        """Test that errors include helpful context."""
        try:
            hardened_add("invalid", 5)
        except InvalidInputError as e:
            assert e.input_value == "invalid"
            assert "First operand must be a number" in str(e)

    def test_calculator_history_management(self):
        """Test history functionality and size limits."""
        calc = HardenedCalculator()

        # Add some calculations
        calc.calculate("add", 2, 3)
        calc.calculate("factorial", 5)

        history = calc.get_history()
        assert len(history) == 2
        assert "add(2, 3) = 5" in history[0]
        assert "factorial(5) = 120" in history[1]

        # Test history clearing
        calc.clear_history()
        assert len(calc.get_history()) == 0

    def test_successful_operations(self):
        """Test that valid operations work correctly."""
        calc = HardenedCalculator()

        # Test basic operations
        assert calc.calculate("add", 2, 3) == 5
        assert calc.calculate("subtract", 10, 4) == 6
        assert calc.calculate("multiply", 3, 4) == 12
        assert calc.calculate("divide", 15, 3) == 5
        assert calc.calculate("factorial", 4) == 24

    def test_postcondition_verification(self):
        """Test postcondition checks are enforced."""
        # Test division postcondition (result * divisor ≈ dividend)
        result = hardened_divide(10, 3)
        assert abs(result * 3 - 10) < 1e-10

        # Test factorial postconditions
        result = hardened_factorial(5)
        assert result >= 1  # Must be >= 1
        assert result > 5  # Must be > n for n > 1


class TestContractViolations:
    """Test contract violations and edge cases."""

    def test_overflow_protection(self):
        """Test overflow protection in operations."""
        calc = HardenedCalculator()

        # Test multiplication overflow protection
        with pytest.raises(BusinessRuleError, match="may cause overflow"):
            calc.calculate("multiply", 2000000, 2000000)

    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        calc = HardenedCalculator()

        # Test very small numbers
        result = calc.calculate("add", 1e-10, 1e-10)
        assert result == 2e-10

        # Test zero operations
        assert calc.calculate("add", 0, 0) == 0
        assert calc.calculate("multiply", 0, 100) == 0

        # Test boundary factorial values
        assert calc.calculate("factorial", 0) == 1
        assert calc.calculate("factorial", 1) == 1
        assert calc.calculate("factorial", 20) > 1000  # Large but valid


# =============================================================================
# DEMONSTRATION: Run tests to show defensive programming in action
# =============================================================================

if __name__ == "__main__":
    # Run some demonstrations
    print("=== Defensive Programming Calculator Demo ===\n")

    calc = HardenedCalculator()

    # Successful operations
    print("✅ Successful operations:")
    print(f"5 + 3 = {calc.calculate('add', 5, 3)}")
    print(f"factorial(5) = {calc.calculate('factorial', 5)}")

    # Error handling demonstrations
    print("\n❌ Error handling demonstrations:")

    try:
        calc.calculate("add", "not_a_number", 5)
    except InvalidInputError as e:
        print(f"Input validation: {e}")

    try:
        calc.calculate("divide", 10, 0)
    except DivisionByZeroError as e:
        print(f"Division by zero: {e}")

    try:
        calc.calculate("factorial", -1)
    except MathematicalError as e:
        print(f"Mathematical constraint: {e}")

    try:
        calc.calculate("factorial", 25)
    except BusinessRuleError as e:
        print(f"Business rule violation: {e}")

    print(f"\n📊 History: {calc.get_history()}")
    print("\n=== Demo Complete ===")


class TestBasicOperations:
    """Test basic calculator operations."""

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert add(2, 3) == 5
        assert add(0, 5) == 5

    def test_subtract_numbers(self):
        """Test subtraction."""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5

    def test_multiply_numbers(self):
        """Test multiplication."""
        assert multiply(3, 4) == 12
        assert multiply(0, 5) == 0

    def test_divide_valid_numbers(self):
        """Test division with valid inputs."""
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_returns_none(self):
        """Test that division by zero returns None (should be exception)."""
        # TODO: Update this test when you implement proper exception handling
        assert divide(10, 0) is None

    # TODO: Add tests for invalid input types
    # TODO: Add tests for contract violations
    # TODO: Add tests for edge cases


class TestAdvancedOperations:
    """Test advanced calculator operations."""

    def test_power_operation(self):
        """Test power operation."""
        assert power(2, 3) == 8
        assert power(5, 0) == 1

    def test_square_root_positive(self):
        """Test square root of positive numbers."""
        assert square_root(9) == 3
        assert square_root(16) == 4

    def test_square_root_negative_returns_error(self):
        """Test square root of negative returns error code."""
        # TODO: Update this test when you implement proper exception handling
        assert square_root(-4) == -1

    def test_factorial_valid(self):
        """Test factorial with valid inputs."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120

    def test_factorial_negative_returns_error(self):
        """Test factorial of negative returns error code."""
        # TODO: Update this test when you implement proper exception handling
        assert factorial(-1) == -1

    # TODO: Add more comprehensive error tests
    # TODO: Add boundary condition tests
    # TODO: Add performance tests for large numbers


class TestCalculatorClass:
    """Test the Calculator class."""

    def test_calculator_initialization(self):
        """Test calculator initializes with empty history."""
        calc = Calculator()
        assert calc.get_history() == []

    def test_calculator_add_operation(self):
        """Test calculator performs addition."""
        calc = Calculator()
        result = calc.calculate("add", 2, 3)
        assert result == 5

    def test_calculator_stores_history(self):
        """Test calculator stores operation history."""
        calc = Calculator()
        calc.calculate("add", 2, 3)
        history = calc.get_history()
        assert len(history) == 1
        assert "add(2, 3) = 5" in history[0]

    def test_calculator_unknown_operation(self):
        """Test calculator handles unknown operations."""
        calc = Calculator()
        result = calc.calculate("unknown", 2, 3)
        # TODO: Update when you implement proper exception handling
        assert "ERROR" in str(result)

    # TODO: Add tests for missing operands
    # TODO: Add tests for invalid input types
    # TODO: Add tests for history management
    # TODO: Add tests for error recovery


class TestSafeDivide:
    """Test the safe_divide function."""

    def test_safe_divide_empty_list(self):
        """Test safe_divide with empty list."""
        assert safe_divide([]) == 0

    def test_safe_divide_single_number(self):
        """Test safe_divide with single number."""
        assert safe_divide([10]) == 10

    def test_safe_divide_multiple_numbers(self):
        """Test safe_divide with multiple numbers."""
        assert safe_divide([10, 2, 5]) == 1.0

    def test_safe_divide_with_zero(self):
        """Test safe_divide when division by zero occurs."""
        # TODO: Update when you implement proper exception handling
        assert safe_divide([10, 2, 0]) is None

    # TODO: Add tests for invalid input types
    # TODO: Add tests for contract violations


class TestCompoundInterest:
    """Test compound interest calculation."""

    def test_compound_interest_annual(self):
        """Test compound interest with annual compounding."""
        result = calculate_compound_interest(1000, 0.05, 2, 1)
        expected = 1000 * (1.05) ** 2
        assert abs(result - expected) < 0.01

    def test_compound_interest_monthly(self):
        """Test compound interest with monthly compounding."""
        result = calculate_compound_interest(1000, 0.12, 1, 12)
        expected = 1000 * (1 + 0.12 / 12) ** 12
        assert abs(result - expected) < 0.01

    # TODO: Add tests for invalid inputs (negative values, etc.)
    # TODO: Add tests for edge cases
    # TODO: Add tests for contract violations


# TODO: Add error path test class
class TestErrorPaths:
    """Test error handling and edge cases."""

    # TODO: Add comprehensive error tests here
    pass


# TODO: Add contract validation test class
class TestContractValidation:
    """Test contract preconditions and postconditions."""

    # TODO: Add contract validation tests here
    pass


# TODO: Add performance test class
class TestPerformance:
    """Test performance characteristics and edge cases."""

    # TODO: Add performance tests here
    pass
