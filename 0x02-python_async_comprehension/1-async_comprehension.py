#!/usr/bin/env python3
"""
This module demonstrates the use of asynchronous comprehensions in Python.
"""

import asyncio
from typing import List
import importlib  # Dynamic import to handle module names with dashes

# Importing the `async_generator` coroutine
async_generator = importlib.import_module("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension"""
    return [i async for i in async_generator()]
