"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
def Print(): # Temos a criação da primeira função e abaixo todos os comandos q ela irá executar, funções são criadas com letra minuscula
    print('Teste1')
    print('Teste2')
    print('Teste3')
    print('Teste4')

def imprimir(a, b, c): # Funções com parametros, são como as variaveis da função, necessarias para a função ser executada
    print(a, b, c) # Essa função mostrará em tela os valores passados como argumentos durante a execução da função

def saudacao(nome='Sem Nome'): # Função com paramentro padrão, caso nao seja passado nenhum argumento durante a execução
    print(f'Olá, {nome}!') # Quando for executada a função e nenhum argumento for passado o padrão será um 'Olá sem nome!'


Print() # Apenas executa a função
imprimir(1, 2, 3) # Executa a função com argumentos as variaveis definidas como parametro
saudacao('Marieli') # Executa a função com o nome passado como argumento obrigatorio
saudacao() # Nesse caso como ofi dado um valor padrão, se nenhum argumento for passado, o que será retornado será o valor padrão
# Definido durante a criação da função

"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y):
    print(f'{x=} {y=}', '|', 'x + y = ', x + y)

soma(1, 2) # Argumento não nomeado
soma(y=2, x=3) # Argumento nomeado

"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""
def somar(x, y, z=None): # Definindo um variável com 3 parametros sendo um com valor padrão none, importante usar valor padrão none para realizar checagens como abaixo
    if z is not None: # No caso se for passado um valor de parametro para z, então será realizado o calculo com os 3 valores
        print(f'{x=} {y=} {z=}', x + y + z)
    else: # Caso nao seja passado nenhum valor, então z continuará sob o tipo none e e nao será incluido no calculo
        print(f'{x=} {y=}', x + y)

somar(1, 2)
somar(3, 5)
somar(100, 200)
somar(z=0, x=8, y=3)

"""
Higher Order Functions
Funções de primeira classe
Podemos Atribuir uma função como argumento para execução de outra função
"""
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'Bom dia', 'jorge')
print(v)