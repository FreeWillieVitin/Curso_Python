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


class Abstrata(ABC):
    def template_method(self):
        self.hook()
        self.operação1()
        self.base_class_method()
        self.operação2()

    def hook(self):
        pass

    def base_class_method(self):
        print('Olá eu sou da classe abstrata')

    @abstractmethod
    def operação1(self):
        pass

    @abstractmethod
    def operação2(self):
        pass


class ClasseConcreta1(Abstrata):
    def hook(self):
        print('Utilizando o Hook')

    def operação1(self):
        print('Operação 1 Concluída')

    def operação2(self):
        print('Operação 2 Concluída')


class ClasseConcreta2(Abstrata):
    def operação1(self):
        print('Operação 1 Concluída (de maneira diferente)')

    def operação2(self):
        print('Operação 2 Concluída (de maneira diferente)')


if __name__ == "__main__":
    c1 = ClasseConcreta1()
    c2 = ClasseConcreta2()
    c1.template_method()
    c2.template_method()
