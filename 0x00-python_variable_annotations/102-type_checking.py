#!/usr/bin/env python3
"""
Module for a function that returns a list with elements from a tuple repeated a given number of times.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list with each item in the tuple repeated a given number of times."""
    return [
        item 
        for item in lst
        for _ in range(factor)
    ]
