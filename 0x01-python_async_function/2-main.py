#!/usr/bin/env python3
import importlib
import sys
import time

# Ensure the current directory is in sys.path
sys.path.append('.')

# Use importlib to import the module with a string
module_name = "2-measure_runtime"
imported_module = importlib.import_module(module_name)

# Access the measure_time function from the imported module
measure_time = imported_module.measure_time

print(measure_time(5, 9))
