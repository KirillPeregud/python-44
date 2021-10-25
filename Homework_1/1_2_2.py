# 1_2. Peregud Kirill
# без использованием метода .replace()
"""
Упоминания в СМИ.
Заменить упоминания о дяде Стёпе в тексте на своё имя.
"""

my_name = 'Kirill'
find_name = (
            'uncle styopa', 'unclestyopa',
            'uncle', 'styopa'
            )

# исходный текст:
enter_text = input("Please, enter your text:\n")

# переведём текст в нижний регистр на случай написания имени с разным регистром
edit_text = enter_text.lower()

# окончательный текст:
result_text = enter_text

index = None
while index != -1:
    for text in find_name:
        index = edit_text.find(text)  # возвращает -1, если text не найден

        # если совпадение text найдено, меняем строку с нижним регистром и
        # строку с окончательным вариантом текста
        if index != -1:
            edit_text = (
                edit_text[:index] + my_name + edit_text[index + len(text):]
                )
            result_text = (
                result_text[:index] + my_name + result_text[index + len(text):]
                )
            break

print("Finale text:\n" + result_text)
