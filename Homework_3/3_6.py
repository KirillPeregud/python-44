# task 3_6 by Peregud Kirill

print("\nThe program calculates the greatest common divisor \
of a pair of integers.\n")


def enter_number(name_arg):
    num = 0
    while num <= 0:
        try:
            num = int(input(f'Please, enter a {name_arg} argument:\n'))
        except:
            print('Unfortunately, the argument is not a positive integer :(\n')
        else:
            if num > 0:
                break
            else:
                print('Enter a positive integer!\n')
    return num

first_num = enter_number('first')
second_num = enter_number('second')

a = first_num
b = second_num

dif = None
while dif != 0:
    max_num = max(a, b)
    min_num = min(a, b)
    dif = max_num - min_num
    if dif == 0:
        nod = max_num
    else:
        a = dif
        b = min_num

print(f'-------\nThe greatest common divisor of a pair of integers \
{first_num}, {second_num} is -> {nod}\n-------')
