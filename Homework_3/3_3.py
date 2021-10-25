# task 3_3 by Peregud Kirill

print("-----\nThe program displays list items that are less than 5.\n-----")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('Initial list:', a)

COMPARE_NUMB = 5
result_list = [x for x in a if x < COMPARE_NUMB]
print(f'\nThe result of displaying list items is less than {COMPARE_NUMB}:')

i = 0
for x in result_list:
    print(f'Item {i} -> {x}')
    i += 1
