"""
    Sets - Conjuntos em Python (tipo set)
    Conjuntos são ensinados na matemática
    https://brasilescola.uol.com.br/matematica/conjunto.htm
    Representados graficamente pelo diagrama de Venn
    Sets em Python são mutáveis, porém aceitam apenas
    tipos imutáveis como valor interno.
    Criando um set
    set(iterável) ou {1, 2, 3}
"""
s1 = set() # Estrutura de um set vazio
s1 = {'Victor', 1, 2, 3} # Outra forma de estrutura de um set, dessa vez com valores
print(s1, type(s1))

"""
 Sets são eficientes para remover valores duplicados
 de iteráveis.
 - Seus valores serão sempre únicos;
 - Não aceitam valores mutáveis;
 - não tem índexes;
 - não garantem ordem;
 - são iteráveis (for, in, not in)
"""
l1 = (1,1,1,2,3,3,4,5,3,1) # Uma tupla com diversos valores, tendo alguns repetidos
s1 = set(l1) # Converte a tupla em um set, e seguindo a regra o set unifica todos os valores repetidos
l2 = tuple(s1) # Converte novamente em uma tupla, dessa vez sem os valores repetidos, retornando todos eles unificados
print(l2)

"""
 Métodos úteis:
 add, update, clear, discard
"""
