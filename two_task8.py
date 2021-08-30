"""
Урок 2
Задание 8.
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры
"""


def func_taskeleven(*args):
    """
    Рекурсия:уменьшаем искомое число и проверяем остаток, равен
    он нашему искомому числу или нет, если да, то увеличиваем счетчик
    :param args: счетчик, число, искомая цифра
    :return: условие выхода счетчик или вызов рекурсии
            Альтернативный вариант
    if my_line == 0:
        return counter
    my_line, remainder = divmod (my_line, 10)
    if remainder == true_number:
        counter += 1
    return func_taskeleven (counter, my_line, true_number)
    """
    counter, my_line, true_number = args[0], args[1], args[2]
    return counter if my_line == 0 else func_taskeleven(counter + 1
                                                        if (my_line % 10) == true_number
                                                        else counter,
                                                        my_line // 10, true_number)


if __name__ == '__main__':
    try:
        while True:
            range_list = [int (number) for number in list (input (
                'Введите через пробел последовательность чисел и'
                ' цифру которую нужно подсчитать ').split (' '))]
            if len (range_list) != 2:
                print ('Введено не три числа, попробуйте еще раз')
                continue
            print (f'Количество вхождений цифры {range_list[1]}'
                   f' в последовательности {range_list[0]} равна '
                   f'{func_taskeleven (0, *range_list)}')
    except ValueError:
        print ('Вы ввели не число')
