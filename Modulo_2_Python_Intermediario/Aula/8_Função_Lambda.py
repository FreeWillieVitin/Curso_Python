# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
lista1 = [4, 32, 1, 34, 5, 6, 6, 21, ] # uma lista com numero fora de ordem
lista1.sort(reverse=True) # A função sort ordem os valores de uma lista, podendo ser de trás para frente de definir o parametro reverse como true
print(lista1) # Exibe a lista ordenada de forma inversa
lista1.sort() # Sem o paramentro reverse definido a lista é ordenada de forma normal
print(lista1) # Exibe a lista em ordem normal
sorted(lista1) # A função de ordenação pode ser escrita dessa forma também, fazendo exatamente a mesma coisa
print(lista1) # Exibe a função ordenadamente
a = sorted(lista1, reverse=True) # Para inverter a ordem usando o sorted eu precisei definir uma variavel a ele
print(a) # Exibindo o sorted inverso

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},               # Lista com Dicionarios dentro
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
def ordena(item): # Função para ordenar a lista conforme o cada valor dos itens do dicionario
    """
    Essa função nao exatamente ordena a lista, ela funciona como chave para a função key mostrada a baixo
    """
    return item['nome']

lista.sort(key=ordena) # Aqui sim que define a ordenação, a função key recebe a chave do dicionario que é definido na função. 
                       # EX: Na função ordena foi definido o return item como nome, então a key vai receber esse valor vai verificar a existencia dele no dicionario e order por este valor

for item in lista: # Então iteramos sobre essa lista de forma que os nomes estão ordenados
    print(item)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def exibir(lista): # Função para iterar sobre uma variavel
    for item in lista:
        print(item)
    print()

"""
Podemos usar a função lambda para servir de parametro para outra função o mesmo que fazia a função ordena no exemplo acima
porém a função ordena estava definida e voce precisava passar valor a ela, o lambda é uma função anonima que não é necessario definir
"""
l1 = sorted(lista, key=lambda item: item['nome']) # Então usando o lambda como chave, precisamos apenas passar qual o item que vai ser usado para realizar a ordenação e pronto
print() 
l2 = sorted(lista, key=lambda item: item['sobrenome'])


exibir(l1) # Executa apenas a função de iteração na variavel e ordena da mesma forma que no exemplo anterior
exibir(l2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Outros exemplos de funções tranformadas em lambda
"""
def executa(funcao, *args): # Função para facilitar a execução das funções abaixo
    return funcao(*args)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def soma(x, y): # Função de soma
    return x + y


"""
Aqui executamos a função executa e em vez de passar a função soma como paramentro e seu valores, passamos o lambda
a estrutura da função lambda fica a seguinte:
passamos o lambda inicialmente e seus argumentos usamos o : e então é descrito o que será feito com esses argumentos, no caso a soma deles, isto seria o primeiro argumento da função executa
o segundo argumento que é um *args é onde será passado os valores que vão ser somados, basicamente a criação e a execução de uma função tudo em uma linha apenas
"""
print(executa(lambda x, y: x + y,2, 3))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cria_multiplicador(multiplicador): # Função que multiplica 1 valor por ele mesmo
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = executa(lambda m: lambda n: m * n, 2)
print(duplica(2))

duplica2 = lambda m : m * m
print(duplica2(5))
