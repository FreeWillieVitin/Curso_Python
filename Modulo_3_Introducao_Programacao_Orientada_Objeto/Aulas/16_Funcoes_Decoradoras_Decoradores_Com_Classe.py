"""
Funções decoradoras e decoradores com classe
"""
from typing import Any


def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls

class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    
@adiciona_repr
class Time:
    def __init__(self, nome) -> None:
        self.nome = nome 

    #     def __repr__(self):
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr

class Planeta(MyReprMixin):
    def __init__(self, nome) -> None:
        self.nome = nome 

    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr

# Time = adiciona_repr(Time)

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
jupiter = Planeta('Jupiter')

print(brasil)
print(portugal)
print(terra)
print(jupiter)
print()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Funções decoradoras e decoradores com métodos
"""
def rapper(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

def add_rapper(cls):
    cls.__repr__ = rapper
    return cls

def meu_carro(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        # if 'Gol' in resultado:
        #     return('O Carro do vò')
        return resultado
    return interno

@add_rapper
class Carro:
    def __init__(self, nome):
        self.nome = nome
    @meu_carro
    def falar_nome(self):
        return f'O carro é {self.nome}'

fiat = Carro('Fiat')
gol = Carro('Gol')

print(fiat.falar_nome())
print(gol.falar_nome())
print()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Classes decoradoras (Decorator classes)
"""
class Multiplicar:
    def __init__(self, valor):
        self.valor = valor
        self._multiplicador = 10

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        resultado1 = self.valor(*args, **kwargs)
        return resultado1 * self._multiplicador

@Multiplicar
def soma(x, y):
    return x * y

conta = soma(2, 8)
print(conta)