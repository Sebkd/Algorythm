"""
Урок 3
Задание 1
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

def func_count(number, *args):
    my_temp = list(*args)
    return len(list(filter(lambda x: x % number == 0, my_temp)))

if __name__ == '__main__':
    my_list = [number for number in range(2, 100)]
    print(my_list)
    for number in range (2, 10):
        print(f'Для числа {number} кол-во кратных'
              f' чисел в списке от 2 до 99'
              f' равно: {func_count(number, my_list)}')
