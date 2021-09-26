# task 3_1 by Peregud Kirill

import math

DOWN_RANGE = 3
UP_RANGE = 21
result = None

print(
"""
-------
The program calculates the difference between the two entered arguments,
if they are numbers in the range from 3 to 21,
and adds the arguments as strings, otherwise.
-------
"""
)

first_arg = input("Please, enter a first argument:\n")
second_arg = input("\nPlease, enter a second argument:\n")

try:
    first_int = int(first_arg)
    second_int = int(second_arg)
except:
    try:
        first_float = float(first_arg)
        second_float = float(second_arg)
    except:
        result = first_arg + second_arg
    else:
        if (DOWN_RANGE <= first_float <= UP_RANGE) and (DOWN_RANGE <= second_float <= UP_RANGE):
            result = abs(first_float - second_float)
else:
    if (DOWN_RANGE <= first_int <= UP_RANGE) and (DOWN_RANGE <= second_int <= UP_RANGE):
        result = abs(first_int - second_int)
    else:
        result = first_arg + second_arg

if result is None:
    result = first_arg + second_arg

print(f'Operation result: {result}')
