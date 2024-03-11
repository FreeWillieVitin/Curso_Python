"""
Builder é um padrão de criação que tem a intenção
de separar a contrução de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos(method chaining).
"""


# Essa é a classe produto, porém da forma q ela é contruída já é uma forma padrão na contrução de atríbutos em python, mas
# para representar o padrão de projeto Builder não será utilizado a contrução tradicional do python que é a seguinte no comentário
# class Usuario:
#     def __init__(self, f_name=None):
#         self.f_name = f_name
from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Usuario(StringReprMixin):
    def __init__(self):
        self.f_name = None
        self.l_name = None
        self.age = None
        self.phone = []
        self.adress = []


class IBuilderUsuario(ABC):
    @property
    @abstractmethod
    def resultado(self): pass

    @abstractmethod
    def add_f_name(self, f_name): pass

    @abstractmethod
    def add_l_name(self, l_name): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_adress(self, adress): pass


class BuilderUsuario(IBuilderUsuario):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._result = Usuario()

    @property
    def resultado(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_f_name(self, f_name):
        self._result.f_name = f_name
        return self

    def add_l_name(self, l_name):
        self._result.l_name = l_name
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone):
        self._result.phone.append(phone)
        return self

    def add_adress(self, adress):
        self._result.adress.append(adress)
        return self


class UserDirector:
    def __init__(self, builder):
        self._builder: BuilderUsuario = builder

    def com_idade(self, f_name, l_name, age):
        self._builder.add_f_name(f_name)
        self._builder.add_l_name(l_name)
        self._builder.add_age(age)
        return self._builder.resultado

    def com_endereco(self, f_name, l_name, adress):
        self._builder.add_f_name(f_name)
        self._builder.add_l_name(l_name)
        self._builder.add_adress(adress)
        return self._builder.resultado

    def com_tudo(self, f_name, l_name, age, phone, adress):
        self._builder.add_f_name(f_name)\
            .add_l_name(l_name)\
            .add_f_name(age)\
            .add_phone(phone)\
            .add_adress(adress)
        return self._builder.resultado


if __name__ == "__main__":
    user_builder = BuilderUsuario()
    user_director = UserDirector(user_builder)
    usuario1 = user_director.com_idade('Victor', 'Hugo', 26)
    usuario2 = user_director.com_endereco('Victor', 'Hugo', 'Rua Madre Inês')
    usuario3 = user_director.com_tudo('Marieli', 'Stankievski', 25, 997718039, 'Rua Esqueci o Nome')
    print(usuario1)
    print(usuario2)
    print(usuario3)
