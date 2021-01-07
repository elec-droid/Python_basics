""" Реализовать генератор с помощью функции с ключевым словом ​ yield​ , создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция должна
вызываться следующим образом: ​
for el in fact(n)​ . Функция отвечает за получение факториала
числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24. """


from math import factorial
from excluded.my_service import get_user_value


def my_fact_yield(n: int):
    for itr in range(1, n + 1):
        yield factorial(itr)


num = get_user_value(int)
for i, itr in enumerate(my_fact_yield(num), 1):
    print(f'{i}!: {itr}')
