"""
Урок 2
Задание 9
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр
"""


def func_sum(*args):
    """
    Функция подсчитывает сумму цифр числа через рекурсию
    :param args: сумма чисел и непосредственно само число
    :return: возвращает сумму цифр числа
    """
    my_sum, my_number = args[0], args[1]
    return my_sum if my_number == 0 else func_sum (my_sum + my_number % 10, my_number // 10)


def func_tasknine(*args):
    """
    Функция подсчитывает наибольшее по сумме цифр число
    :param args: список натуральных чисел
    :return: вывод на экран полученных значений
    """
    my_list = args
    max_value, max_index = 0, 0
    for index, item in enumerate (my_list):
        if func_sum (0, item) > max_value:
            max_value = func_sum (0, item)
            max_index = index
    return print (f'Наибольшее по сумме цифр это число {my_list[max_index]}, '
                  f'а сумма его цифр равна {max_value}')


if __name__ == '__main__':
    try:
        range_list = [int (number) for number in list (input (
            'Введите через пробел последовательность чисел ').split (' '))]
        func_tasknine (*range_list)
    except ValueError:
        print ('Вы ввели не число')
