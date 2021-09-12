"""
Урок 3
Задание 5
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве
"""

import random

if __name__ == '__main__':
    my_list = [random.randint (-100, 100) for number in range (100)]
    print (my_list)
    MAX_NEG_INDEX = 0
    for index, value in enumerate (my_list):
        MAX_NEG_INDEX = index if value < 0 and \
                                 abs (value) < abs (my_list[MAX_NEG_INDEX]) \
            else MAX_NEG_INDEX
    print (f'Максимальное отрицательное число "{my_list[MAX_NEG_INDEX]}"'
           f' оно имеет индекс в списке "{MAX_NEG_INDEX}"')
