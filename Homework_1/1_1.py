# 1_1. Peregud Kirill
"""
Сломанные часы.

При заданном количестве секунд от начала дня (в диапазоне от 0 до 86400)
программа выводит точное время в формате: часы-минуты-секунды.
"""

MIN_TIME = 0
ONE_MINUTE = 60
ONE_HOUR = 3600
MAX_TIME = 86400
flag = False

# цикл будет выполняться, пока пользователь не введёт корректное значение
while flag is not True:
    # проверка введённого значения на целочисленность
    try:
        exact_time = int(input(
            "Please, enter a natural number from %d to %d:\n"
            % (MIN_TIME, MAX_TIME)
            ))
    except:
        print("Unfortunately, this is not a natural number :( \n")
    else:
        # если введено целое число,
        # проверяем его на вхождение в диапазон от 0 до 86400
        if MIN_TIME < exact_time <= MAX_TIME:
            hours = exact_time // ONE_HOUR
            minutes = (exact_time % ONE_HOUR) // ONE_MINUTE
            seconds = (exact_time % ONE_HOUR) % ONE_MINUTE
            flag = True
        else:
            print(
                "Sorry, this number isn't in the range from %d to %d..."
                % (MIN_TIME, MAX_TIME)
                )

print("Exact time: %02d hrs. %02d min. %02d sec." % (hours, minutes, seconds))
