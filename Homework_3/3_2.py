# task 3_2 by Peregud Kirill

DOWN_RANGE = 3
UP_RANGE = 23
operation = ('+', '-', '*', '/')

print(
"""
Enter two arguments from 3 to 23 and an operation
on them ('+', '-', '*', '/'), output the result of the calculation.
"""
)


def enter_argument(name_arg):
    enter_arg = False
    while enter_arg is not True:
        try:
            value_arg = int(
                input(f'Please, enter a {name_arg} argument from {DOWN_RANGE} to {UP_RANGE}:\n')
                )
        except:
            print('Unfortunately, the argument is not a natural number :(\n')
        else:
            if DOWN_RANGE <= value_arg <= UP_RANGE:
                enter_arg = True
            else:
                print(
                    f'Sorry, the {name_arg} argument is not in the range from {DOWN_RANGE} to {UP_RANGE}...\n'
                    )
    return value_arg

first_arg = enter_argument('first')
second_arg = enter_argument('second')

operation_arg = input(
        'Please, enter operation on numbers: "+", "-", "*", "/"\n'
        )
while  operation_arg not in operation:
    print('\t-----\nOh, incorrect input :(\n\t-----')
    operation_arg = input(
        'Please, enter operation on numbers: "+", "-", "*", "/"\n'
        )

if operation_arg == operation[0]:
    result = first_arg + second_arg
elif operation_arg == operation[1]:
    result = first_arg - second_arg
elif operation_arg == operation[2]:
    result = first_arg * second_arg
elif operation_arg == operation[3]:
    result = first_arg / second_arg

print(f'Operation result: {first_arg} {operation_arg} {second_arg} = {result}')
