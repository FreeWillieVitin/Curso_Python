"""
While em Python
utilizado para realizar ações enquanto uma condição for verdadeira

while = enquanto
"""

while True:  # Cria um laço infinito
    nome = input("Qual é o seu nome? ")
    print(f'Olá {nome}!')

x = 0
while x < 100:  # Laço que verifica se o x é menor que 100, se ele for menor ele soma mais 1
    print(x)
    x = x + 1

print('Acabou')
# Debuggar é testar linha por linha do código

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue  # Ignora uma parte do ‘loop’ criado pelo while, mas não para a execução dele, continua com o resto do
# o resto do loop

    print(x)
    x = x + 1

print('Acabou')

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break  # Quando o loop alcança um valor desejado, o break faz com que aquele loop se encerre

    print(x)
    x = x + 1

print('Acabou')

x = 0

while x < 10:
    y = 0

    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1

    x += 1  # x = x + 1

print('Acabou!')

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
