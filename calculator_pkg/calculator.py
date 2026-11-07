"""Calculator module providing basic arithmetic operations.

Functions:
- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)

All functions accept real-number inputs and return float results. The divide
function raises ZeroDivisionError when the divisor is zero.
"""
from typing import Union
from numbers import Real

Number = Real


def add(a: Number, b: Number) -> float:
    """Return the sum of a and b.

    Args:
        a: First addend (number).
        b: Second addend (number).

    Returns:
        float: The sum a + b.
    """
    return float(a + b)


def subtract(a: Number, b: Number) -> float:
    """Return the result of subtracting b from a.

    Args:
        a: Minuend (number).
        b: Subtrahend (number).

    Returns:
        float: The difference a - b.
    """
    return float(a - b)


def multiply(a: Number, b: Number) -> float:
    """Return the product of a and b.

    Args:
        a: First factor (number).
        b: Second factor (number).

    Returns:
        float: The product a * b.
    """
    return float(a * b)


def divide(a: Number, b: Number) -> float:
    """Return the quotient of a divided by b.

    Args:
        a: Dividend (number).
        b: Divisor (number).

    Returns:
        float: The quotient a / b.

    Raises:
        ZeroDivisionError: If ``b`` is zero.
    """
    # Strict zero check covers int/float/Real types.
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return float(a / b)
