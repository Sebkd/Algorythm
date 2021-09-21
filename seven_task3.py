"""
Урок 7
Задание 3
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда,
делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках
"""
from random import randint
from seven_task2 import func_rec_mergesort


def sherlock_find(first, second, *args):
    """
    Поиск медианны без сортировки первоначального списка
    :param first: начало списка
    :param second: конец списка
    :param args: несортированный список
    :return: медиана списка
    """
    temp_list = list (args)
    median = len (temp_list) // 2
    if first >= second:
        return temp_list[median]
    pillar, i_index, j_index = temp_list[median], first, second
    while i_index <= j_index: # пока нет сходимости индексов слева и справа
        while temp_list[i_index] < pillar:
            i_index += 1 # выполняется пока значение слева не станет больше тестового значения
        while temp_list[j_index] > pillar:
            j_index -= 1 # то же самое только проверяется пока значение справа не станет меньше
        if i_index <= j_index: # при условии что список еще имеет элементы, есть разница
            # между индексами, значения меняются местами и индексы далее продолжают сходимость
            temp_list[i_index], temp_list[j_index] = temp_list[j_index], temp_list[i_index]
            i_index += 1
            j_index -= 1
    if i_index > median: # рекурсивный вызов функции при условии что индексы сходимости не добрались
        # до середины списка, т.е запускаем еще раз сходимость списков
        temp_list[median] = sherlock_find (first, j_index, *temp_list)
    elif j_index < median:
        temp_list[median] = sherlock_find (i_index, second, *temp_list)
    return temp_list[median]


if __name__ == '__main__':
    m_number = randint(10, 100)
    unsort_list = [randint (0, 50) for _ in range (2 * m_number + 1)]
    print (f'Ряд размера 2*m+1 при m = 100, имеет длину: {len (unsort_list)}')
    print (f'Несортированный список: {unsort_list}')
    middle = sherlock_find(0, len(unsort_list) - 1, *unsort_list)
    print(f'Медиана ряда несортированного списка: {middle}')
    sort_list = func_rec_mergesort(*unsort_list)
    unsort_list.sort()
    print(f'Сортированный список для проверки: {unsort_list}')
    print (f'Медиана ряда сортированного списка: {unsort_list[len (unsort_list) // 2]}')
    print (f'Сортированный список из task2 для проверки: {sort_list}')
    print(f'Медиана ряда сортированного списка: {sort_list[len(sort_list) // 2]}')
