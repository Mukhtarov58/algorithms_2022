"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""
def find_sum_number(count, sum_number = 0, number = 1):
    if count == 0:
        return sum_number
    else:
        return find_sum_number(count -1, sum_number + number, number / -2)


count = int(input("Введите количество элементов: "))
print(find_sum_number(count))
