"""
Урок 2
Задание 1.
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа
не должна завершаться, а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""


def show_me(*args):
    """
    Функция вывода на экран результатов введенных данных
    :param args: посчитанный результат
    :return: вывод на экран
    """
    return print ('Ваш результат: ', args[0])


def input_operand():
    """
    Функция запроса операции
    :return: возвращает введенный знак
    """
    operand_inn = input ('Введите операцию (+, -, *, / или 0 для выхода): ')
    return operand_inn


def func_taskone(operand=0):
    """
     Функция отработки введенных данных и зацикливания
    :param operand: введенный знак
    :return: в случае завершения вводится 0 и функция завершается
    """
    try:
        if operand == "0":
            return True
        range_list = [int (number) for number in list (input (
            'Введите через пробел два числа ').split (' '))]
        if len (range_list) != 2:
            # Проверка то что чисел 2 если нет то вызываем исключение
            raise ValueError
        if operand == "+":
            show_me (range_list[0] + range_list[1])
        elif operand == "-":
            show_me (range_list[0] - range_list[1])
        elif operand == "*":
            show_me (range_list[0] * range_list[1])
        elif operand == "/":
            show_me (range_list[0] / range_list[1])
        else:
            raise ValueError
        operand = input_operand () # Дальнейшее выполнение программы
        if operand in "+-*/0":
            func_taskone (operand)
        else:
            return False
    except (ValueError, ZeroDivisionError):
        print ('Вы ввели не числа, больше или меньше двух чисел или '
               'или делитель равен 0, попробуйте заново')
        operand = input_operand ()
        if operand in "+-*/0":
            func_taskone (operand)
        else:
            return False


if __name__ == '__main__':
    while True:
        operand_out = input_operand ()
        if operand_out in "+-*/0":
            if func_taskone (operand_out):
                print ('Финал программы')
                break
        else:
            print ('У вас недопустимый знак операции и не ноль,'
                   'попробуйте снова ввести\n')
            continue
