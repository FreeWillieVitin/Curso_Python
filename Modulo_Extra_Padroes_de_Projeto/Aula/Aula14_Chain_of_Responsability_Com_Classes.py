"""
Chain of Responsability (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""
from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, sucessor) -> None:
        self.sucessor: Handler = sucessor

    @abstractmethod
    def handle(self, letter: str) -> str:
        pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler):
        self.letras = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letra: str) -> str:
        if letra in self.letras:
            return f'FunçãoABC: tratou o valor {letra}'
        return HandlerDEF(letra)
