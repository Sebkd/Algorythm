"""
Урок 3
Задание 8
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""



if __name__ == '__main__':
    matrix = []
    LINE_MATRIX, COLUMN_MATRIX = 4, 5
    for line in range(LINE_MATRIX):
        matrix.append([])
        SUM = 0
        for column in range(COLUMN_MATRIX-1):
            user_value = int(input(f'Введите число {line + 1}'
                                   f', столбец {column + 1}: '))
            SUM += user_value
            matrix[line].append(user_value)
        matrix[line].append(SUM)
    for line in matrix:
        print(' '.join(map(str, line)))
