"""
Factory method é um padrão de criação que permite definir uma interface para criar objetos,
mas deixa as subclasses decidirem quais objetos criar.
O Factory method permite adiar a instanciação para as subclasses, garantindo o baixo acomplamento entre classes.
"""
from abc import ABC, abstractmethod


class veiculo1(ABC):
    @abstractmethod
    def buscar_cliente1(self) -> None: pass


class CarroLuxo1(veiculo1):
    def buscar_cliente1(self) -> None:
        print('Carro de luxo está buscando o cliente...')


class CarroPopular1(veiculo1):
    def buscar_cliente1(self) -> None:
        print('Carro popular está buscando o cliente...')


class Moto1(veiculo1):
    def buscar_cliente1(self) -> None:
        print('Moto está buscando o cliente...')


class MotoLuxo1(veiculo1):
    def buscar_cliente1(self) -> None:
        print('Moto de luxo está buscando o cliente...')


class VeiculoFactory1(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro1(tipo)

    @staticmethod
    @abstractmethod
    def get_carro1(tipo: str) -> veiculo1:  # type: ignore
        ...

    def buscar_cliente1(self):
        self.carro.buscar_cliente1()


class Filial1Factory(VeiculoFactory1):
    @staticmethod
    def get_carro1(tipo: str) -> veiculo1:  # type: ignore
        if tipo == 'luxo':
            return CarroLuxo1()
        if tipo == 'popular':
            return CarroPopular1()
        if tipo == 'moto':
            return Moto1()
        if tipo == 'moto_luxo':
            return MotoLuxo1()
        assert 0, 'Veículo não existe'


class Filial2Factory(VeiculoFactory1):
    @staticmethod
    def get_carro1(tipo: str) -> veiculo1:  # type: ignore
        if tipo == 'popular':
            return CarroPopular1()
        assert 0, 'Veículo não existe'


if __name__ == "__main__":
    from random import choice
    veiculos_filial1 = ['luxo', 'popular', 'moto', 'moto_luxo']
    veiculos_filial2 = ['popular']

    print('Filial 1')
    for i in range(10):
        carro1 = Filial1Factory(choice(veiculos_filial1))
        carro1.buscar_cliente1()

    print()

    print('Filial 2')
    for i in range(10):
        carro1 = Filial2Factory(choice(veiculos_filial2))
        carro1.buscar_cliente1()
print()
