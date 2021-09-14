"""
Урок 3
Задание 4
Определить, какое число в массиве встречается чаще всего
"""

import random


def func_rec(max_i, *args):
    """
    Функция возвращает индекс списка элемент которого чаще всего
    встречается в этом списке, сделано через рекурсию с уменьшением
    длины передаваемого списка
    :param max_i: индекс
    :param args: список
    :return: индекс числа вхождение которого наибольшее в списке
    """
    my_list_in = list (*args)
    if len (my_list_in) == 0:
        return max_i
    if my_list_in.count (max_i) < my_list_in.count ([-1]):
        max_i = my_list_in.pop ()
    else:
        my_list_in.pop ()
    func_rec (max_i, my_list_in)


if __name__ == '__main__':
    my_list = [random.randint (0, 100) for number in range (100)]
    print (my_list)
    INDEX_MAX_REC = func_rec (0)
    print (f'Число {my_list[INDEX_MAX_REC]} встречается чаще '
           f'всего =  {my_list.count (INDEX_MAX_REC)} раз(-а)')
