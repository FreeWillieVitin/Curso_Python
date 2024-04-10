"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from django.dispatch import receiver


class Colleague(ABC):
    def __init__(self) -> None:
        self.nome: str

    @abstractmethod
    def broadcast(self, msg: str) -> None:
        pass

    @abstractmethod
    def direct(self, msg: str) -> None:
        pass


class Pessoa(Colleague):
    def __init__(self, nome: str, mediator: Mediator) -> None:
        self.nome = nome
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.mostrar(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direto(self, receiver, msg)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def mostrar(self, pessoa: Colleague, msg: str) -> None:
        pass

    @abstractmethod
    def direto(self, sender: Colleague, receptor: str, msg: str) -> None:
        pass


class Chat(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def colega_existe(self, colega: Colleague) -> bool:
        return colega in self.colleagues

    def add(self, colega: Colleague) -> None:
        if not self.colega_existe(colega):
            self.colleagues.append(colega)

    def remove(self, colega: Colleague) -> None:
        if self.colega_existe(colega):
            self.colleagues.remove(colega)

    def mostrar(self, pessoa: Colleague, msg: str) -> None:
        if not self.colega_existe(pessoa):
            return
        print(f'{pessoa.nome} enviou: {msg}')

    def direto(self, sender: Colleague, receptor: str, msg: str) -> None:
        if not self.colega_existe(sender):
            return

        receptor_obj: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.nome == receptor
        ]

        if not receptor_obj:
            return

        receptor_obj[0].direct(
            f'{sender.nome} para {receptor_obj[0].nome}: {msg}'
        )


if __name__ == "__main__":
    chat = Chat()

    victor = Pessoa('Victor', chat)
    Marieli = Pessoa('Marieli', chat)
    Luiz = Pessoa('Luiz', chat)
    Judite = Pessoa('Judite', chat)

    chat.add(victor)
    chat.add(Marieli)
    chat.add(Judite)
    chat.add(Luiz)

    victor.broadcast('Olá galera')
    Marieli.broadcast('E aí')
    print()

    victor.send_direct('Marieli', 'Oi amor')
    Marieli.send_direct('Victor', 'Eu te amo')
