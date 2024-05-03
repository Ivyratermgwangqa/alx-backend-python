#!/usr/bin/env python3
"""
Module for a function that returns the sum of a list containing integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list containing integers and floats."""
    return sum(mxd_lst)
