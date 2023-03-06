# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multi(*args):
    result = 1
    for calc in args:
        print('Total', result, '*', calc) 
        result = result * calc
        print('Total', result)
    return result

vezes = multi(2,3,4,5,6,78,9)
print(vezes)


# Crie uma função fala se um numero é par ou ímpar.
# Retorne se o número é par ou ímpar

def par_impar()