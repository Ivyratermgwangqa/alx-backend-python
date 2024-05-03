# Python Variable Annotations

## Overview
This project demonstrates the use of type annotations in Python to specify variable types, function signatures, and more. It covers basic and complex types, duck typing, and how to validate code with type-checking tools like mypy.

## Requirements
- Python 3.7 or later
- Ubuntu 18.04 LTS (or a similar environment)
- PEP 8 (pycodestyle) for code styling
- Mypy for type checking

## Project Structure
The project is structured into multiple tasks, each addressing different concepts related to type annotations. Here is a list of the tasks and their brief descriptions:

- **Task 0: Basic Annotations - `add`**  
  A function that adds two float numbers and returns the result.

- **Task 1: Basic Annotations - `concat`**  
  A function that concatenates two strings.

- **Task 2: Basic Annotations - `floor`**  
  A function that returns the floor of a float.

- **Task 3: Basic Annotations - `to_str`**  
  A function that converts a float to its string representation.

- **Task 4: Define Variables**  
  A set of annotated variable definitions with specific values.

- **Task 5: Complex Types - List of Floats**  
  A function that returns the sum of a list of floats.

- **Task 6: Complex Types - Mixed List**  
  A function that returns the sum of a list containing integers and floats.

- **Task 7: Complex Types - String and Int/Float to Tuple**  
  A function that returns a tuple with a string and the square of an int/float.

- **Task 8: Complex Types - Functions**  
  A function that returns a function to multiply a float by a given multiplier.

- **Task 9: Duck Typing - Iterable Object**  
  A function that returns a list of tuples containing an element and its length.

- **Task 10: Duck Typing - First Element of a Sequence**  
  A function that safely returns the first element of a sequence or `None` if the sequence is empty.

- **Task 11: More Involved Type Annotations**  
  A function that safely retrieves a value from a dictionary, with a default fallback.

- **Task 12: Type Checking**  
  A function that creates a list with each item from a tuple repeated a given number of times.

## Running the Project
To run the project and test the functions:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd 0x00-python_variable_annotations
   ```

3. Execute each task's corresponding test script to validate the implementations:
   ```bash
   ./0-main.py
   ./1-main.py
   # Repeat for each test script
   ```

## Type Checking with Mypy
To validate the code with mypy, you can use the following command to check for type inconsistencies:
```bash
mypy .
```

This command will analyze the code and report any type-related issues.

## Contributions
Contributions to this project are welcome. If you find a bug or have suggestions for improvement, please open an issue or submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License. For more information, see the LICENSE file.
```
