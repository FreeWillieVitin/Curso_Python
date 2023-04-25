# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# def multi(*args):
#     result = 1
#     for calc in args:
#         print('Total', result, '*', calc) 
#         result = result * calc
#         print('Total', result)
#     return result

# vezes = multi(2,3,4,5)
# print(vezes)


# Crie uma função fala se um numero é par ou ímpar.
# Retorne se o número é par ou ímpar

# def par_impar(x):
#     if x % 2 == 0:
#         return (f"{x} é um número par")
#     else:
#         return (f"{x} é um número ímpar")
    
# ret = par_impar(int(input('Digite um numero: ')))
# print(ret)

"""
Faça uma função	que calcule a média	de um aluno	de acordo com o critério definido	
neste curso. Além disso, faça uma segunda função que informe o status do aluno de	
acordo com a tabela	a seguir:
Nota acima de 6	à “Aprovado”
Nota entre 4 e 6 à Conceito	“Verificação Suplementar”
Nota abaixo	de 4 à Conceito	“Reprovado”
"""

# def calc_media(a,b,c,d):
#     soma = (a + b + c + d)
#     media = (soma/4)
#     def aprovado():
#         if media > 6:
#             status = 'Aprovado'
#         elif media >= 4 or media <= 6:
#             status = 'Verificação Suplementar'
#         else:
#             status = 'Reprovado'
#         return status
#     print(aprovado())
#     return media
# calcula_media = calc_media(5,3,4,8)
# print(calcula_media)

"""
    Considerando duas listas de inteiros ou floats (lista A e lista B)
    Some os valores nas listas retornando uma nova lista com os valores somados:
    Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
    menor.

    Exemplo:
    lista_a     = [1, 2, 3, 4, 5, 6, 7]
    lista_b     = [1, 2, 3, 4]
    =================== resultado
    lista_soma  = [2, 4, 6, 8]
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4, 9]

lista_resultado = []

lista1 = lista_a
lista2 = lista_b

for i, valor in enumerate(lista_b):
    result = valor + lista2[i]
    lista_resultado.append(result)
print(lista_resultado)

# Solução do professor usando list comprehension e zip ou zip_longest
# lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
# print(lista_soma)

# from itertools import zip_longest
 
# lista_a = [10, 2, 3, 4, 5]
# lista_b = [12, 2, 3, 6, 50, 60, 70]
# lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
# print(lista_soma)
