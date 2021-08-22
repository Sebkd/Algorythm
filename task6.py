"""
Задание 6.
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""



if __name__ == '__main__':
    try:
        number_up = int(input ('Введите номер буквы в алфавите a до z '
                                  '(A до Z) '))
        if number_up > 26 or number_up < 0:
            raise TypeError
        print(f'Ваш символ "{chr(number_up + 96)}" ')
    except TypeError:
        print('Введено число меньше 0 или более 26 английского алфавита')
    except ValueError:
        print('Вводить необходимо одно число')
