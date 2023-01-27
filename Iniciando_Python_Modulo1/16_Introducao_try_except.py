"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o número que vc digitar: ') # Recebe uma string

try: # tenta executar
    numero_float = float(numero_str) # COnverte a string em valor float
    print('FLOAT:', numero_float) # Retorna o valor convertido
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') # Dobra o valor convertido
except: # Se houver um erro
    print('Isso não é um número') # Se o valor que esta tentado ser convertido não for um tipo permitido,
    #  então como excessão, o interpretador retornará essa mensagem
