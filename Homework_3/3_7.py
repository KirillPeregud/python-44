# task 3_7 by Peregud Kirill
from decimal import *

print("\nBank.\n")

PERCENT = 10


def enter_number(name_side):
    num = 0
    while num <= 0:
        try:
            num = int(input(f'Please, enter {name_side}:\n'))
        except:
            print('Unfortunately, the argument is not a positive integer :(\n')
        else:
            if num > 0:
                break
            else:
                print('Enter a positive integer!\n')
    return num

a = enter_number('the amount of the deposit in rubles')
years = enter_number('the storage period of the deposit in years')

total_sum = Decimal(a)

for year in range(years):
    total_sum += Decimal(PERCENT/100) * total_sum
    total_sum = total_sum.quantize(Decimal("1.00"))

print(f'-------\nAfter {years} year(-s), with an initial deposit amount of {a} rub., \
the total deposit amount will be equal to {total_sum} rub.\n-------')
