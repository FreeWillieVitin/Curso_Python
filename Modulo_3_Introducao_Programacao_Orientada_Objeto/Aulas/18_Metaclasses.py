"""
Metaclasses são o tipo das classes
EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
Então, qual é o tipo de uma classe? (type)
Seu objeto é uma instância da sua classe
Sua classe é uma instância de type (type é uma metaclass)
type('Name', (Bases,), __dict__)

Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
__new__ da metaclass é chamado e cria a nova classe
__call__ da metaclass é chamado com os argumentos e chama:
  __new__ da class com os argumentos (cria a instância)
  __init__ da class com os argumentos
__call__ da metaclass termina a execução

Métodos importantes da metaclass
__new__(mcs, name, bases, dct) (Cria a classe)
__call__(cls, *args, **kwargs) (Cria e inicializa a instância)

"Metaclasses são magias mais profundas do que 99% dos usuários
deveriam se preocupar. Se você quer saber se precisa delas,
não precisa (as pessoas que realmente precisam delas sabem
com certeza que precisam delas e não precisam de uma explicação
sobre o porquê)."
— Tim Peters (CPython Core Developer)
"""
# object acima
from typing import Any


class Foo:
    ...


Foo = type('Foo', (object,), {}) # Essa linha de código é a forma visível da estrutura de criação de uma classe em python, a criação da classe começa apartir de uma metaclasse
f = Foo() # Acima temos a classe a ser criada Foo, de onde ela é herdade, como sempre a classe principal herda da classe object e o seu dicionario
print(isinstance(f, Foo))
print(type(f))
print(type(Foo))
print()
def meu_repr(self):
    return f'{type(self).__name__} ({self.__dict__})'

class Meta(type): # Podemos também criar nossas metaclasses para que executem prioritariamente quando executamos alguma classe criada por ela
    def __new__(mcs, name, bases, dct): # A crição da metaclasse parte de um método new com os seus argumentos
        print('MetaClass New') # Antes de qualquer ação de uma classe o python mostrará a mensagem pois a metaclass traz essa prioridade
        cls = super().__new__(mcs, name, bases, dct) # Aqui criamos uma instancia para receber a metaclass
        cls.attr = 1234 # Podendo então usar essa instancia para criar execução para as classes futuras que partiram dessa metaclasse como por exemplo está ação que mostrará 1234 se a função attr for chamada
        cls.__repr__ = meu_repr

        print(cls.__dict__)
        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError ('Implemente Falar')
        return cls
    
    def __call__(self, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        print(instancia.__dict__)
        return instancia

class Pessoa(metaclass=Meta): # Aqui temos a primeira classe criada apartir da metaclasse anterior
    def __new__(cls, *args, **kwargs):
        print('Meu New')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome) -> None:
        print('Meu Init')
        self.nome = nome

    def falar(self):
        print('Falando ...')

p1 = Pessoa('Victor')
p1.falar()
print(p1.attr)
print(p1)
# -------------------------------------------------------------------------------------------------------------------------------------------
