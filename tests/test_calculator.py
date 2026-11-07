import pytest

from calculator_pkg import add, subtract, multiply, divide


def test_add_integers():
    assert add(2, 3) == 5.0


def test_add_floats():
    assert add(2.5, 1.25) == pytest.approx(3.75)


def test_subtract():
    assert subtract(10, 4) == 6.0
    assert subtract(2.5, 0.5) == pytest.approx(2.0)


def test_multiply():
    assert multiply(3, 5) == 15.0
    assert multiply(2.5, 4) == pytest.approx(10.0)


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7.5, 2.5) == pytest.approx(3.0)


def test_divide_negative_and_float():
    assert divide(-6, 2) == -3.0
    assert divide(5, 2) == pytest.approx(2.5)


def test_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError) as exc:
        divide(5, 0)
    assert "Division by zero" in str(exc.value)
