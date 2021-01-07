# Python basics
GeekBrains домашние задания по курсу "Основы языка Python"
___
## Оглавление

1. [Знакомство с Python](#Знакомство-с-Python)
2. [Встроенные типы и операции с ними](#Встроенные-типы-и-операции-с-ними)
3. [Функции](#Функции)

____
## 1\. Знакомство с Python
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня. <br>Например: `a = 2`, `b = 3`. <br>Результат: <br>1-й день: 2 <br>2-й день: 2,2 <br>3-й день: 2,42 <br>4-й день: 2,66 <br>5-й день: 2,93 <br>6-й день: 3,22 <br>Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
## 2\. Встроенные типы и операции с ними
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию `type()` для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию `input()`.
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через `list` и через ```dict```.
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них. <br>
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. <br>
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2. <br>
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2. <br>
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1. <br>
Набор натуральных чисел можно задать непосредственно в коде, например, `my_list = [7, 5, 3, 3, 2]`.
6. \*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
```python
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
 ```
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров. Пример:
```python
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
```
## 3\. Функции
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
3. Реализовать функцию `my_func()`, которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
4. Программа принимает действительное положительное число `x` и целое отрицательное число `y`. Необходимо выполнить возведение числа `x` в степень `y`. Задание необходимо реализовать в виде функции `my_func(x, y)`. При решении задания необходимо обойтись без встроенной функции возведения числа в степень. <br> Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора `**`. Второй — более сложная реализация без оператора `**`, предусматривающая использование цикла.
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии *Enter* должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать *Enter*. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
6. Реализовать функцию `int_func()`, принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, `print(int_func(‘text’)) -> Text`. <br>Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию `int_func()`.
