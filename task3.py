"""
Задание 3.
По введенным пользователем координатам двух точек вывести уравнение
прямой вида y=kx+b, проходящей через эти точки

"""

if __name__ == '__main__':
    first_list = list(input ('Введите через пробел координаты '
                             'первой точки X1, Y1: ').split(' '))
    second_list = list(input ('Введите через пробел координаты '
                              'второй точки X2, Y2: ').split(' '))
    K_INDEX = (float(second_list[1]) - float(first_list[1])) / \
              (float(second_list[0]) - float(first_list[0]))
    B_INDEX = float(first_list[1]) - float(first_list[0]) * K_INDEX
    if B_INDEX < 0:
        SIGN = ''
    else:
        SIGN = '+'
    print(f'Уравнение имеет вид Y={K_INDEX}*X{SIGN}{B_INDEX}')
