"""
Урок 2
Задание 7.
Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число
"""


def func_taskseven(number):
    """
    Рекурсивная функция обратного подсчета вручную 1+2+...+n
    :param number: количество элементов
    :return: их сумма, если количество элементов равно 1, выводится 1
    так как вызывать функцию не нужно
    """
    return number if number == 1 else number + func_taskseven (number - 1)


if __name__ == '__main__':
    try:
        NATURAL_NUMBER = int (input ('Введите натуральное число: '))
        print (func_taskseven (NATURAL_NUMBER))
        print (f'{int (NATURAL_NUMBER * (NATURAL_NUMBER + 1) / 2)}')
    except ValueError:
        print ('Вы ввели не число')
