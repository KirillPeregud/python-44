# task №9_1 by Kirill Peregud

import random

DOWN_RANGE = 1
UP_RANGE = 50


class CheckDublicate:

    def __init__(self):
        self.search = 0
        self.result = []

    def check(self, array):
        for index in range(len(array) - 1):
            if array[index] == array[index + 1]:
                if array[index] not in self.result:
                    self.result.append(array[index])
        return self.result


def enter_number(arg):
    print('----------')
    num = None
    while num not in range(DOWN_RANGE, UP_RANGE + 1):
        try:
            num = int(input(f'\nEnter the {arg}:\n'))
        except:
            print('\nUnfortunately, the argument is not an integer :(\n')
        else:
            if num in range(DOWN_RANGE, UP_RANGE + 1):
                break
            else:
                print(f'\nPlease, enter a positive integer number from {DOWN_RANGE} to {UP_RANGE}.')
    print('----------\n')    
    return num


def main():

    n = enter_number('size of sequence')
    array = [random.randint(DOWN_RANGE, UP_RANGE) for _ in range(n)]
    array.sort()
    print(array)

    result_dublicate = CheckDublicate().check(array)

    if result_dublicate:
        res_str = ''
        for elem in result_dublicate:
            res_str += str(elem) + '; '
        print(f'Dublicate numbers: {res_str}\n')
    else:
        print(f'No dublicates in the list.\n')


if __name__ == '__main__':
    main()
