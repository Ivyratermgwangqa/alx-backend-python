#!/usr/bin/env python3
"""
Module that measures the execution time of `wait_n`.
"""
import time
import asyncio
import importlib

# Dynamically import the module with `importlib`
module_name = '1-concurrent_coroutines'
imported_module = importlib.import_module(module_name)

# Get the `wait_n` function from the imported module
wait_n = imported_module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
