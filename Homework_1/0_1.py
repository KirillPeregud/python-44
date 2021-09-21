# 1_0. Peregud Kirill
"""
Вывести на экран решение выражения:
"""
flag = False

while flag is not True:
    try:
        number = int(input("Please, enter an integer:\n"))
    except:
        print("Unfortunately, this is not an integer :( \n")
    else:
        x = 555 // 3 * (2 + 345) ** 7 - 345 + number
        flag = True

print("Solution:", x)
