"""
Урок 5
Задание 1
Пользователь вводит данные о количестве предприятий, их наименования
и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
"""

import collections
from random import randint

if __name__ == '__main__':
    try:
        Company = collections.namedtuple ('Company', ['quarter1',
                                                      'quarter2',
                                                      'quarter3',
                                                      'quarter4',
                                                      'avg_profit'])
        book_of_company = {}
        number_of_company = int (input ('Введите количество компаний: '))
        manual_or_auto = 
        for number in range (1, number_of_company + 1):
            name = input (str (number) + '-ая компания ')
            profit = [0] * 5
            for value in range (4):
                profit[value] = int (input ('Введите прибыль за ' + str (value + 1) + ' квартал: '))
                profit[4] += profit[value]
            profit[4] /= 4
            book_of_company[name] = Company(
                quarter1 = profit[0],
                quarter2 = profit[1],
                quarter3 = profit[2],
                quarter4 = profit[3],
                avg_profit = profit[4]
            )
        total_avg_profit = 0
        for name, profit in book_of_company.items():
            print(f'Компания {name}, средняя прибыль {profit[4]}')
            total_avg_profit += profit[4]
        print(f'Средняя прибыль (за год для всех компаний): {total_avg_profit} ')




    except ValueError:
        print ('Вы ввели не число')
