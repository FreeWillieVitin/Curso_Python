"""
Formatar valores com modificadores.

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO DE CASAS DECIMAIS)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
div = num1 / num2
print('{:.2f}'.format(div))
print(f'{div:.2f}')

nome = 'Victor Hugo'
print(f'{nome:s}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

num_3 = 1150
print(f'{num_3:0^10}')

#  Uso de indices
nome = 'victor'
nome = nome.ljust(20,'#')  # Retorna 20 caracteres justificados a esquerda da palavra
sobrenome = 'Hugo'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)  # adiciona caracteres as strings
print(nome_formatado)
print(nome.lower())  # Tudo minusculo
print(nome.upper())  # Tudo Maiusculo
print(nome.title())  # As primeiras letras maiusculas
