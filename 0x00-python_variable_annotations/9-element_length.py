#!/usr/bin/env python3
"""
Module for a function that returns the length of each element in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing an element and its length."""
    return [(i, len(i)) for i in lst]
