# 0x03. Unittests and Integration Tests

## Description

This project involves learning and implementing unit tests and integration tests in Python. The primary focus is on testing various functions and methods, ensuring code reliability and correctness by using different testing strategies such as mocking, parameterization, and fixtures.

## Learning Objectives

By the end of this project, you should be able to:

- Understand the difference between unit tests and integration tests.
- Implement common testing patterns such as mocking, parameterizations, and fixtures.
- Write and run tests using the `unittest` framework.
- Mock external dependencies to isolate the functionality being tested.

## Project Requirements

- All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files end with a new line.
- The first line of all Python files should be `#!/usr/bin/env python3`.
- Code adheres to the `pycodestyle` style (version 2.5).
- All files must be executable.
- Modules, classes, and functions must have documentation.
- All functions and coroutines must be type-annotated.

## Project Structure

- `utils.py`: Contains utility functions to be tested.
- `client.py`: Contains the `GithubOrgClient` class which interacts with the GitHub API.
- `fixtures.py`: Contains fixture data for integration tests.
- `test_utils.py`: Contains unit tests for the functions in `utils.py`.
- `test_client.py`: Contains unit and integration tests for the `GithubOrgClient` class.
- `README.md`: Project documentation.

## Tasks

### Task 0: Parameterize a Unit Test

Write unit tests for the `utils.access_nested_map` function using parameterized inputs.

### Task 1: Parameterize a Unit Test for Exceptions

Extend unit tests for `utils.access_nested_map` to handle exceptions using parameterized inputs.

### Task 2: Mock HTTP Calls

Write unit tests for `utils.get_json` function, mocking external HTTP calls.

### Task 3: Parameterize and Patch

Write unit tests for `utils.memoize` decorator, ensuring methods are only called once when memoized.

### Task 4: Parameterize and Patch as Decorators

Write unit tests for the `GithubOrgClient.org` method, ensuring correct parameterized input handling and HTTP call mocking.

### Task 5: Mocking a Property

Write unit tests for the `_public_repos_url` property in `GithubOrgClient`, mocking external dependencies.

### Task 6: More Patching

Write unit tests for the `GithubOrgClient.public_repos` method, mocking external calls and properties.

### Task 7: Parameterize

Write unit tests for the `GithubOrgClient.has_license` method using parameterized inputs.

### Task 8: Integration Test: Fixtures

Write integration tests for `GithubOrgClient.public_repos` method, using fixtures for setup and teardown.

### Task 9: Integration Tests

Extend integration tests to include testing of `public_repos` with specific licenses.

## How to Run Tests

To run the tests, use the following command:
```sh
$ python -m unittest path/to/test_file.py
```

For example, to run tests in `test_utils.py`, use:
```sh
$ python -m unittest test_utils.py
```

## Resources

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Author

This project was created as part of the ALX Backend Python curriculum.
```
