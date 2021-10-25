# task 3_5 by Peregud Kirill

print("\nThe program calculates the sum of the digits of a number.\n")

sum = 0
while sum == 0:
    enter_num = input('Please, enter a positive number:\n')
    try:
        number = int(enter_num)
    except:
        print('Unfortunately, the argument is not a integer :(\n')
    else:
        if number < 0:
            print(
                f'Sorry, the number "{enter_num}" is not positive...\n'
                )
        elif number == 0:
            break
        elif number > 0:
            for num in enter_num:
                sum += int(num)

print(f'-----\nThe sum of the digits of the number {enter_num} -> \
{sum}\n-----')
