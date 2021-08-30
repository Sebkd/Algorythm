"""
Урок 2
Задание 6.
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или
меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число
"""

import random


def func_tasksix(number_in, count):
    """
    Функция реализует простое сравнения введенного пользователем числа и
    запрограммированным
    :param number_in: загаданное число
    :param count: количество попыток
    """
    try:
        print (f'Попытка: {count}')
        answer = int (input ('Введите число от 0 до 100: '))
        if count == 10 or answer == number_in:
            if answer == number_in:
                print ('Угадали!')
            else:
                print('Кол-во попыток закончилось')
        else:
            if answer > number_in:
                print (f'Загаданное число меньше чем {answer}')
            else:
                print (f'Загаданное число больше чем {answer}')
            func_tasksix (number_in, count + 1)
    except ValueError:
        print('Вы ввели не число')
        func_tasksix (number_in, count + 1)


if __name__ == '__main__':
    func_tasksix (random.randint (0, 100), 1)
