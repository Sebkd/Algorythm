"""
Задание 8.
Определить, является ли год, который ввел пользователем, високосным или невисокосным.
"""

def leapyear(*args):
    '''
    Функция считает високосный год или нет
    :param args: вводится год
    :return: если год високосный то вывод True
    '''
    my_year = args[0]
    if my_year % 4 != 0 or (my_year % 100 == 0 and my_year % 400 != 0):
        return False
    return True


if __name__ == '__main__':
    if leapyear(int(input('Введите год в формате YYYY: '))):
        print ('Високосный год')
    else:
        print ('Обычный год')
