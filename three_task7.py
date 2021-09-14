"""
Урок 3
Задание 7
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
так и различаться
"""

import random


if __name__ == '__main__':
    my_list = [random.randint (10, 100) for number in range (100)]
    print (my_list)
    sort_list = []
    sort_list.extend(my_list)
    sort_list.sort()
    print(f'Два наименьших элемента списка 1) "{sort_list[0]}",'
          f'с индексом "{my_list.index(sort_list[0])}", '
          f'2) "{sort_list[1]}",'
          f'с индексом "{my_list.index(sort_list[1])}"')
