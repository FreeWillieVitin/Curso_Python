"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro.
"""
num1 = input("Digite um número: ")
if num1.isnumeric():
    num1 = int(num1)
else:
    print(f"{num1} Não é um número inteiro")
    exit()

    if num1 % 2 == 0:
        print(f"{num1} é um número par")
    else:
        print(f"{num1} é um número ímpar")

"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario descrito, exiba a saudação apropriada.
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
hora = input("Que horas são? ")
if hora.isdigit():
    hora = int(hora)
else:
    print("Horário não valido")
    exit()

if 0 <= hora <= 11:
    print("Bom dia")

elif 12 <= hora <= 17:
    print("Boa Tarde")

elif 18 <= hora <= 23:
    print("Boa noite")

else:
    print("Esse valor não é aceito")



"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Digite o seu nome: ")

if len(nome) <= 4:
    print(f"{nome} é um nome curto.")

if 4 < len(nome) < 7:
    print(f"{nome} é um nome normal.")

elif len(nome) > 6:
    print(f"{nome} é um nome grande. ")