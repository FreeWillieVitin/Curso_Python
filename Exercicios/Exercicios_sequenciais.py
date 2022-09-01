# Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Alo Mundo')

# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
num1 = input('Digite um numero: ')
print(f'O número informado foi {num1}.')

# Faça um Programa que peça dois números e imprima a soma.
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite outro numero: '))
print(num2 + num3)

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = [int(input('Digite a nota do aluno: '))]

while len(notas) < 4:
    notas.append(int(input('Digite a nota do aluno: ')))
else:
    print(sum(notas)/4)

# Faça um Programa que converta metros para centímetros.
metros = float(input('Digite o tamanho: '))
print('O valor {}m em centimetros é {:.0f}cm'.format(metros, metros * 100))
print('O valor {}m em milimetros é {:.0f}mm'.format(metros, metros * 1000))

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input('Digite o raio do circulo: '))
pi = 3.14
print('O area do circulo é de {}'.format(pi * raio**2))

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
largura = float(input('Digite a largura do quadrado: '))
dobro = largura ** 2 * 2
print('A area do quadrado é de {}'.format(largura**2))
print(dobro)

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
salario = float(input('Quanto você ganha por hora? '))
hora = int(input('Quantas horas você trabalha? '))
print('O seu salário é de {}'.format(salario * hora))

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
f = int(input('Digite a temperatura em Fahrenheit: '))
c = 5 * ((f-32) / 9)
print('Sua temperatura em Celsius é de {}'.format(c))

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
c= int(input('Digite a temperatura em Celsius: '))
f = (c * 1.8 + 32)
print('Sua temperatura em Fahrenheit é de {}'.format(f))

"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
#
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).