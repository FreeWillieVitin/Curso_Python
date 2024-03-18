"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""
from __future__ import annotations
from typing import List
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Pessoa(StringReprMixin):
    def __init__(self, f_name: str, l_name: str):
        self.f_name = f_name
        self.l_name = l_name
        self.endereco: List[Endereco] = []

    def add_endereco(self, end: Endereco) -> None:
        self.endereco.append(end)

    def clone(self) -> Pessoa:
        return deepcopy(self)


class Endereco(StringReprMixin):
    def __init__(self, rua: str, numero: str):
        self.rua = rua
        self.numero = numero


if __name__ == "__main__":
    p = Pessoa('Victor', 'Hugo')
    end_p = Endereco('Rua Sem Saída', '121')
    p.add_endereco(end_p)

    esposa_p = p.clone()
    esposa_p.f_name = 'Marieli'
    print(p)
    print(esposa_p)
