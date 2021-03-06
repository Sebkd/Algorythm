"""
Задание 2.
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

"""




if __name__ == '__main__':
    NUMBER_A = 5
    NUMBER_B = 6
    print(bin(NUMBER_A), bin(NUMBER_B))
    print (NUMBER_A & NUMBER_B)
    '''
    Побитовое И возвращает 1, если оба бита равны 1, в противном случае – 0
    '''
    print (NUMBER_A | NUMBER_B)
    '''
    Побитовое ИЛИ возвращает 1, если какой то бит равен 1, если оба равны 0 то 0
    '''
    print (NUMBER_A ^ NUMBER_B)
    '''
    Побитовое XOR возвращает 1, если один из битов равен 0, а другой бит равен 1.
    Если оба бита равны 0 или 1, он возвращает 0.
    '''
    print (~NUMBER_A)
    '''
    Комплиментарное увеличение на 1 бит, получается -0b110
    '''
    print (NUMBER_A << 2)
    '''
    Побитовый сдвиг влево, умножение на 2 получилось 0b10100
    '''
    print (NUMBER_A >> 2)
    '''
    Побитовый сдвиг вправо, деление на 2 получилось 0b001
    '''
