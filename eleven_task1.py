"""
Урок 8
Задание 1
Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке
"""

from hashlib import sha1


def func_usual(string):
    """
    Функция подсчета уникальных подстрок
    :param string: строка
    :return: длина множества хэш значений уникальных подстрок
    """
    sum_sub_string = set ()
    for index_alpha in range (len (string)):
        for index_beta in range (len (string), index_alpha, -1):
            hash_str = sha1 (string[index_alpha:index_beta].encode ('utf-8')).hexdigest ()
            sum_sub_string.add (hash_str)
    return len (sum_sub_string)


if __name__ == '__main__':
    while True:
        my_string = str (input ('Введите строку из английских букв: ')).lower ()
        if my_string.isalpha ():
            print (f'в этой строке {func_usual (my_string)} уникальных подстрок')
            break
