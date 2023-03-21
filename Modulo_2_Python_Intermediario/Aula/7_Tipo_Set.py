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
met = set() # Cria um método vazio
met.add('Victor') # Adiciona valores ao set
met.add(1) # Adicionou o valor inteiro 1 ao set
met.update(('Olá mundo', 1,2,3,4),'teste') # Funciona da mesma forma que o add, esse método atualiza o set, podendo inserir valores
# met.clear() # Limpa o Set
met.discard('t') # Elimina valores do set
print(met)

"""
 Operadores úteis:
 | união (union) = Une
 & (intersection) = Itens presentes em ambos
 - Diferença = Itens presentes apenas no set da esquerda
 ^  diferença simétrica = Itens que não estão em ambos
"""
op1 = {1, 2, 3} # Criação de 2 sets com valores distintos
op2 = {2, 3, 4}
op3 = op1 | op2 # Uma variável que recebe a união dos 2 sets, lembrando que um set nao armazena valores repetidos
op4 = op1 & op2 # Recebe apenas os valores que estão em ambos os sets, eliminando os valores diferentes
op5 = op1 ^ op2 # Contrário do anterior, recebe apenas os valores diferentes e elimina os iguais
op6 = op1 - op2 # Recebe apenas os valores que contém apenas no conjunto da esquerda, varia conforme é contruído

"""
Exemplo de uso dos sets
"""
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)
