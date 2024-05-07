#!/usr/bin/env python3
import asyncio
import importlib  # Use `importlib` for dynamic import
import sys

sys.path.append('.')  # Ensure the current directory is in `sys.path`

# Import the module dynamically
module_name = "1-concurrent_coroutines"
imported_module = importlib.import_module(module_name)

# Get the `wait_n` function
wait_n = imported_module.wait_n

# Test `wait_n` with different inputs
print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
