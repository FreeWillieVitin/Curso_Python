"""
Abstract Factory é um padrão de criação que fornece uma interface para criar famílias de objetos relacionados ou dependentes sem
especificar suas classes concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o Factory Method usa herança, enquanto o Abstract Factory
usa a composição.

Princípio: Programe para interfaces, não para implementações
"""
from abc import ABC, abstractmethod


# Diferente do modelo anterior, agora dividimos a classe de veículos em duas interfaces para cada modelo de carro, ambas
# são compostas pelo método buscar_cliente1 porém cada uma tem a sua família de objetos, uma para os veículos de luxo e outra
# para os populares
class veiculoLuxo(ABC):  # Classe abstrata que chamamos de produto
    @abstractmethod
    def buscar_cliente1(self) -> None:  # Método abstrato
        pass


class veiculoPopular(ABC):  # Classe abstrata que chamamos de produto
    @abstractmethod
    def buscar_cliente1(self) -> None:  # Método abstrato
        pass


# Cada objeto de tipo de veículo herda a função da classe respectiva a classificação do veículo se é de luxo ou popular, dessa
# forma não usamos a mesma classe para categorias diferentes e limitamos o uso de algumas condicionais
class CarroLuxoFilial1(veiculoLuxo):
    def buscar_cliente1(self) -> None:
        print('Carro de luxo da Filial1 está buscando o cliente...')


class CarroPopularFilial1(veiculoPopular):
    def buscar_cliente1(self) -> None:
        print('Carro popular da Filial1 está buscando o cliente...')


class MotoFilial1(veiculoPopular):
    def buscar_cliente1(self) -> None:
        print('Moto da Filial1 está buscando o cliente...')


class MotoLuxoFilial1(veiculoLuxo):
    def buscar_cliente1(self) -> None:
        print('Moto de luxo da Filial1 está buscando o cliente...')


class CarroLuxoFilial2(veiculoLuxo):
    def buscar_cliente1(self) -> None:
        print('Carro de luxo da Filial2 está buscando o cliente...')


class CarroPopularFilial2(veiculoPopular):
    def buscar_cliente1(self) -> None:
        print('Carro popular da Filial2 está buscando o cliente...')


class MotoFilial2(veiculoPopular):
    def buscar_cliente1(self) -> None:
        print('Moto da Filial2 está buscando o cliente...')


class MotoLuxoFilial2(veiculoLuxo):
    def buscar_cliente1(self) -> None:
        print('Moto de luxo da Filial2 está buscando o cliente...')


# Agora teremos um método para cada tipo de veículo que é criado apartir da classe que o classifica
class VeiculoFactory1(ABC):
    # def __init__(self, tipo):
    #     self.carro = self.get_carro1(tipo)

    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> veiculoLuxo:
        ...

    def get_carro_popular() -> veiculoPopular:  # type: ignore
        ...

    def get_moto_luxo() -> veiculoLuxo:  # type: ignore
        ...

    def get_moto_popular() -> veiculoPopular:  # type: ignore
        ...

    # def buscar_cliente1(self):
    #     self.carro.buscar_cliente1()


# Como dito acima, eliminamos o uso de condicionais como no exemplo anterior que havia as condicionais if para cada vaículo
# agora tudo é retornado com base nos métodos criados pela fábrica em que cada método é para cada tipo de veículo e se for
# necessário a criação de mais tipos apenas adicionamos outro método na Factory, damos a sua classificação e aplicamos na filial
# correspondente
class Filial1Factory(VeiculoFactory1):
    @staticmethod
    def get_carro_luxo() -> veiculoLuxo:
        return CarroLuxoFilial1()

    @staticmethod
    def get_carro_popular() -> veiculoPopular:  # type: ignore
        return CarroPopularFilial1()

    @staticmethod
    def get_moto_luxo() -> veiculoLuxo:  # type: ignore
        return MotoLuxoFilial1()

    @staticmethod
    def get_moto_popular() -> veiculoPopular:  # type: ignore
        return MotoFilial1()


class Filial2Factory(VeiculoFactory1):
    @staticmethod
    def get_carro_luxo() -> veiculoLuxo:
        return CarroLuxoFilial2()

    @staticmethod
    def get_carro_popular() -> veiculoPopular:  # type: ignore
        return CarroPopularFilial2()

    @staticmethod
    def get_moto_luxo() -> veiculoLuxo:  # type: ignore
        return MotoLuxoFilial2()

    @staticmethod
    def get_moto_popular() -> veiculoPopular:  # type: ignore
        return MotoFilial2()


# Então usando composição criamos a classe que vai usar a interface Factory
class Filial:
    def busca_clientes(self):
        for factory in [Filial1Factory(), Filial2Factory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente1()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente1()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente1()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente1()


if __name__ == "__main__":
    cliente = Filial()
    cliente.busca_clientes()
print()
