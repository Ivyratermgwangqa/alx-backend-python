#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import sys
sys.path.append('.')

from 2-measure_runtime import measure_time

print(measure_time(5, 9))
