"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algoritmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/Closed Principle):
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Pedido:
    def __init__(self, total: float, desconto: EstrategiaDesconto) -> None:
        self._total = total
        self._desconto = desconto

    @property
    def total(self):
        return self._total

    @property
    def total_desconto(self):
        return self._desconto.calcular(self.total)


class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass


class Vinte(EstrategiaDesconto):
    def calcular(self, valor: float) -> float:
        return valor - (valor * 0.2)


class Cinquenta(EstrategiaDesconto):
    def calcular(self, valor: float) -> float:
        return valor - (valor * 0.5)


class SemDesconto(EstrategiaDesconto):
    def calcular(self, valor: float) -> float:
        return valor


class DescontoPersonalizado(EstrategiaDesconto):
    def __init__(self, desconto) -> None:
        self.desconto = desconto / 100

    def calcular(self, valor: float) -> float:
        return valor - (valor * self.desconto)


if __name__ == "__main__":
    vinte = Vinte()
    cinquenta = Cinquenta()
    zero = SemDesconto()
    desconto = DescontoPersonalizado(5)

    pedido = Pedido(1000, vinte)
    print(pedido.total, pedido.total_desconto)

    pedido = Pedido(1000, cinquenta)
    print(pedido.total, pedido.total_desconto)

    pedido = Pedido(1000, zero)
    print(pedido.total, pedido.total_desconto)

    pedido = Pedido(1000, desconto)
    print(pedido.total, pedido.total_desconto)

    pedido = Pedido(1000, DescontoPersonalizado(28))
    print(pedido.total, pedido.total_desconto)
