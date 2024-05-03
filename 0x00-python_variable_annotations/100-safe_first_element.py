#!/usr/bin/env python3
"""
Module for a function that safely returns the first element in a sequence.
"""

from typing import Sequence, Union, Any

def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """Return the first element in a sequence or None if it's empty."""
    if lst:
        return lst[0]
    else:
        return None
