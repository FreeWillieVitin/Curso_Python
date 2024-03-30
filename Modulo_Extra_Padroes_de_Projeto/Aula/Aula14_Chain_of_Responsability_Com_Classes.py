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
    def __init__(self) -> None:
        self.sucessor: Handler

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
        return self.sucessor.handle(letra)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler):
        self.letras = ['D', 'E', 'F']
        self.sucessor = sucessor

    def handle(self, letra: str) -> str:
        if letra in self.letras:
            return f'FunçãoDEF: tratou o valor {letra}'
        return self.sucessor.handle(letra)


class NaoTrata(Handler):
    def handle(self, letra: str) -> str:
        return f'Não consegui tratar o valor {letra}'


if __name__ == "__main__":
    handler_nao = NaoTrata()
    handler_def = HandlerDEF(handler_nao)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))
    print()
    print(handler_abc.handle('D'))
    print(handler_abc.handle('E'))
    print(handler_abc.handle('F'))
    print()
    print(handler_abc.handle('G'))
    print(handler_abc.handle('H'))
    print()
    print(handler_def.handle('A'))
    print(handler_def.handle('D'))
    print(handler_def.handle('I'))
