# task №5_1 by Kirill Peregud

print("\nThe program is convert arguments to 'int', 'float', 'str', 'tuple' or 'list'.")
types = (int, float, str, tuple, list)
result = []

def input_type():
    choice = None
    while choice != ('0', '1', '2', '3', '4'):
        print(
        """
    Choose an action:
        0 - Convert arguments to 'int'
        1 - Convert arguments to 'float'
        2 - Convert arguments to 'str'
        3 - Convert arguments to 'tuple'
        4 - Convert arguments to 'list'

        q - Quit
        """
        )
        choice = input('Your choice:\n').lower()
        if choice == '0':
            return types[0]
        elif choice == '1':
            return types[1]
        elif choice == '2':
            return types[2]
        elif choice == '3':
            return types[3]
        elif choice == '4':
            return types[4]
        elif choice == 'q':
            exit()
        else:
            print(f'Sorry, but position "{choice}" no such...')

type = input_type()

def decor_func(type):
    def actual(func):
        def wrapper(*args, **kwargs):
            print('\nStart decorator...\n')
            input_data = func(*args, **kwargs)
            if type == tuple:
                for arg in input_data:
                    result.append((arg,))
                print('\nFinish decorator...\n')
                return func(*result)
            elif type == list:
                for arg in input_data:
                    result.append([arg])
                print('\nFinish decorator...\n')
                return func(*result)
            else:
                for arg in input_data:
                    try:
                        value = type(arg)
                    except:
                        print(f'The argument {arg} can not be cast to the type {type}.')
                    else:
                        result.append(value)
                print('\nFinish decorator...\n')
                return func(*result)
        return wrapper
    return actual


@decor_func(type)
def function(*args, **kwargs):
    sp = args
    for (key, value) in list(kwargs.items()):
        sp += (key, value)
    return sp


funct = function(2, 3, 5, 234, '787', 'sdsds', 6.78, jljl=1, hjh=3, hh=10)
print('----------')
print(f'Result: {funct}.')
print('----------')
