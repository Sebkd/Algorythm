"""
Урок 3
Задание 9
Найти максимальный элемент среди минимальных элементов столбцов матрицы
"""
import random

if __name__ == '__main__':
    matrix = []
    LINE_MATRIX, COLUMN_MATRIX = 4, 5
    for line in range(LINE_MATRIX):
        matrix.append([])
        SUM = 0
        for column in range(COLUMN_MATRIX-1):
            user_value = random.randint(10, 100)
            matrix[line].append(user_value)
    for line in matrix:
        print(' '.join(map(str, line)))
    calc_line = []
    for column in range(COLUMN_MATRIX-1):
        calc_column = []
        for line in matrix:
            calc_column.append(line[column-1])
        calc_column.sort()
        calc_line.append(calc_column[0])
    calc_line.sort ()
    calc_line.reverse ()
    print(f'Максимальный элемент среди минимальных элементов '
          f'столбцов матрицы равен {calc_line[0]}')
