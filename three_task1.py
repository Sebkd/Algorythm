"""
Урок 3
Задание 1
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


def func_count(number_in, *args):
    """
    Функция подсчета кратности итерируемого объекта определенному числу
    :param number: кратное число
    :param args: итерируемый объект
    :return: возвращает кол-во вхождений
    """
    my_temp = list (*args)
    return len (list (filter (lambda x: x % number_in == 0, my_temp)))


if __name__ == '__main__':
    '''Первый способ: заполнение, подсчет через функцию'''
    my_list = [number for number in range(2, 100)]
    print(my_list)
    for number in range (2, 10):
        print (f'Для числа {number} кол-во кратных'
               f' чисел в списке от 2 до 99'
               f' равно: {func_count (number, my_list)}')
    print('Второй способ')
    '''Второй способ: заполнение, подсчет и вывод, сразу в процессе
    заполнения списка'''
    for multiple_number in range (2, 10):
        print(f'Для числа {multiple_number} кол-во кратных'
               f' чисел в списке от 2 до 99'
               f' равно: '
              f'{len([number for number in range(2, 100) if number % multiple_number == 0])}')
