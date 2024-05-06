#!/usr/bin/env python3
"""
Module to measure execution time of concurrent coroutines
"""
import time
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for `wait_n(n, max_delay)`.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
