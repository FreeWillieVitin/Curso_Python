"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que
podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe podem usar seus dados
internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de
classes.
"""
string = 'Victor'  # str
print(string.upper())
print(isinstance(string, str))
print()

class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'Victor'
p1.sobrenome = 'Hugo'

p2 = Pessoa()
p2.nome = 'Marieli'
p2.sobrenome = 'Stankievski'

print(p1.nome)
print(p1.sobrenome)
print()
print(p2.nome)
print(p2.sobrenome)