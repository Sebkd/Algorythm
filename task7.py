"""
Задание 7.
 По длинам трех отрезков, введенных пользователем, определить возможность
 существования треугольника, составленного из этих отрезков.
 Если такой треугольник существует, то определить,
 является ли он разносторонним, равнобедренным или равносторонним.
"""

def possibolity (*args):
    '''
    Проверка возможности существования треугольника.
    сумма меньших двух сторон должна быть больше третей стороны
    :param args:
    :return:
    '''
    if args[2] + args[1] < args[0]:
        return True
    return False

def isosceles (*args):
    '''
    Проверка равнобедренного треугольника
    :param args:
    :return:
    '''
    if args[0]  == args[2] or args[0] == args[1] or args[1] == args[2]:
        return True
    return False

def equilateral (*args):
    '''
    Проверка равностороннего треугольника
    :param args:
    :return:
    '''
    if args[0]  == args[2] and args[0] == args[1]:
        return True
    return False

if __name__ == '__main__':
    while True:
        try:
            range_list = [int(number) for number in list (input (
                'Введите через пробел длины сторон треугольника ').split (' '))]
            if len(range_list) < 3:
                print('Введено не три длины, а меньше')
                continue
            range_list.sort(reverse = True)
            if possibolity(*range_list):
                print ('Треугольник невозможен')
            elif equilateral (*range_list):
                print ('Треугольник равносторонний')
            elif isosceles (*range_list):
                print ('Треугольник равнобедренный')
            else:
                print ('Треугольник разносторонний')
            break
        except TypeError:
            print('Введены не числа или длины меньше 0')
        except ValueError:
            print('Вводить необходимо одно число')
