# task 3_5 by Peregud Kirill

print("\nThe program calculates the sum of the digits of a three-digit number.\n")

sum = 0
while sum == 0:
    enter_num = input('Please, enter a positive three-digit number:\n')
    try:
        number = int(enter_num)
    except:
        print('Unfortunately, the argument is not a integer :(\n')
    else:
        if len(enter_num) != 3 or number < 100:
            print(f'Sorry, the number "{enter_num}" is not positive three-digit...\n')
        else:
            for num in enter_num:
                sum += int(num)

print(f'-----\nThe sum of the digits of the number {number} -> \
{sum}\n-----')
