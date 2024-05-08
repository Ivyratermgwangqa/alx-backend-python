# 0x02. Python - Async Comprehension
# Python Asynchronous Comprehension Project

This project demonstrates the use of asynchronous comprehensions and generators in Python. It covers several key concepts, including asynchronous coroutines, generators, and the measurement of runtime for parallel asynchronous operations.

## Project Structure

The project consists of three main Python files, each implementing different functionalities:

1. **0-async_generator.py**:
   - Defines an asynchronous generator coroutine `async_generator` that loops 10 times, waits for 1 second asynchronously in each loop, and yields a random number between 0 and 10.
   - This file demonstrates basic asynchronous behavior using coroutines and generators.

2. **1-async_comprehension.py**:
   - Defines an asynchronous coroutine `async_comprehension` that collects 10 random numbers using an asynchronous comprehension over `async_generator`.
   - This module shows how asynchronous comprehensions work and their potential applications.

3. **2-measure_runtime.py**:
   - Contains a coroutine `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`. It measures the total runtime and returns it.
   - This module demonstrates parallel execution of asynchronous tasks and how to measure their runtime.

## Usage

To run the code in this project, you can use Python's `asyncio.run()` function to execute the asynchronous coroutines. Below are some examples of how to run and test each module:

### 0-async_generator.py

```bash
python3 0-async_generator.py
```

### 1-async_comprehension.py

```bash
python3 1-async_comprehension.py
```

### 2-measure_runtime.py

```bash
python3 2-measure_runtime.py
```

## Requirements

- Python 3.7 or later
- Basic understanding of asynchronous programming in Python
- `asyncio` module for running asynchronous code
- `random` module for generating random numbers

## Further Information

For more information about asynchronous comprehensions and generators in Python, check out:
- [PEP 530 - Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [Python Official Documentation](https://docs.python.org/3/library/asyncio.html)
```
