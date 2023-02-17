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
# Minha versão do exercício
vl1 = 10  # Valor que indica o valor a ser multiplicado(é descontado 1 a cada volta do laço)
vl2 = 10
cpf_novo = []  # Lista que armazenará o cpf validado
cpf = '16899535009'  # Valor a ser verificado
soma = 0  # Armazena o resultado da operação que multiplica cada numero do CPF
soma2 = 0
dg1 = 0  # Armazena o resultado da operação de verificação do CPF
dg2 = 0

for i in range(0, len(cpf)-2):  # Inicia um laço em cada número do CPF menos os dois últimos
    soma = soma + (int(cpf[i]) * vl1)  # Insere na variável o resultado da expressão que multiplica cada número do CPF
    # pelo valor atual da variável vl1 e depois realiza a adição com a variável soma
    i += 1  # Acrescenta 1 cada vez que iniciar o laço
    vl1 -= 1    # Diminui 1 da variavel vl1 cada vez que retorna o laço
dg1 = 11 - (soma % 11)  # Armazena na variável o resultado da operação
if dg1 >= 10:   # Verifica se o resultado é maior que 10
    cpf_novo.append(0)  # Se for maior um novo caractere é inserido para verificar com o cpf completo
else:
    cpf_novo.append(dg1)    # se não for maior que 10 então é inserido o resultado da operação

for x in range(1, len(cpf)-1): # Inicia um laço em cada número do CPF menos 1, pois ja foi verificado um dos números
    soma2 = soma2 + (int(cpf[x]) * vl2)
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

"""
Aqui ficará a versão do professor

cpf = '16899535009'
novo_cpf = cpf[:-2]
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9
    total += int(novo_cpf[index]) * reverso
        
    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        
        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)
        
if cpf == novo_cpf:
    print('Válido')
else:
    print('Inválido')
"""