"""
Chain of Responsability (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""


# Implementando com função
def HandlerABC(letra: str) -> str:
    letras = ['A', 'B', 'C']

    if letra in letras:
        return f'FunçãoABC: tratou o valor {letra}'
    return HandlerDEF(letra)


def HandlerDEF(letra: str) -> str:
    letras = ['D', 'E', 'F']

    if letra in letras:
        return f'FunçãoDEF: tratou o valor {letra}'
    return HandlerNaoTrata(letra)


def HandlerNaoTrata(letra: str) -> str:
    return f'handler nao trata {letra}'


if __name__ == "__main__":
    print(HandlerABC('A'))
    print(HandlerABC('B'))
    print(HandlerABC('C'))
    print(HandlerABC('D'))
    print(HandlerABC('E'))
    print(HandlerABC('F'))
    print(HandlerABC('G'))
