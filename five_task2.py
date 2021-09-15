"""
Урок 5
Задание 2
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого
это цифры числа. Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
"""


def hex_to_int(*args):
    """
    Перевод значения 16-ричного в 10-ный [] + проверка что число в hex формате
    :param args: типа A2
    :return: [162]
    """
    temp_number = hex (int (''.join (list (*args)), 16))
    return int (''.join (list (*args)), 16)


def add_hex(*args):
    """
    Сложение 2-х 16-ричных чисел
    :param args: десятичное число
    :return: типа ['A','2','F']
    """
    return list (hex (args[0] + args[1]).upper ())[2:]


def mult_hex(*args):
    """
    Умножение 2-х 16-ричных чисел
    :param args: десятичное число
    :return: типа ['A','2','F']
    """
    return list (hex (args[0] * args[1]).upper ())[2:]


if __name__ == '__main__':
    try:
        number_a = list (input ('Введите первое 16-ричное число: '))
        FIRST_HEX = hex_to_int (number_a)
        number_b = list (input ('Введите второе 16-ричное число: '))
        SECOND_HEX = hex_to_int (number_b)
        print (f'Первое число: {number_a}\nВторое число: {number_b}\n')
        print (f'Сложение этих чисел: {add_hex (FIRST_HEX, SECOND_HEX)}')
        print (f'Умножение этих чисел: {mult_hex (FIRST_HEX, SECOND_HEX)}\n')
    except ValueError:
        print('Введено не 16-ричное число')
