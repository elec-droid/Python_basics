"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

my_list = [10, 20.20, 'строка', True, [10, 20, 30], {10, 20, 30}]

i = 0
while i < len(my_list):
    print(f'Элемент листа № {i+1} имеет значение "{my_list[i]}" и тип {type(my_list[i])}')
    i += 1
