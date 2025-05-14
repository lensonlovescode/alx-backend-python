#!/usr/bin/env python3
"""
contains a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies a float
by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a callable
    """
    def multiply(k: float) -> float:
        """
        the callable
        """
        return multiplier * k
    return multiply
