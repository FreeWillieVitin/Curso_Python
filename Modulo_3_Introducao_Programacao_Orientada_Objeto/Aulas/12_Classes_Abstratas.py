"""
Classes abstratas - Abstract Base Class (abc)
ABCs são usadas como contratos para a definição
de novas classes. Elas podem forçar outras classes
a criarem métodos concretos. Também podem ter
métodos concretos por elas mesmas.
@abstractmethods são métodos que não têm corpo.
As regras para classes abstratas com métodos
abstratos é que elas NÃO PODEM ser instânciadas
diretamente.
Métodos abstratos DEVEM ser implementados
nas subclasses (@abstractmethod).
Uma classe abstrata em Python tem sua metaclasse
sendo ABCMeta.
É possível criar @property @setter @classmethod
@staticmethod e @method como abstratos, para isso
use @abstractmethod como decorator mais interno.
"""
from abc import ABC, ABCMeta, abstractmethod

# class Log(metaclass=ABCMeta):
#     pass

class Log(ABC): # A classe que possuir um método abstrado deve herdar a função de abstração da classe ABC
    @abstractmethod # Decorator que indica que o método é um método abstrato
    def _log(self, msg): ... # Método Abstrato não tem sua execução partida da classe da qual ela pertence, a classe abstrata precisa ser implementada por outra classe filha, usando os mesmo padrão de contruçao do método da classe pai
    
    def log_error(self, msg): # Método Concreto pode ser executado diretamente da classe em que ele foi criado
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l.log_error('Oi')
# -----------------------------------------------------------------------------------------------------------------------------------------

"""
abstractmethod para qualquer método já decorado (@property e setter)
É possível criar @property @property.setter @classmethod
@staticmethod e métodos normais como abstratos, para isso
use @abstractmethod como decorator mais interno.
Foo - Bar são palavras usadas como placeholder
para palavras que podem mudar na programação.
"""
print()
class AbstractFoo(ABC): # Classe pai que herda métodos e decoradores da classe ABC responsável pela criação de métodos abstratos
    def __init__(self, name): # Método inicializador
        self._name = None # Criamos primeiramente o atributo protegida _name que é o atributo receptor do valor a ser setado para a property
        self.name = name # O setter passar o valor para a property name para que o valor possa ser retornado
        
    @property
    @abstractmethod
    def name(self): ... # Criação de uma property abstrata, para que a property possa ser abstrata o decorator @abstractmethod precisa estar o mais perto possivel da assinatura do method

    @name.setter # Por haver um property abstrato, precisamos ter uma assinatura de um setter para passar o valor, que é definito não na classe pai quanto na classe filha
    # @abstractmethod O setter também pode ser abstrato e para isso passamos o decorator da mesma forma que na property e para chama-lo nma classe filha usamos o decorator da seguinte forma @NomeDaClassePai.nomedometodo.setter
    def name(self, name): ... #Enfim é passado a assinatura do método setter

class Foo(AbstractFoo):
    # name = ''

    def __init__(self, name):
        super().__init__(name)
        # print('Sou Inútil')

    @property
    def name(self): 
        return self._name

    # @AbstractFoo.name.setter
    @name.setter
    def name(self, name): 
        self._name = name

foo = Foo('Bar')
print(foo.name)
