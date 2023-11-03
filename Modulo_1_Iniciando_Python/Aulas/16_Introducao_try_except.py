"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
# numero_str = input('Vou dobrar o número que vc digitar: ') # Recebe uma string

# try: # tenta executar
#     numero_float = float(numero_str) # COnverte a string em valor float
#     print('FLOAT:', numero_float) # Retorna o valor convertido
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') # Dobra o valor convertido
# except: # Se houver um erro
#     print('Isso não é um número') # Se o valor que esta tentado ser convertido não for um tipo permitido,
#     #  então como excessão, o interpretador retornará essa mensagem

# # ------------------------------------------------------------------------------------------------------------------------------
# """
# Try, except, else e finally
# """
# # a = 'a'
# # b = 10

# # c = a / b

# """
# Continuando com a tratação de erros, podemos especificar diferentes erros para cada ação incorreta do usuário
# """

# try:
#     a = int(input("Digite um número: "))
#     Aqui temos um sistema de divisão, onde obviamente vai dividir o valor de a com o valor de b
#     b = int(input("Digite um número: "))

#     c = a / b
#     print(c)

# Caso o usuário tente erroneamente realizar uma divisão por 0, o sistema automáticamente mostrará uma mensagem
# com o erro ZeroDivisionError
# except ZeroDivisionError as error:

#     Para o usuário é difícil a compreensão do erro se form mostrado isso a ele, dessa maneira se especificarmos
#     após o except qual o erro a ser tratado
#     print('Impossivel dividir')

#     Podemos personalizar a mensagem retornada ao usuário, facilitando a compreensão, isso pode ser feito quantas vezes for
#     necessário, para os diversos tipos de erro
#     print('MSG:', error)
#     print('Nome:', error.__class__.__name__)

# except NameError:
#     print('Sem valor definido')

# except ValueError:
#     print('Sem valor definido')

# Podemos também mesmo que não sendo correto, tratar mais de um erro no mesmo except, inserindo eles em uma tupla
# except (TypeError, IndexError):
#     print('TyperError + IndexError')

# O tipo de erro exception é como se fosse o primeiro da hierarquia dos erros, valendo para todos os outros,
# caso já tenho sido especificado todos os erros conhecidos
# except Exception:
#     Mas mesmo assim queira deixar uma tratativa de segurança para algum erro não encontrado, usamos a classe de erro exception
#     print('Erro Desconhecido')

# # ------------------------------------------------------------------------------------------------------------------------------
# try:
#     print('ABRIR O ARQUIVO')
#     8/0

# except ZeroDivisionError:
#     print('ERRO')

# O else em uma tratação de erro é uma mensagem se caso não aconteça o erro, pouquissimo usado pois temos a palavra chave finally
# que faz algo semelhante
# else:
#     print('Não deu erro')

# O finally ele é uma palavra chave que executará de qualquer forma, tanto se o erro ocorrer, quanto se não ocorrer, imaginamos
# que nesse exemplo estamos tentando abrir o arquivo
# finally:
# Para executar alguma coisa, o arquivo abrirá fará o que tem que ser feito e será fechado, se caso aconteça um erro, o arquivo
# será fechado da mesma forma
# print('FECHAR ARQUIVO')

# # ------------------------------------------------------------------------------------------------------------------------------
"""
Criando Exceptions em Python Orientado a Objetos
Para criar uma Exception em Python, você só
precisa herdar de alguma exceção da linguagem.
A recomendação da doc é herdar de Exception.
https://docs.python.org/3/library/exceptions.html
Criando exceções (comum colocar Error ao final)
Levantando (raise) / Lançando (throw) exceções
Relançando exceções
Adicionando notas em exceções (3.11.0)
"""


# Classe com excessão, por convenção sempre deve terminar o nome com error e herdar da classe exception
class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Nota 1')
    exception_.add_note('Errou isso')
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar denovo')
    exception_.add_note('Mais uma nota')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error
