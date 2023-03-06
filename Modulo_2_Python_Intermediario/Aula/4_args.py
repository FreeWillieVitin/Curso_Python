"""
args - Argumentos não nomeados
* - *args (Empacotamento e desempacotamento)
"""
def soma(*args): # args é um nome dado por convenção á parametros com infinitos argumentos, quando o usuário quiser poderá passar quantos valores quiser
    print(args, type(args)) # Os args são do tipo tuple(tupla), abaixo um exemplo de como somar varios valores passados como argumentos
    total = 0 # Cria uma variável que armazenará os os valores para soma iniciando em 0
    for num in args: # Itera sobre a tupla gerada pelos argumentos e armazena na variável num
        print('Total', total, '+', num) # Mostra em tela qual o calculo que está sendo feito
        total += num # A variável total recebe o valor da soma entre ela e o argumento
        print('Total', total) # Mostra o resultado
    return total # Mostra o resultado final

conta = soma(1, 2, 3, 4, 5, 6, 7, 8, 9) # Execução da função com vários argumentos passados
print(conta)