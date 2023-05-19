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
class Classe: # Criação da classe
    @staticmethod # Decorador que indica o inicio de um método estatico
    def funcao_que_esta_na_classe(*args, **kwargs): # Estrutura do método estatico é igual ao de uma função, por que é uma função
        print('OOi', args, kwargs) # Métodos estaticos são funções criadas dentro de uma classe para unico fim de organizar o código, em um método estático não se usa nenhum tipo de argumento da classe como o self, cls e não tem acesso direto aos atributos
    # Esses métodos sempre são iniciados com o decorador @staticmethod
def funcao(*args, **kwargs): # Função que faz exatamente a mesma coisa que o método estático, que é exibir a palavra oi e seus argumentos
        print('OOi', args, kwargs)

c1 = Classe()
c1.funcao_que_esta_na_classe(1,2,3) # Executando o método estático com argumentos não nomeados
Classe.funcao_que_esta_na_classe(nomeado=1) # Executando o método estático com argumentos nomeados
funcao(1,2,3) # Executando a função com argumentos não nomeados
funcao(nomeado=1) # Executando a função com argumentos nomeados
print()

"""
Comparação entre method, @classmethod e @staticmethod
method - self, método de instância
@classmethod - cls, método de classe
@staticmethod - método estático
"""
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): # setter
        self.user = user

    def set_password(self, password): # setter
        self.password = password

    @classmethod
    def create_user_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG:', msg)

        
c1 = Connection()
c1.set_user('FreeWillie')
c1.set_password('123456')
print(c1.user)
print(c1.password)
print()

c2 = Connection.create_user_auth('Victor', 'teste')
print(c2.user)
print(c2.password)
print()

c3 = Connection.log('Essa é a mensagem de log')

