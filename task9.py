"""
Задание 9.
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

if __name__ == '__main__':
    while True:
        try:
            range_list = [int(number) for number in list (input (
                'Введите через пробел три числа ').split (' '))]
            if len(range_list) != 3:
                print('Введено не три числа, попробуйте еще раз')
                continue
            range_list.sort(reverse = True)
            print(f'Это число "{range_list[1]}" является средним '
                  f'(больше одного, но меньше другого)')
            break
        except TypeError:
            print('Введены не числа или длины меньше 0')
