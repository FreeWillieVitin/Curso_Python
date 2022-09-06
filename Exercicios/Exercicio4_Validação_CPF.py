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
vl1 = 10
vl2 = 10
cpf_novo = []
cpf = '11613504977'
soma = 0
soma2 = 0
dg1 = 0
dg2 = 0

for i in range(0, len(cpf)-2):
    soma = soma + (int(cpf[i]) * vl1)
    i += 1
    vl1 -= 1
dg1 = 11 - (soma % 11)
if dg1 >= 10:
    cpf_novo.append(0)
else:
    cpf_novo.append(dg1)

for x in range(1, len(cpf)-1):
    soma2 = soma2 + (int(x) * vl2)
    x += 1
    vl2 -= 1
dg2 = 11 - (soma2 % 11)
if dg2 >= 10:
    cpf_novo.append(0)
else:
    cpf_novo.append(dg2)
print(soma)
print(soma2)
print(cpf_novo)
