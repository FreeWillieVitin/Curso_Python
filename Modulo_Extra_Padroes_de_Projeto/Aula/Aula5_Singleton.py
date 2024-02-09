"""
O Singleton tem a intenção de garantir que uma classe tenha somente uma instância e fornece um ponto global
de acesso para a mesma.

When discussing which patterns to drop, we found that we still love them all.
(Not really-I'm in favor of dropping smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""


class AppSettings:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls, *args, **kwargs)
        return cls._instancia

    def __init__(self):
        self.tema = 'Tema Escuro'
        self.fonte = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'Tema Claro'
    print(as1.tema)
    as2 = AppSettings()
    print(as1.tema)
    print()

    print(as1)
    print(as1)
    print(as1 == as2)
    print()

    as1.nome = 'Victor'  # type: ignore
    print(as1.nome)  # type: ignore
    print(as2.nome)  # type: ignore
    print()

# --------------------------------------------------------------------------------------------------------------------------------
"""
O maior problema do uso de singleton é que ao usar uma função inicializadora, mesmo o valor do objeto sendo alterado, cada bem que
a classe é instanciada ela volta ao seu estado inicial, ou seja com o valor que foi definido na função init, se a classe não tiver
a função init esse erro obviamente não ocorre, abaixo temos o código que mostra como contornar esse problema gerado pela função
init.
"""


def singleton(a_classe):
    instances = {}

    def get_class(*args, **kwargs):
        if a_classe not in instances:
            instances[a_classe] = a_classe(*args, **kwargs)
        return instances[a_classe]
    return get_class


@singleton
class AppSettings1:
    def __init__(self):
        self.tema1 = 'Tema Escuro'
        self.fonte1 = '18px'


@singleton
class AppSettings2:
    def __init__(self):
        print('OI')


if __name__ == "__main__":
    as3 = AppSettings1()
    as3.tema1 = 'Tema Claro'
    print(as3.tema1)

    as4 = AppSettings1()
    print(as3.tema1)
    print()

    t1 = AppSettings2()
    t2 = AppSettings2()
    print(t1 == t2)
    print()

# --------------------------------------------------------------------------------------------------------------------------------
"""
Singleton usando metaclass
"""


# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('CALL é executado')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW vem Primeiro')
#         return super().__new__(cls)

#     def __init__(self, nome) -> None:
#         print('INIT vem depois')
#         self.nome = nome

#     def __call__(self, x, y) -> Any:
#         print('Chamando o call', self.nome, x + y)


# p1 = Pessoa('Victor')
# p1(2, 2)
# print(p1.nome)

class Meta(type):
    instances2 = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances2:
            cls.instances2[cls] = super().__call__(*args, **kwargs)
        return cls.instances2[cls]


@singleton
class AppSettings3(metaclass=Meta):
    def __init__(self):
        self.tema1 = 'Tema Escuro'
        self.fonte1 = '18px'


if __name__ == "__main__":
    as3 = AppSettings3()
    as3.tema1 = 'Tema Claro'
    print(as3.tema1)

    as4 = AppSettings1()
    print(as3.tema1)
    print(as4.tema1)
    print()
