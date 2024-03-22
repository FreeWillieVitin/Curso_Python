"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possivel definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood Principle: "Don't Call Us, We'll Call You"
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    # Classe abstrata
    def prepara(self):
        # Template Method
        self.hook_antes()
        self.add_ingredientes()  # Abstract
        self.hook_depois()
        self.cozinhar()  # Abstract
        self.cortar()
        self.servir()

    def hook_antes(self):
        pass

    def hook_depois(self):
        pass

    def cortar(self):
        print(f'{self.__class__.__name__}: Cortando Pizza')

    def servir(self):
        print(f'{self.__class__.__name__}: Servindo Pizza')

    @abstractmethod
    def add_ingredientes(self):
        pass

    @abstractmethod
    def cozinhar(self):
        pass


class Marguerita(Pizza):
    def add_ingredientes(self):
        print('Marguerita: Queijo, Tomate, Manjericão')

    def cozinhar(self):
        print('Marguerita: Cozinhando por 30min')


class Doce(Pizza):
    def hook_antes(self):
        print('Temperando o Chocolate')

    def add_ingredientes(self):
        print('Chocolate: Chocolate Preto, Granulado')

    def hook_depois(self):
        print('Checar aos 15min')

    def cozinhar(self):
        print('Chocolate: Cozinhando por 30min')


if __name__ == "__main__":
    marguerita = Marguerita()
    doce = Doce()
    marguerita.prepara()
    print()
    doce.prepara()
