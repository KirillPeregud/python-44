# 1_2. Peregud Kirill
# с использованием метода .replace()
"""
Упоминания в СМИ.

Заменить упоминания о дяде Стёпе в тексте на своё имя.
"""

my_name = 'Kirill'
find_name = (
            'Uncle Styopa', 'uncle Styopa', 'uncle styopa',
            'Uncle', 'Styopa',
            'uncle', 'styopa'
            )

enter_text = input("Please, enter your text:\n")
new_text = enter_text

for text in find_name:
    new_text = new_text.replace(text, my_name)

print("Finale text:\n" + new_text)
