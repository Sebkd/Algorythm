"""
Урок 3
Задание 3
В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы
"""

import random

if __name__ == '__main__':
    my_list = [number for number in range(21)]
    random.shuffle(my_list)
    print(my_list)
    print(max(my_list), my_list.index(max(my_list)))
    print(min(my_list), my_list.index(min(my_list)))
    my_list[my_list.index(max(my_list))], my_list[my_list.index(min(my_list))] \
        = my_list[my_list.index(min(my_list))], my_list[my_list.index(max(my_list))]
    print (my_list)
    print (max (my_list), my_list.index (max (my_list)))
    print (min (my_list), my_list.index (min (my_list)))
