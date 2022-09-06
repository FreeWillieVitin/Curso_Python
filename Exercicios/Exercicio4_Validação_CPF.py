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
vl2 = 11
cpf_novo = []
n = 0
cpf = '11131867980'
li = list(cpf)
soma = 0
soma2 = 0
cpf2 = cpf[:-2]

for i in cpf2:
    te = int(i)
    cal1 = te * vl1
    soma = soma + cal1
prox1 = 11 - (soma % 11)
if prox1 > 9:
    cpf_novo.append(0)
else:
    cpf_novo.append(prox1)
print(soma)

for x in cpf2:
    te2 = int(x)
    cal2 = te2 * vl2
    soma2 = soma2 + cal2
prox2 = 11 - (soma2 % 11)
if prox2 > 9:
    cpf_novo.append(0)
else:
    cpf_novo.append(prox2)
print(soma2)

print(cpf_novo)















