"""
Урок 8
Задание 2
Закодируйте любую строку из трех слов по алгоритму Хаффмана
"""

import heapq
from collections import Counter
from collections import namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


if __name__ == '__main__':
