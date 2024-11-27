#!/usr/bin/python3
"""Defines an addition function."""


def add_integer(a, b=98):
    """Return the addition of a and b.
    Float arguments are casted to int before addition is performed.
    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
