"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (в материалах есть его описание)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
"""
from timeit import timeit

def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def resheto(i):
    a = []
    l = 10000
    for n in range(l+1):
        a.append(n)
    a[1] = 0
    n = 2
    while n <= l:
        if a[n] != 0:
            m = n + n
            while m <= l:
                a[m] = 0
                m = m + n
        n = n + 1

    return [p for p in a if p != 0] [i - 1]

i = int(input('Введите порядковый номер искомого простого числа: '))

print(simple(i))
print(resheto(i))

print(
    timeit(
        "simple(i)",
        setup="from __main__ import simple, i",
        number=100))
print(
    timeit(
        "resheto(i)",
        setup="from __main__ import resheto, i",
        number=100))
"""
Взяли 100 повторений. При поиске не большого числа скорость с применением
«Решета Эратосфена» очень низкая, с увеличением числа и растёт скорость.
Эффективно при работе с числами с большим порядковым числом.

i = 10

0.002321699999999982
0.4398635999999998

i = 100

0.47613499999999975
0.45380470000000006

i = 1000

46.1688623
0.47131740000000377
"""
