# task 3_4 by Peregud Kirill
import math


def enter_number(name_side):
    num = 0
    while num <= 0:
        try:
            num = int(input(f'Enter the length of the {name_side}:\n'))
        except:
            print('Unfortunately, the argument is not an integer :(\n')
        else:
            if num > 0:
                break
            else:
                print('Enter a positive integer.')
    return num


def area_rectangle(a, b):
    return a * b


def area_triangle(a, b, c):
    semi_p = (a + b + c) / 2
    return math.sqrt(semi_p * (semi_p - a) * (semi_p - b) * (semi_p - c))


def area_circle(r):
    return math.pi * (r ** 2)

print("The program is designed to calculate the area of a rectangle, triangle or circle")

choice = None
while choice != 'q':
    print(
    """
    Choose an action:
    1 - Calculating the area of a rectangle
    2 - Calculating the area of a triangle
    3 - Calculating the area of a circle

    q - Quit
    """
    )
    choice = input('Your choice:\n').lower()
    if choice == '1':
        side_a = enter_number('first side')
        side_b = enter_number('second side')
        result = area_rectangle(side_a, side_b)
        print(f'-------\nThe area of a rectangle with sides {side_a}, {side_b} is: {result}\n-------')

    elif choice == '2':
        side_a = enter_number('first side')
        side_b = enter_number('second side')
        side_c = enter_number('third side')
        try:
            result = area_triangle(side_a, side_b, side_c)
        except ValueError:
            print(f'Triangle with sides {side_a}, {side_b}, {side_c} does not exist!')
            continue
        else:
            if result == 0:
                print(f'Triangle with sides {side_a}, {side_b}, {side_c} does not exist!')
            else:
                print(f'-------\nThe area of a triangle with sides {side_a}, {side_b}, {side_c} is: {result}\n-------')

    elif choice == '3':
        radius = enter_number('radius')
        result = area_circle(radius)
        print(f'-------\nThe area of a circle with radius {radius} is: {result}\n-------')

    elif choice == 'q':
        print('\nGood bye!\n')

    else:
        print(f'Sorry, but position "{choice}" no such...')
