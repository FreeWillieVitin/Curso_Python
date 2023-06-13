"""
namedtuples - tuplas imutáveis com nomes para valores
Usamos namedtuples para criar classes de objetos que são apenas um
agrupamento de atributos, como classes normais sem métodos, ou registros de
bases de dados, etc.
As namedtuples são imutáveis assim como as tuplas.
https://docs.python.org/3/library/collections.html#collections.namedtuple
https://docs.python.org/3/library/typing.html#typing.NamedTuple
https://brasilescola.uol.com.br/curiosidades/baralho.htm
"""
from collections import namedtuple
from typing import NamedTuple

class Carta1(NamedTuple): # Herdamos a classe NamedTuple para indicar a classe que seus atributos são chaves nomeadas de uma tupla
    valor: str = 'Valor'
    naipe: str = 'Naipe'

Carta = namedtuple('Carta', ['Valor', 'Naipe'], # Usar a função namedtuple faz exatamente a mesma coisa, nesse caso passamos o primeiro parâmetro o nome da classe e a seguir as chaves
                   defaults=['', '😶']) # as chaves são colocadas dentro de uma lista, também podemos passar valores padrão usando o parâmentro defaults=[valores]
as_espada = Carta('A', '♠') # Então passamos os valores para as chaves, que obviamente sustituirão os valores padrão
print(as_espada)
print(as_espada.Naipe) # Dessa forma não precisamos passar o indíce para chamar um valor, mas sim o nome da chave como está sendo mostrado nessa linha
print(as_espada[0]) # Mas se quiser usar indíces também funciona
print(as_espada.Valor)
print(as_espada[1])
print()

for valor in as_espada:
    print(valor) # Itera sobre os valores passados
    print(as_espada._fields) # O _fields mostra todas as chaves existente
    print(as_espada._field_defaults) # E o _fields_defaults retorna as chaves e os valores padrão
print()

print(as_espada._asdict()) # _asdict converte para dicionário

