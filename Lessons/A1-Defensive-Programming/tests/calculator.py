"""
Calculator module for defensive programming practice.

This module implements basic calculator operations but lacks proper
error handling, contracts, and defensive programming patterns.

Your task: Harden this module by applying defensive programming principles.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        return None  # TODO: Replace with proper exception
    return a / b


def power(base, exponent):
    """Raise base to the power of exponent."""
    return base**exponent


def square_root(number):
    """Calculate square root of a number."""
    if number < 0:
        return -1  # TODO: Replace with proper exception
    return number**0.5


def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        return -1  # TODO: Replace with proper exception
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def percentage(part, whole):
    """Calculate what percentage 'part' is of 'whole'."""
    if whole == 0:
        return None  # TODO: Replace with proper exception
    return (part / whole) * 100


class Calculator:
    """A simple calculator class."""

    def __init__(self):
        self.history = []

    def calculate(self, operation, a, b=None):
        """
        Perform a calculation.

        Args:
            operation: String name of operation
            a: First operand
            b: Second operand (optional for unary operations)

        Returns:
            Result of calculation or error code
        """
        if operation == "add":
            if b is None:
                return "ERROR: Missing operand"
            result = add(a, b)
        elif operation == "subtract":
            if b is None:
                return "ERROR: Missing operand"
            result = subtract(a, b)
        elif operation == "multiply":
            if b is None:
                return "ERROR: Missing operand"
            result = multiply(a, b)
        elif operation == "divide":
            if b is None:
                return "ERROR: Missing operand"
            result = divide(a, b)
            if result is None:
                return "ERROR: Division by zero"
        elif operation == "power":
            if b is None:
                return "ERROR: Missing operand"
            result = power(a, b)
        elif operation == "sqrt":
            result = square_root(a)
            if result == -1:
                return "ERROR: Cannot calculate square root of negative number"
        elif operation == "factorial":
            result = factorial(a)
            if result == -1:
                return "ERROR: Factorial not defined for negative numbers"
        else:
            return "ERROR: Unknown operation"

        # Store in history
        if b is None:
            calculation = f"{operation}({a}) = {result}"
        else:
            calculation = f"{operation}({a}, {b}) = {result}"

        self.history.append(calculation)
        return result

    def get_history(self):
        """Get calculation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []


def safe_divide(numbers):
    """
    Divide a list of numbers in sequence.

    Example: safe_divide([10, 2, 5]) = ((10 / 2) / 5) = 1.0
    """
    if not numbers:
        return 0

    if len(numbers) == 1:
        return numbers[0]

    result = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] == 0:
            return None  # TODO: Replace with proper exception
        result = result / numbers[i]

    return result


def calculate_compound_interest(principal, rate, time, compounds_per_year=1):
    """
    Calculate compound interest.

    Formula: A = P(1 + r/n)^(nt)
    Where:
        P = principal amount
        r = annual interest rate (as decimal)
        t = time in years
        n = number of times interest compounds per year
    """
    # TODO: Add input validation and error handling
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    return amount


if __name__ == "__main__":
    # Simple test cases
    calc = Calculator()

    print("Testing calculator...")
    print(f"2 + 3 = {calc.calculate('add', 2, 3)}")
    print(f"10 / 0 = {calc.calculate('divide', 10, 0)}")
    print(f"sqrt(-4) = {calc.calculate('sqrt', -4)}")
    print(f"factorial(-1) = {calc.calculate('factorial', -1)}")

    print("\\nHistory:")
    for entry in calc.get_history():
        print(f"  {entry}")
