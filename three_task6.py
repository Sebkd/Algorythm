"""
Урок 3
Задание 6
В одномерном массиве найти сумму элементов, находящихся между минимальным
и максимальным элементами. Сами минимальный и максимальный элементы
в сумму не включать
"""

import random


if __name__ == '__main__':
    my_list = [random.randint (10, 1000) for number in range (100)]
    print (my_list)
    INDEX_MAX, INDEX_MIN, STEP, SUM = 0, 0, 1, 0
    for value in my_list:
        if my_list[INDEX_MAX] < value:
            INDEX_MAX = my_list.index(value)
        elif my_list[INDEX_MIN] > value:
            INDEX_MIN = my_list.index(value)
    print(f'Максимальное число с индексом {INDEX_MAX},'
          f' равно {my_list[INDEX_MAX]}, '
          f'Минимальное число с индексом {INDEX_MIN}, '
          f'равно {my_list[INDEX_MIN]}')
    if (INDEX_MAX - INDEX_MIN) < 0:
        STEP = -1
    for value in my_list[INDEX_MIN+STEP:INDEX_MAX:STEP]:
        SUM += value
    print(f'Сумма элементов, находящихся между минимальным {my_list[INDEX_MIN]}'
          f' и максимальным {my_list[INDEX_MAX]} элементами, равна {SUM}')
