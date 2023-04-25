# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
import itertools
cidades = [
    'Salvador',
    'Ubatuba', # Lista cidades
    'Belo Horizonte',
]

estados = [
    'BA',
    'SP', # Lista estados
    'MG',
    'RJ',
]
def unir1(cidade, estado): # Cria função para receber as duas listas como argumento
    if len(cidade) < len(estado): # Checa se a lista cidade é menor que a lista estado, se sim armazena a lista na variável lista_menor
        lista_menor = cidade
    else:
        lista_menor = estado

    resultado = [] # Cria uma lista em branco onde será inserido os valores gerados

    for i, valor in enumerate(lista_menor): # Itera sobre a variável que recebeu a lista cidade
        if len(cidade) < len(estado): # Checagem novamente se a lista passada no argumento cidade for menor que estado
            resultado.append((valor, estado[i])) # Então inserir a lista em branco o valor da lista cidade e o index referente ao valor do estado
        else:
            resultado.append((valor, cidade[i])) # Se não faça o inverso

    return resultado # Retorna a lista que antes estava vazia, e agora está preenchida com os valores checados

print(unir1(cidades, estados)) # Executa a função, passando as duas listas como argumento
print()

def unir(): # Existe um método em python que ja realiza a junção de duas listas e também existe uma classe que faz isso, no exemplo abaixo
    z = list(itertools.zip_longest(cidades,estados)) # Importamos o método itertools e usamos a função zip_longest, essa função recebe as listas
    print(z) # E pega a lista maior e une com as outras
unir()

print()
print(list(zip(cidades, estados))) # Já a classe zip faz a mesma coisa, porém nao precisa ser importado nada e pega a lista menor e une com as outras


# Solução do exercicio do professor
# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]


