# Python Asynchronous Programming

This project involves asynchronous programming in Python, focusing on coroutines, asyncio, and related concepts. The project consists of several tasks, each designed to teach or reinforce a specific concept in asynchronous programming.

## Tasks Overview

### Task 0: The Basics of Async
- **File**: `0-basic_async_syntax.py`
- **Description**: This task introduces asynchronous coroutines. It defines a coroutine `wait_random` that waits for a random delay between 0 and a given `max_delay` (inclusive), then returns the delay as a float.

### Task 1: Concurrent Coroutines
- **File**: `1-concurrent_coroutines.py`
- **Description**: This task introduces running multiple coroutines concurrently. It defines `wait_n`, an asynchronous function that spawns `n` instances of `wait_random` with a given `max_delay`. The function returns a list of delays in ascending order, without using the `sort()` function.

### Task 2: Measure the Runtime
- **File**: `2-measure_runtime.py`
- **Description**: This task focuses on measuring the execution time for asynchronous operations. The `measure_time` function measures the total execution time for `wait_n(n, max_delay)` and returns the average time per coroutine execution.

### Task 3: Tasks
- **File**: `3-tasks.py`
- **Description**: This task introduces asyncio tasks. It defines `task_wait_random`, a regular function (not a coroutine) that returns an `asyncio.Task` wrapping `wait_random`.

### Task 4: Tasks with Concurrency
- **File**: `4-tasks.py`
- **Description**: This task extends `wait_n` to use asyncio tasks instead of direct coroutines. The `task_wait_n` function creates `n` tasks with `task_wait_random(max_delay)`, gathers them asynchronously, and returns the sorted list of delays.

## Usage
To execute the tasks, ensure Python 3.7 or higher is installed. Make the files executable and run them to test the functionality. Example usage:

```bash
chmod +x *.py  # Make all Python files executable

# Run main files to test the implementation
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
```

## Notes
Ensure that each function and module has proper documentation. Type annotations are required for all functions and coroutines. Additionally, ensure code adheres to PEP 8 (Python style guide). For concurrency, asyncio should be used appropriately to manage asynchronous operations.
```
