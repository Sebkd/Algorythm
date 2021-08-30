"""
Задание 5.
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят
и сколько между ними находится букв.
"""



if __name__ == '__main__':


    try:
        range_list = list (input ('Введите через пробел две буквы '
                              'диапазона от a до f (A до F англ): ').lower().split (' '))
        number_up, number_down = ord (range_list[0]) - 96, ord (range_list[1]) - 96
        if number_up > 26 or number_down > 26 or number_up > 26 or number_down > 26:
            raise TypeError
        if number_down < number_up:
            number_down, number_up = number_up, number_down
        print(f'Ваш символ "{chr(number_up + 96)}" стоит {number_up} на месте в алфавите'
              f'\nА символ "{chr(number_down + 96)}" стоит {number_down} на месте в алфавите\n'
              f'Между ними {number_down - number_up - 1} символ(-а, -ов)')
    except TypeError:
        print('Введен не символ или буквы не английского алфавита')
    except ValueError:
        print('Вводить необходимо через пробел, без знаков препинания')
