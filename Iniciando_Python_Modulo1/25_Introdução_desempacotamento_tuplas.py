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

"""
Desempacotamento em chamadas de métodos e funções
"""
string = 'ABCDE'
lista = ['Victor', 'Marieli', 1, 2, 3, 'Luiz']
lista2 = ['Victor', 'Marieli', 1, 2, 3, 'Luiz']
tupla = 'Python', 'é', 'legal'

p, b, *_, ap, u = lista # Criamos uma ordem para os valores, seguindo a ideia q o * retorna o resto, tudo o que vem antes e depois
# é organizado para não ser englobado no resto, no exemplo a cima, está ordenado para estar fora do resto e receber a o valor
# conforme o posicionamento do seu indice
print(p, u, ap, _) # p = Victor, u = Luiz, ap = 3 e por ultimo a variavel _ que receberá todas os outros valores

for i in lista2:
    print(i, end=' ')
# Ao exibir qualquer iteravel com print, se usarmos o *, todos os valores serão exibidos em linha, sem quebra por valor
print('Victor', 'Marieli', 1, 2, 3, 'Luiz')
print(*lista2)
print(*lista2, sep='-')
print(*string)
print(*string, sep='*')
print(*tupla)
print(*tupla, sep='+')

# Tupla ---------------------------------------------------------------------------------------------------------------------------------------------------
nome = 'Victor', 'Marieli', 'Judite', 'Luiz' # A criação de uma tupla é basicamente como a de uma lista, porém sem os colchetes tornando ela assim imutável
nome = list(nome) # Converte a tupla em lista, tornando ela mutável
print(nome)
nome = tuple(nome) # Converte a lista para tupla, tornando imutável
print(nome)

