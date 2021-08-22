"""
Задание 4.
Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
"""

import random

if __name__ == '__main__':
    range_list = list (input ('Введите через пробел границы диапазона: ').split (' '))
    number_down, number_up = range_list[0], range_list[1]
    if number_down > number_up:
        number_down, number_up = number_up, number_down
    print (f'Случайное целое число вашего диапазона: '
           f'{random.randint(int(number_down), int(number_up))}')
    print (f'Случайное вещественное число вашего диапазона: '
           f'{random.uniform (float (number_down), float (number_up)):.2f}')
    my_symbol = random.randint (int (number_down) if int(number_down) > 0 else 0,
                                int (number_up) if int(number_up) < 256 else 256)
    print (f'Случайный символ вашего диапазона (диапазон ограничен 0-256): '
           f'код символа {my_symbol}, символ {chr(my_symbol)}')
