#!/usr/bin/env python3
"""
Module for a function that safely retrieves a value from a dictionary.
"""

from typing import Mapping, TypeVar, Union, Any

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)
-> Union[Any, T]:

    
    """Return the value for a key in a dictionary, or the default value"""
    if key in dct:
        return dct[key]
    else:
        return default
