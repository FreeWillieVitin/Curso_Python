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

class Pessoa: # Classe é o que cria objetos
    def __init__(self, nome, sobrenome): # Na criação de uma classe pprecisamos passar uma função inicializadora, sua estrutura é exatamente igual a de uma função, a diferença é no seu nome
        # Que sempre será um __init__ e precisamos sempre reservar o primeiro argumento para o self, é a partir do self que criamos os atributos da classe
        self.nome = nome # Um exemplo é o atributo nome, no caso a Classe Pessoa terá sempre que receber um atributo nome e sobrenome
        self.sobrenome = sobrenome # na criação de seus objetos

p1 = Pessoa('Victor', 'Hugo') # Variável são os objetos que por sua vez possuem atributos esses atributos são passados em forma de valores para a variável

p2 = Pessoa('Marieli', 'Stankievski') # O objeto p2 recebe a classe pessoa e nela o seus argumentos, lembrando que o self é um argumento padrão e não precisa de valor, os argumentos passados são referentes ao nome e sobrenome

p3 = Pessoa('Luiz', 'Carlos')

print(p1.nome) # Execução do atributo nome a partir do objeto p1 
print(p1.sobrenome)
print()
print(p2.nome)
print(p2.sobrenome)
print()
print(p3.nome)
print(p3.sobrenome)