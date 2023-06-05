"""
Enum -> Enumerações
Enumerações na programação, são usadas em ocasiões onde temos
um determinado número de coisas para escolher.
Enums têm membros e seus valores são constantes.
Enums em python:
  - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
  - podem ser iterados para retornar seus membros canônicos na ordem de
      definição
enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
  diretamente (mesmo assim, Enums não são classes normais em Python).
Você poderá usar seu Enum com type annotations, com isinstance e
outras coisas relacionadas com tipo.
Para obter os dados:
membro = Classe(valor), Classe['chave']
chave = Classe.chave.name
valor = Classe.chave.value
"""
import enum
# Abaixo temos duas formas de usar a classe enum
Direcoes = enum.Enum('Direcoes', ['Esquerda', 'Direita', 'Acima', 'Abaixo']) # Variável que recebe a classe Enum do módulo enum, onde nela é passado os argumentos de nome da classe enumerada e uma lista de coisas que normalmente são da mesma categoria

class Direcao(enum.Enum): # Também podemos cirar uma classe e herdar a classe Enum para ela, dessa forma trabalhamos com enum dentro da classe, de forma mais organizada
    ESQUERDA = enum.auto() # Temos os atributos todos enumerados podendo ser manualmente ou usando a classe auto() do módulo enum
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()
    

print(Direcoes(1), Direcoes['Esquerda'], Direcoes.Esquerda) # Aqui temos algumas formas de mostrar atributos enumerados da classe, exibindo o seu nome e qual a sua posição
print(Direcoes(1).name, Direcoes.Esquerda.value)

def mover(direcao: Direcao): # Função para exibir as direções presentes na classe como atributo, se caso alguma das direções não estiver presente, temos a excessão retornando uma mensagem de erro
    if not isinstance(direcao, Direcao):
        raise ValueError('Direção não encontrada')
    
    
    print(f'Movendo para {direcao.name} ({direcao.value})')

# mover('Esquerda')
# mover('Direita')
# mover('Acima')
# mover('Abaixo')
# mover('lado')
print()
# mover(Direcoes.Esquerda)
# mover(Direcoes.Direita)
# mover(Direcoes.Acima)
# mover(Direcoes.Abaixo)
print()
mover(Direcao.ESQUERDA)
mover(Direcao.DIREITA)
mover(Direcao.ACIMA)
mover(Direcao.ABAIXO)


