"""
GOF - Memento é um padrão de projeto comportamental
que tem a intenção de permitir que voce salve e restaure
um estado anterior de um objeto originator sem revelar os
detalhes da sua implementação e sem violar o encapsulamento.

Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armazenar mementos.
Caretaker também é usado com o Padrão Command.
"""
from __future__ import annotations
from typing import Dict, List
from copy import deepcopy


class Memento:
    def __init__(self, estado: Dict) -> None:
        self._estado: Dict
        super().__setattr__('_estado', estado)

    def get_estado(self) -> Dict:
        return self._estado

    def __setattr__(self, name, value) -> None:
        raise AttributeError('Desculpe, sou imutavel')


class EditorImagem:
    def __init__(self, nome: str, largura: int, altura: int) -> None:
        self.nome = nome
        self.largura = largura
        self.altura = altura

    def save_estado(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restaura(self, memento: Memento) -> None:
        self.__dict__ = memento.get_estado()

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'


class Caretaker:
    def __init__(self, originator: EditorImagem):
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_estado())

    def restaura(self) -> None:
        if not self._mementos:
            return

        self._originator.restaura(self._mementos.pop())


if __name__ == "__main__":
    img = EditorImagem('Foto.jpg', 111, 111)
    caretaker = Caretaker(img)

    caretaker.backup()

    img.nome = 'Foto2.jpg'
    img.altura = 222
    img.largura = 333

    caretaker.backup()

    img.nome = 'Foto3.jpg'
    img.altura = 444
    img.largura = 555
    print(img)

    caretaker.restaura()

    print(img)
