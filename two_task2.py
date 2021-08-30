"""
Урок 2
Задание 2.
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5)
"""


def func_recursion_two(number, in_even_numbers=0, in_odd_numbers=0):
    """
    Функция подсчета четных и нечетных цифр в числе
    :param number: наше число
    :param in_even_numbers: число четных цифр
    :param in_odd_numbers: число нечетных чисел
    :return: возврат количества четных и нечетных чисел
    """
    if number == 0:
        return in_even_numbers, in_odd_numbers
    cur_n = number % 10
    number = number // 10
    if cur_n % 2 == 0:
        in_even_numbers += 1
    else:
        in_odd_numbers += 1
    return func_recursion_two (number, in_even_numbers, in_odd_numbers)




if __name__ == '__main__':
    try:
        even_numbers, odd_numbers = 0, 0
        print ('Количество четных и нечетных цифр в числе равно: ',
               func_recursion_two (int (input ('Введите число: '))))
    except ValueError:
        print ('Вы ввели не число')
