# task №9_1 by Kirill Peregud

import random

DOWN_RANGE = 1
UP_RANGE = 50


class BinarySearch:

    def __init__(self):
        self.search = 1

    def is_number_in(self, num, array):

        self.index_min = 0
        self.index_max = len(array) - 1
        self.middle_index = (self.index_min + self.index_max) // 2

        while num != array[self.middle_index] and self.index_min < self.index_max:
            
            if num >= array[self.index_min] and num <= array[self.middle_index]:
                self.index_max = self.middle_index - 1
            elif num >= array[self.middle_index] and num <= array[self.index_max]:
                self.index_min = self.middle_index + 1
            else:
                break

            self.middle_index = (self.index_min + self.index_max) // 2
            self.search += 1

        if num == array[self.middle_index]:
            return True
        else:
            return False


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

    search_number = enter_number('number to search')
    bs = BinarySearch()

    if bs.is_number_in(search_number, array):
        print(f'Result: the number "{search_number}" is in position "{bs.middle_index}" of the list.\n')
    else:
        print(f'Result: the number "{search_number}" is missing in the list.\n')

    print(f'Number of iterations: {bs.search}.')


if __name__ == '__main__':
    main()
