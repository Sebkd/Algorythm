"""
Урок 4
Задание 2
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию:
Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""

import math
from timeit import default_timer


def func_erotosfen(number_in):
    '''
    Функция использует теорему о распределении простых чисел,
    она утверждает, что количество простых чисел на отрезке
    [1;n] растёт с увеличением n как n / ln(n)
    :param number_in: какое i-ое по счету простое число
    :return: i-ое простое число
    '''
    number_primes = 0
    upper_limit = 2
    while number_primes <= number_in:
        number_primes = upper_limit / math.log (upper_limit)
        upper_limit += 1
    list_primes = [value for value in range (2, upper_limit)]
    for value in list_primes:
        if list_primes.index (value) <= value - 1:
            for just in range (2, len (list_primes)):
                if value * just in list_primes[value:]:
                    list_primes.remove (value * just)
        else:
            break
    return list_primes[number_in - 1]

def func_not_erotosfen(number_in):
    """
    Функция поиска i-го простого числа
    :param number_in: порядок числа
    :return: само простое число
    """
    my_list = [2]
    number = 3
    while len (my_list) < number_in:
        right_on = True
        for just in my_list.copy ():
            if number % just == 0:
                right_on = False
                break
        if right_on:
            my_list.append (number)
        number += 1
    return my_list[-1]



if __name__ == '__main__':
    my_number = int (input ('Введите порядок простого числа: '))
    start_time = default_timer()
    print (f'Без использования решета Эратосфена: {func_not_erotosfen (my_number)}')
    wo_eratosfen = default_timer() - start_time
    start_time = default_timer()
    print (f'C использования решета Эратосфена: {func_erotosfen (my_number)}')
    w_eratosfen = default_timer() - start_time
    print(f'Решение без решета Эратосфена быстрее в {w_eratosfen / wo_eratosfen} раз')
    '''
Введите порядок простого числа: 1000
Без использования решета Эратосфена: 7919
C использования решета Эратосфена: 7919
Решение без решета Эратосфена быстрее в 101.19699101931339 раз
    '''
