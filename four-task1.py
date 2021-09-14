"""
Урок 4
Задание 1
Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их
"""


def func_erotosfen(number_in):
    temp_list = [0] * number_in
    for value in range (number_in):
        temp_list[value] = value
    temp_list[1] = 0
    number_temp = 2
    while number_temp < number_in:
        if temp_list[number_temp] != 0:
            temp_value = number_temp * 2
            while temp_value < number_in:
                temp_list[temp_value] = 0
                temp_value += number_temp
        number_temp += 1
    return_list = []
    for index in temp_list:
        if temp_list[index] != 0:
            return_list.append (temp_list[index])
    del temp_list
    return return_list

def not_func_erotosfen(number_in):
    temp_list = [0] * number_in
    for value in range (number_in):
        temp_list[value] = value
    temp_list[1] = 0
    number_temp = 2
    


if __name__ == '__main__':
    my_number = int (input ('Введите натуральное число, '
                            'до которого необходимо вывести простые числа: '))
    print (func_erotosfen (my_number))
