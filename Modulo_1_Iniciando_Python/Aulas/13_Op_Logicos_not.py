"""
Operador not em Python
and, or, not, in, not in

Usado para inverter expressões
not: se nao existir nada dentro de uma variavel ou ela for igual a zero vai retornar true
not True = False
not False = True
"""

a = 2
b = 3

if not b > a:  # Se b não for maior que a faça alguma coisa
    print('B é maior do que A')
else:
    print('A é maior do que B')

x = ''
y = 0

if not x:
    print('valor vazio')

print(not True)
print(not False)
