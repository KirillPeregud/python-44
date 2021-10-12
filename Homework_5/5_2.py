# task №5_2 by Kirill Peregud

print("\nThe program outputs fibonacci numbers using a generator.")

def enter_number():
    start = 2
    num = start
    while num <= 2:
        try:
            num = int(input('\nEnter the amount of fibonacci numbers:\n'))
        except:
            print('\nUnfortunately, the argument is not an integer :(\n')
        else:
            if num > 2:
                break
            else:
                print(f'\nPlease, enter a positive integer greater than {start}.')
    return num

fibb = [0, 1]
n = enter_number()

generator_fibb = ((fibb[i - 1] + fibb[i - 2]) for i in range(2, n))
print(type(generator_fibb))

for val in generator_fibb:
    fibb.append(val)

print('----------')
print(f'Result: {fibb}')
print('----------')
