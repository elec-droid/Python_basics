""" Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить
задание в одну строку.
Подсказка: использовать функцию ​ range()​ и генератор. """


print('\nКратные 20')
print([el for el in range(20, 239, 20)])
print('\nКратные 21')
print([el for el in range(20, 239) if el % 21 == 0])
print('\nКратные 20 и 21')
print([el for el in range(20, 239) if (el % 21 == 0) or (el % 20 == 0)])
