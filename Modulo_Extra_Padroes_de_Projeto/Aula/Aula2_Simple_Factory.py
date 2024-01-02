"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory)

    Podem facilitar o processo de "cache" ou a criação de "Singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código
"""
from abc import ABC, abstractmethod


# Classe que herda a classe abstrata, essa classe no simple factory seria o produto de forma abstrata, as classes fábricas criaram
# métodos que serão usados pelo cliente, o produto é sempre abstrato e apartir dele é que temos os produtos concretos
class veiculo(ABC):  # Classe abstrata
    @abstractmethod
    def buscar_cliente(self) -> None: pass  # Método abstrato


class CarroLuxo(veiculo):  # Classe que herda da classe abstrata, o que chamamos de classe concreta, ou produto concreto
    def buscar_cliente(self) -> None:  # Método que implementa o método abstrato
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente...')


class Moto(veiculo):
    def buscar_cliente(self) -> None:
        print('Moto está buscando o cliente...')


# A classe a seguir é a classe factory(fábrica), ela que disponibliza as classes abstratas e seus métodos para o uso do cliente
class VeiculoFactory:
    @staticmethod
    # Através da condicional abaixo será executado a classe abstrata
    def get_carro(tipo: str) -> veiculo:  # type: ignore
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        assert 0, 'Veículo não existe'


if __name__ == "__main__":  # Enfim temos o cliente, ele receberá o retorno do que for criado pelas fábricas
    from random import choice  # Módulo random importado para usar a função choice que escolher um valor aleatoriamente
    carros_disponiveis = ['luxo', 'popular', 'moto']  # Lista com as opções que o cliente terá, que são os mesmos tipos na fábrica

    for i in range(10):  # Iteramos 10 vezes
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))  # Armazenamos em variável os produtos gerados pela fábrica
        carro.buscar_cliente()  # Com isso executamos o método de cada produto
print()

# --------------------------------------------------------------------------------------------------------------------------------
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


class VeiculoFactory1:
    def __init__(self, tipo):
        self.carro = self.get_carro1(tipo)

    @staticmethod
    def get_carro1(tipo: str) -> veiculo1:  # type: ignore
        if tipo == 'luxo':
            return CarroLuxo1()
        if tipo == 'popular':
            return CarroPopular1()
        if tipo == 'moto':
            return Moto1()
        assert 0, 'Veículo não existe'

    def buscar_cliente1(self):
        self.carro.buscar_cliente1()


if __name__ == "__main__":
    from random import choice
    carros_disponiveis1 = ['luxo', 'popular', 'moto']

    for i in range(10):
        carro1 = VeiculoFactory1(choice(carros_disponiveis1))
        carro1.buscar_cliente1()
print()
