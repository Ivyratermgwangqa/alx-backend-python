#!/usr/bin/env python3
"""
Test script for task_wait_n function.
"""
import importlib
import asyncio
import sys

# Ensure the current directory is in `sys.path`
sys.path.append('.')

# Use `importlib` to import `4-tasks`
module_name = "4-tasks"
imported_module = importlib.import_module(module_name)

# Get `task_wait_n` from the imported module
task_wait_n = imported_module.task_wait_n

# Test with 5 tasks and a maximum delay of 6 seconds
n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
