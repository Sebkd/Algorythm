"""
Урок 6
Задание 1
Подсчитать, сколько было выделено памяти под переменные в ранее
 разработанных программах в рамках первых трех уроков.
 Проанализировать результат и определить программы с наиболее
 эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

Разрядность x64, версия Python 3.9.0

Урок 3, задание 2
"""

import random
import sys

if __name__ == '__main__':
    my_list = [number for number in range(21)]
    random.shuffle(my_list)
    print(my_list)
    list_b = []
    for index, number in enumerate(my_list):
        if number % 2 == 0 and number != 0:
            list_b.append(index)
    print(list_b)
    tuple_c = tuple(list_b)
    print (f'Размер "my_list =" {sys.getsizeof (list_b)}')
    print(f'Размер "list_b =" {sys.getsizeof(list_b)}')
    print (f'Размер "tuple_c =" {sys.getsizeof (tuple_c)}')
'''
[19, 8, 14, 15, 3, 12, 17, 20, 6, 5, 16, 10, 11, 4, 9, 7, 1, 13, 2, 0, 18]
[1, 2, 5, 7, 8, 10, 11, 13, 18, 20]
Размер "my_list =" 184
Размер "list_b =" 184
Размер "tuple_c =" 120
размер листа меньше чем должен быть по формуле 40+8*длина
получается пайтон делает ссылки на одни и те же ссылки, при увеличении 
массива растет выделяемый объем памяти
'''