"""
Урок 7
Задание 2
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы
"""

import cProfile
import io
import pstats
from pstats import SortKey
from random import randint
from timeit import default_timer


def func_rec_mergesort(*args):
    """
    Функция предварительного разбиения вводимого массива чисел на массивы
    по одному числу (рекурсивный метод):
    Массив делится на две части, далее каждый последующий делиться также
    на две части и так пока не останется в массиве 1 число.
    далее запускается функция сортировки под каждой рекурсией
    :param args: несортированный массив
    :return: сортированный массив
    """
    temp_list = list (args)
    if len (temp_list) < 2:
        return temp_list[:]
    middle = len (temp_list) // 2
    left_list = func_rec_mergesort (*temp_list[:middle])
    right_list = func_rec_mergesort (*temp_list[middle:])
    return func_merge (left_list, right_list)


def func_merge(left_list, right_list):
    """
    сравнение и упорядочивание двух массивов
    :param left_list: первый массив
    :param right_list: второй массив
    :return: сортированный один массив
    """
    result, l_index, r_index = [], 0, 0
    while l_index < len (left_list) and r_index < len (right_list):
        if left_list[l_index] < right_list[r_index]:
            result.append (left_list[l_index])
            l_index += 1
        else:
            result.append (right_list[r_index])
            r_index += 1
    while l_index < len (left_list):
        result.append (left_list[l_index])
        l_index += 1
    while r_index < len (right_list):
        result.append (right_list[r_index])
        r_index += 1
    return result


if __name__ == '__main__':
    pr = cProfile.Profile ()
    pr.enable () # запускаем подсчет профилировщиком
    '''Основная программа'''
    unsort_list = [randint (0, 50) for _ in range (60)]
    print (unsort_list)
    start_time = default_timer ()
    sort_list = func_rec_mergesort (*unsort_list)
    print (f'Время выполнения {default_timer () - start_time}\n'
           f'{sort_list}')
    '''Конец основной программы'''
    pr.disable () # останавливаем подсчет профилировщиком
    s = io.StringIO ()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats (pr, stream = s).sort_stats (sortby)
    ps.print_stats ()
    print (s.getvalue ()) # вывод статистики
