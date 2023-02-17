"""
Operador in e not in em Python
and, or, not, in, not in

in: usado para verificar se existe algo dentro de uma variavel
not in: é o contrario do in, ou seja, se nao existir algo dentro da variavel

Strings são iteráveis
"""

# Exemplo de in
nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} existe em {nome}')
else:
    print(f'{encontrar} não existe em {nome}')
