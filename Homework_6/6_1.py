# task №6_1 by Kirill Peregud

print(
"""
----------
The program performs operations on complex numbers ('+', '-', '*', '/')
and finds the module of a complex number.
----------
"""
)

DOWN_RANGE = -50
UP_RANGE = 50
operation = ('+', '-', '*', '/', '||')


class Complex:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self, compl):
        result = (self.x + compl.x) + (self.y + compl.y) * 1j
        return result

    def subtraction(self, compl):
        result = (self.x - compl.x) + (self.y - compl.y) * 1j
        return result

    def multiplication(self, compl):
        result = (self.x * compl.x - self.y * compl.y) + (self.x * compl.y + compl.x * self.y) * 1j
        return result

    def division(self, compl):
        denom = compl.x ** 2 + compl.y ** 2
        result = (self.x * compl.x + self.y * compl.y) / denom + 1j * (compl.x * self.y - self.x * compl.y) / denom
        return result

    def module(self):
        return pow(self.x ** 2 + self.y ** 2, 0.5)

    def print_complex(self):
        return self.x + self.y * 1j


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


operation_arg = input(
        'Please, enter operation on complex numbers: "+", "-", "*", "/" or "||" (module)\n'
        )
        
while  operation_arg not in operation:
    print('----------')
    print('Oh, incorrect input :(')
    print('----------')
    operation_arg = input(
        'Please, enter operation on complex numbers: "+", "-", "*", "/" or "||" (module)\n'
        )

if operation_arg == operation[0]:
    z1, z2 = basic_operations()
    result = z1.addition(z2)

elif operation_arg == operation[1]:
    z1, z2 = basic_operations()
    result = z1.subtraction(z2)

elif operation_arg == operation[2]:
    z1, z2 = basic_operations()
    result = z1.multiplication(z2)

elif operation_arg == operation[3]:
    z1, z2 = basic_operations()
    result = z1.division(z2)

elif operation_arg == operation[4]:
    z = find_module()
    print('----------')
    print(f'Calculation result: |{z.print_complex()}| = {z.module()}')
    print('----------')


if operation_arg in operation[0:4]:
    print('----------')
    print(f'Calculation result: {z1.print_complex()} {operation_arg} {z2.print_complex()} = {result}')
    print('----------')
