"""
Operador or em Python
"""

nome = input('QUal o seu nome? ')
msg = print(nome) if nome else print('Vazio')

print(nome or 'Você não digitou nada')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Victor'

var = a or b or c or d or e or f or g
print(var)