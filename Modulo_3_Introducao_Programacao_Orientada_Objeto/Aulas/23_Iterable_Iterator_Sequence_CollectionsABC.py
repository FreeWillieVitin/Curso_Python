"""
Implementando o protocolo do Iterator em Python
Essa é apenas uma aula para introduzir os protocolos de collections.abc no
Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
estrutura usada nessa aula.
https://docs.python.org/3/library/collections.abc.html
"""
from collections.abc import Iterable, Iterator, Sequence
from typing import Iterator

class MinhaLista(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_item = 0

    def append(self, valor):
        self._data[self._index] = valor
        self._index += 1

    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self):
        if self._next_item >= self._index:
            raise StopIteration

        value = self._data[self._next_item]
        self._next_item += 1
        return value

    def __len__(self):
        return self._index
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, valor):
        self._data[index] = valor

if __name__ == '__main__':
    lista = MinhaLista()
    lista.append('Victor')
    lista[0] = 'Luiz'
    lista.append('Marieli')
    print(lista._data)

    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')