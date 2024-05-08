#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine to collect random numbers.

The `async_comprehension` coroutine collects 10 random numbers using
an asynchronous comprehension over the `async_generator` coroutine from
the previous module.
"""

import asyncio
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension"""
    return [i async for i in async_generator()]
