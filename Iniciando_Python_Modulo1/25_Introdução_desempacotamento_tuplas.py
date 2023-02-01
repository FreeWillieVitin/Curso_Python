"""
Introdução ao desempacotamento + tuples (tuplas)
*(variavel) -> Ao realizar o desempacotamento devemos ter a mesma quantidade de variáveis e valores na lista, criar uma variável com * na frente
significa q ela criará uma variável com o resto dos valores, como no exemplo abaixo que iréi comentar

_ -> Usar o Underline como variável é uma boa prática dos programadores para indicar uma variável que funciona porém não é usada

Tipo tupla -> Uma lista imutável, não sendo possivel adicionar, remover ou alterar qualquer valor da lista
"""
# Desempacotamento ----------------------------------------------------------------------------------------------------------------------------------------
l = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Temos uma variável com uma lista
l1, l2, l3, *_ = l # Foi desempacotado 3 valores da lista em 3 variáveis diferentes e a quarta variável foi acrescentado um *, guardará o resto dos valores
print(l2, _) # Exibe a variável com o segundo valor da lista, e a variável com o resto dos valores em tipo lista

# Tupla ---------------------------------------------------------------------------------------------------------------------------------------------------
nome = 'Victor', 'Marieli', 'Judite', 'Luiz' # A criação de uma tupla é basicamente como a de uma lista, porém sem os colchetes tornando ela assim imutável
nome = list(nome) # Converte a tupla em lista, tornando ela mutável
print(nome)
nome = tuple(nome) # Converte a lista para tupla, tornando imutável
print(nome)