#!/usr/bin/env python3
"""
Module for a function that returns a tuple with a string .
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of the given int/float."""
    return k, float(v * v)
