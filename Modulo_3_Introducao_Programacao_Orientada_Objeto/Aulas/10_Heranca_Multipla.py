"""
Herança Múltipla - Python Orientado a Objetos
Quer dizer que no Python, uma classe pode estender
várias outras classes.
Herança simples:
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Herança múltipla e mixins(é uma classe que não faz parte da família)
Log -> FileLog
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Cliente(Pessoa, FileLog)

A, B, C, D
D(B, C) - C(A) - B(A) - A

método -> falar
          A
        /   \
       B     C
        \   /
          D

Python 3 usa C3 superclass linearization
para gerar o mro.
https://en.wikipedia.org/wiki/C3_linearization

Para saber a ordem de chamada dos métodos
Use o método de classe Classe.mro()
Ou o atributo __mro__ (Dunder - Double Underscore)
"""
class A: 
    ...

    def falar(self):
        print('A')

class B(A):
    ...

    def falar(self):
        print('B')

class C(A):
    ...

    def falar(self):
        print('C')

class D(B, C):
    ...

    # def falar(self):
    #     print('D')

falando = D() # Da prioridade de execução a si mesmo ou ao método de classe herdada mais proxima seguindo a ordem do mro
falando.falar()
print(D.mro())
print(D.__mro__)