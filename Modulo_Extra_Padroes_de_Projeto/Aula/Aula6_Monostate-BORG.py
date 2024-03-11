"""
Monostate (ou Borg) - É uma variação do Singleton proposto por Alex Martelli
que tem a intenção de garantir que o estado do objeto seja igual para todas
as instâncias.
"""
from matplotlib.pyplot import cla


class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class A(StringReprMixin):
    def __init__(self, nome):
        self.x = 40
        self.y = 20
        self.nome = nome


a = A('Victor')
print(a.__dict__)
print(a)
print()


class MonoStateSimple(StringReprMixin):
    _state: dict = {
        'x': 10,
        'y': 20,
    }

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == "__main__":
    m1 = MonoStateSimple('Victor')
    m2 = MonoStateSimple(sobrenome='Hugo')
    m1.x = 'Qualquer Coisa'  # type: ignore
    print(m1)
    print(m2)
    print()


class MonoStateNotSimple(StringReprMixin):
    _state1: dict = {
        'x': 10,
        'y': 20,
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state1
        return obj

    def __init__(self, nome=None, sobrenome=None):

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


class B(MonoStateNotSimple):
    pass


if __name__ == "__main__":
    m3 = MonoStateNotSimple('Kleber')
    m4 = B(sobrenome='Hugo')
    m1.x = 'Qualquer Coisa'  # type: ignore
    print(m3)
    print(m4)
    print()
