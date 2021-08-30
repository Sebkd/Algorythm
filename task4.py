"""
Задание 4.
Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random

def input_numbers(choise):
    '''
    :param choise: выбор варианта что будет считаться
    :return: возвращает случайное число или символ
    '''
    if choise == 0 or choise == 1:
        range_list = list (input ('Введите через пробел границы '
                                  'диапазона для случайного числа: ').split (' '))
        number_down, number_up = range_list[0], range_list[1]
        if number_down > number_up:
            number_down, number_up = number_up, number_down
        if choise == 0:
            return print (f'Случайное целое число вашего диапазона: '
                   f'{random.randint (int (number_down), int (number_up))}')
        else:
            return print (f'Случайное вещественное число вашего диапазона: '
                   f'{random.uniform (float (number_down), float (number_up)):.2f}')
    range_list = list (input ('Введите через пробел границы '
                              'диапазона от a до f (англ): ').split (' '))
    number_down, number_up = ord(range_list[0]), ord(range_list[1])
    if number_down > number_up:
        number_down, number_up = number_up, number_down
    my_symbol = random.randint (int (number_down) if int (number_down) > 96 else 97,
                                int (number_up) if int (number_up) < 123 else 122)
    return print (f'Случайный символ вашего диапазона (диапазон ограничен от a до f): '
            f'код символа {my_symbol}, символ {chr (my_symbol)}')

if __name__ == '__main__':
    print('программа, которая генерирует в указанных пользователем границах: '
          '\nслучайное целое число; '
          '\nслучайное вещественное число; '
          '\nслучайный символ '
          '\nДля каждого из трех случаев пользователь задает свои границы диапазона\n'
          'Учитываются только два первых значения\n')
    try:
        for number in range(3):
            input_numbers(number)
    except TypeError:
        print('Введен не символ')
    except ValueError:
        print('Вводить необходимо через пробел, без знаков препинания')
