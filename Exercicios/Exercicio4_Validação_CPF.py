"""
CPF = 168.995.350-09
-----------------------------------------------------------------
1 * 10 = 10                  #     1 * 11 = 11 <-
6 * 9 = 54                   #     6 * 10 = 60
8 * 8 = 64                   #     8 *  9 = 72
9 * 7 = 63                   #     9 *  8 = 72
9 * 6 = 54                   #     9 *  7 = 63
5 * 5 = 25                   #     5 *  6 = 30
3 * 4 = 12                   #     3 *  5 = 15
5 * 3 = 15                   #     5 *  4 = 20
0 * 2 = 0                    #     0 *  3 = 0
                             # ->  0 *  2 = 0
           297               #              343
11 - (297 % 11) = 11         #      11 - (343 % 11) = 9
11 > 9 = 0                   #
Digito 1 = 0                 #    Digito 2 = 9
"""
lista1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
lista2 = [11, 10, 9, 8, 7, 6, 5, 4, 3]
teste = []
cpf_novo = []
n = 0
cpf = '111318679'

for i in cpf:
    for x in lista1:
        n = n + x
        print(f'{x} + {i} = {i}')
    print(i)















