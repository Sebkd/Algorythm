"""
Задание 1.

Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""


def func_multiplication (number):
    '''
    функция умножения цифр числа
    '''
    if number // 10 == 0:
        return number
    local_number = number % 10
    return local_number * func_multiplication(number // 10)

def func_add (number):
    '''
    функция сложения цифр числа
    
    '''
    if number // 10 == 0:
        return number
    local_number = number % 10
    return local_number + func_add(number // 10)


if __name__ == '__main__':
    number = int(input('Введите 3-значное число: '))
    print(f'Произведение цифр вашего числа составляет {func_multiplication(number)}')
    print(f'Сумма цифр вашего числа составляет {func_add(number)}')

'''
сделано через рекурсию:
полностью раскрываем число на цифры и потом их или умножаем или слагаем
'''