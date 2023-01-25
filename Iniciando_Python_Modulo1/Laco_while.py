"""
While em Python - Repetição
utilizado para realizar ações enquanto uma condição for verdadeira
Loop Infinito -> Quando um código fica executando sem que haja um fim
while = enquanto

Operadores de atribuiçao com while
=, +=, -=, *=, /=, //=, **, %=
Não é necessario repetir a variavel para realizar operações
Ex: a = a + 1 -> pode ser substituido por a += 1
"""
# -------------------------------------------------------------------------------------------------------------------------
x = 1 # Define a primeira variavel
while x <= 5: # Enquanto o valor de x for menor que 5 a operação se repetirá
    y = 1 # Define a variavel y e reseta ela quando o proximo laço chegar ao fim
    while y <= 5: # Enquanto o valor de y for menor que 5 a operação se repetirá
        print(f'{x= } {y= } ') # Mostra em tela os valores de suas repetições
        y += 1 # Soma mais 1 a variavel y até q ela chegue ao valor de 5
    x += 1  # Soma mais 1 a variavel x até que ela chegue ao valor de 5

print('Acabou!')

# -------------------------------------------------------------------------------------------------------------------------
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break  # Quando o loop alcança um valor desejado, o break faz com que aquele loop se encerre

    print(x)
    x = x + 1

print('Acabou')

# -------------------------------------------------------------------------------------------------------------------------
x = 0 # Variável de valor 0

while x < 10: # Enquanto a variável for menor que 10
    x += 1 # Soma mais 1 a variável

    if x == 3: # Quando a soma chegar em 3
        print('Não vou mostrar o 3') # Será exibido essa mensagem na tela
        continue  # Então o continue pulará a exibição do valor 3 porém não vai parar a execução, seguirá normalmente até o fim 

    print(x) # Exibe cada novo valor do laço

print('Acabou') # Quando chegar no 10 termina a execução com essa mensagem

# -------------------------------------------------------------------------------------------------------------------------
x = 0
while x <= 100:  # Laço que verifica se o x é menor que 100, se ele for menor ele soma mais 1
    print(x)
    x += 1

print('Acabou')
# -------------------------------------------------------------------------------------------------------------------------

while True:  # Cria um laço infinito
    nome = input("Qual é o seu nome? ")
    print(f'Olá {nome}!')
# -------------------------------------------------------------------------------------------------------------------------

# Debuggar é testar linha por linha do código




while True:
    print()
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')

    if not n1.isnumeric() or not n2.isnumeric():
        print('Você não digitou um número!!!!')
        continue

    n1 = int(n1)
    n2 = int(n2)

    if operador == '+':
        print(n1 + n2)
        break
    elif operador == '-':
        print(n1 - n2)
        break
    elif operador == '*':
        print(n1 * n2)
        break
    elif operador == '/':
        print(n1 / n2)
        break
    else:
        print('erro')
        break
