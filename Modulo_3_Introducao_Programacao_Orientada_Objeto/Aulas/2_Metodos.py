"""
Métodos em instâncias de classes Python
Hard codded - É Algo que  foi escrito diretamente no código
"""
class Carro: # Criamos uma classe e dentro dela teremos nossa função inicializadora e um método, esse método podemos executar no momento de execução do objeto
    def __init__(self, nome): # Função inicializadora definindo sempre o argumento self, e criamos um argumento secundário para receber o nome como parâmetro
        self.nome = nome

    def acelerar(self): # Dentro da classe criamos um método básico que executa uma ação a partir do nome passado como argumento
        print(f'{self.nome} está acelerando...') # Dessa forma o método exibe o valor de atributo passado com sua ação

fusca = Carro('Fusca') # Objeto com seu atributo
print(fusca.nome)
fusca.acelerar() # Objeto executando o método criado na classe

celta = Carro(nome='Celta')
print(celta.nome)
Carro.acelerar(celta)
print()
"""
Entendendo self em classes Python
Classe - Molde(geralmente sem dados)
Instância da class (objeto) - Tem os dados
Uma classe pode gerar várias instâncias.
Na classe o self é a própria instância.
O argumento self tem esse nome apenas por convenção, pois poderia ser qualquer outro nome, mas basicamente o self é o primeiro argumento para
referenciar uma instância
"""
# --------------------------------------------------------------------------------------------------------------------------------------------

"""
Métodos de classe + factories (fábrica)
São métodos onde "self" será "cls", ou seja,
ao invés de receber a instância no primeiro
parâmetro, receberemos a própria classe.
"""
class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

p1 = Pessoa('Victor', 25)
p1.metodo_de_classe()
Pessoa.metodo_de_classe()
print()
p2 = Pessoa.criar_com_50_anos('Judite')
print(p2.nome, p2.idade)
print()
print(Pessoa.ano)
print()
# --------------------------------------------------------------------------------------------------------------------------------------------

"""
@staticmethod (métodos estáticos) 
Métodos estáticos são métodos que estão dentro da classe,
mas não tem acesso ao self nem ao cls.
Em resumo, são funções que existem dentro da sua classe.
"""
class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('OOi', args, kwargs)

def funcao(*args, **kwargs):
        print('OOi', args, kwargs)

c1 = Classe()
c1.funcao_que_esta_na_classe(1,2,3)
Classe.funcao_que_esta_na_classe(nomeado=1)
funcao(1,2,3)
funcao(nomeado=1)