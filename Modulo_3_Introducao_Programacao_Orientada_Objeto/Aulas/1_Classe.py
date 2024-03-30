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
print()
# -----------------------------------------------------------------------------------------------------------------------------------------

"""
Mantendo estados dentro da classe
No exemplo abaixo, podemos observar como podemos alterar o comportamento de objetos dentro da classe atráves de funções
temos uma câmera que transita-rá de parada, para filmando e fotografando apenas executando suas funções
"""
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar, câmera filmando...')
            return
        
        print(f'{self.nome} está fotografando...')

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar() # Podemos observar a existência de 2 objetos e que a execução de cada um se comporta da sua própria maneira independente se é usada as mesmas funções da classe
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
print()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()