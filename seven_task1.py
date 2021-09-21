"""
Урок 7
Задание 1
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее)
"""

from random import randint
from timeit import default_timer


def bubble_sort(*args):
    """
    Пузырьковая сортировка
    :param args: несортированный массив
    :return: сортированный массив
    """
    temp_list = list (args)
    for index in range (len (temp_list) - 1):
        for j in range (len (temp_list) - index - 1):
            if temp_list[j] > temp_list[j + 1]:
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
    return temp_list


def bubble_sort_two(*args):
    """
    Пузырьковая сортировка оптимизированная
    :param args: несортированный массив
    :return: сортированный массив
    """
    temp_list = list (args)
    swap_signal = True
    total = 0
    while swap_signal:
        swap_signal = False
        for j in range (len (temp_list) - total - 1):
            if temp_list[j] > temp_list[j + 1]:
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
                swap_signal = True
        total += 1
    return temp_list


if __name__ == '__main__':
    unsort_list = [randint (-100, 100) for _ in range (200)]
    sort_list = bubble_sort (*unsort_list)
    sort_opt_list = bubble_sort_two (*unsort_list)
    print (f'Длина несортированного списка {len (unsort_list)}, список: {unsort_list}')
    start_time = default_timer ()
    print (f'Длина cортированного списка {len (sort_list)}, список: {sort_list}\n'
           f'Время выполнения: {default_timer() - start_time}')
    start_time = default_timer ()
    print (f'Длина сортированного опти списка {len (sort_opt_list)}, список: {sort_opt_list}\n'
           f'Время выполнения: {default_timer() - start_time}')
