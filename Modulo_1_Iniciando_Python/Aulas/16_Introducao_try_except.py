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

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Try, except, else e finally
"""
# a = 'a'
# b = 10

# c = a / b

try:
    a = int(input("Digite um número: "))
    b = int(input("Digite um número: "))

    c = a / b
    print(c)

except ZeroDivisionError as error:
    print('Impossivel dividir')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)

except NameError:
    print('Sem valor definido')

except ValueError:
    print('Sem valor definido')

except (TypeError, IndexError):
    print('TyperError + IndexError')

except Exception:
    print('Erro Desconhecido')

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    print('ABRIR O ARQUIVO')
    8/0

except ZeroDivisionError:
    print('ERRO')

else:
    print('Não deu erro')

finally:
    print('FECHAR ARQUIVO')