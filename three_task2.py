"""
Урок 3
Задание 2
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
то во второй массив надо заполнить значениями 0, 3, 4, 5,
т.к. именно в этих позициях первого массива стоят четные числа
"""

import random

if __name__ == '__main__':
    my_list = [number for number in range(21)]
    random.shuffle(my_list)
    print(my_list)
    list_b = []
    for index, number in enumerate(my_list):
        if number % 2 == 0 and number != 0:
            list_b.append(index)
    print(list_b)
