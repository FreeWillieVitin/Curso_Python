"""
Iterator é um padrão comportamental que tem a intenção
de fornecer um meio de acessar, sequencialmente,
os elementos de um objeto agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.

Aggregate = Iteravel, objeto com os dados
Iterator = Objeto que transcorre pelos dados
"""
from collections.abc import Iterable, Iterator
from typing import List, Any


class MeuIterador(Iterator):
    def __init__(self, minha_lista: List[Any]) -> None:
        self._minha_lista = minha_lista
        self._index = 0

    def __next__(self):
        try:
            item = self._minha_lista[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class MeuIteradorReverso(Iterator):
    def __init__(self, minha_lista: List[Any]) -> None:
        self._minha_lista = minha_lista
        self._index = -1

    def __next__(self):
        try:
            item = self._minha_lista[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MinhaLista(Iterable):
    def __init__(self) -> None:
        self._item: List[Any] = []
        self._meu_iterator = MeuIterador(self._item)

    def add(self, valor: Any) -> None:
        self._item.append(valor)

    def __iter__(self):
        return self._meu_iterator
        # return MeuIterador(self._item)

    def iterador_reverso(self) -> Iterator:
        return MeuIteradorReverso(self._item)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._item})'


if __name__ == "__main__":
    Iteravel = MinhaLista()
    Iteravel.add('Victor')
    Iteravel.add('MArieli')
    Iteravel.add('Judite')
    Iteravel.add('Luiz')

    for valor in Iteravel:
        print(valor)

    print()

    for valor in Iteravel.iterador_reverso():
        print(valor)
    # print(Iteravel)
