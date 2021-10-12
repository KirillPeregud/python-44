# task №6_1 by Kirill Peregud

import math

print(
"""
----------
The program performs operations on complex numbers ('+', '-', '*', '==', '/')
and finds the module ('| |') of a complex number.
----------
"""
)

DOWN_RANGE = -50
UP_RANGE = 50
operation = ('+', '-', '*', '/', '==', '||')


class Complex:

    def __init__(self, x, y):
        self.re = x
        self.im = y

    def __add__(self, right):
        return Complex(self.re + right.re, self.im + right.im)

    def __sub__(self, right):
        return Complex(self.re - right.re, self.im - right.im)

    def __mul__(self, right):
        return Complex(self.re * right.re - self.im * right.im, self.re * right.im + right.re * self.im)

    def __truediv__(self, right):
        self.fi = math.atan2(self.im, self.re)
        right.fi = math.atan2(right.im, right.re)
        r = abs(self) / abs(right)
        return Complex(round(r * math.cos(self.fi - right.fi), 2), round(r * math.sin(self.fi - right.fi), 2))

    def __abs__(self):
        return round(pow(self.re ** 2 + self.im ** 2, 0.5), 2)

    def __eq__(self, right):
        return self.re == right.re and self.im == right.im

    def __repr__(self):
        return f'{self.re} + ({self.im})*i'


def enter_argument(name_arg):
    enter_arg = False
    while enter_arg is not True:
        try:
            value_arg = int(
                input(f'Please, enter a {name_arg} from {DOWN_RANGE} to {UP_RANGE}:\n')
                )
        except:
            print('Unfortunately, the argument is not an integer number :(\n')
        else:
            if value_arg in range(DOWN_RANGE, UP_RANGE + 1):
                enter_arg = True
            else:
                print(
                    f'Sorry, the {name_arg} is not in the range from {DOWN_RANGE} to {UP_RANGE}...\n'
                    )
    return value_arg


def basic_operations():
    print('----------')
    print('Enter the first complex number:\n')
    z1 = Complex(enter_argument('real part'), enter_argument('imaginary part'))
    print('----------')
    print('Enter the second complex number:\n')
    z2 = Complex(enter_argument('real part'), enter_argument('imaginary part'))
    return z1, z2


def find_module():
    print('Enter the complex number:\n')
    z = Complex(enter_argument('real part'), enter_argument('imaginary part'))
    return z


def print_result(z1, operation, z2, result):
    print('----------')
    print(f'Calculation result: ({z1}) {operation} ({z2}) = {result}')
    print('----------')


# Start of the program
operation_arg = input(
        'Please, enter operation on complex numbers: "+", "-", "*", "/", "==" or "||" (module)\n'
        )
        
while  operation_arg not in operation:
    print('----------')
    print('Oh, incorrect input :(')
    print('----------')
    operation_arg = input(
        'Please, enter operation on complex numbers: "+", "-", "*", "/", "==" or "||" (module)\n'
        )

if operation_arg == operation[0]:
    z1, z2 = basic_operations()
    print_result(z1, operation[0], z2, z1 + z2)

elif operation_arg == operation[1]:
    z1, z2 = basic_operations()
    print_result(z1, operation[1], z2, z1 - z2)

elif operation_arg == operation[2]:
    z1, z2 = basic_operations()
    print_result(z1, operation[2], z2, z1 * z2)

elif operation_arg == operation[3]:
    z1, z2 = basic_operations()
    print_result(z1, operation[3], z2, z1 / z2)

elif operation_arg == operation[4]:
    z1, z2 = basic_operations()
    print('----------')
    if (z1 == z2):
        print(f'Calculation result: ({z1}) {operation_arg} ({z2}) -> True')
    else:
        print(f'Calculation result: ({z1}) != ({z2}) -> False')
    print('----------')

elif operation_arg == operation[5]:
    z = find_module()
    result = abs(z)
    print('----------')
    print(f'Calculation result: |{z}| = {result}')
    print('----------')
