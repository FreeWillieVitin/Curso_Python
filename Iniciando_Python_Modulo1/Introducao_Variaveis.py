"""
Variáveis: è basicamente algo salvo na memória do computador
As variáveis sempre começam com letra minúscula
PEP8: Inicia variaveis com letras minúsculas, pode usar
números e underline _.
O sinal de = é o operador de atribuição. Ele é usado para
atribuir um valor a um nome (variável).
Uso: nome_variavel = expressão
"""

nome = 'Victor'
sobrenome = 'Hugo'
idade = 24
ano_nascimento = 1998
altura = 1.74
e_maior = idade > 18
peso = 82
imc = (peso / (altura ** 2))
print(nome, type(nome))
print('Nome:', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior:', e_maior)
print(idade * altura)
#Exercício de variáveis
#Calculo de IMC
print(nome, 'você tem', idade, 'e seu imc é', imc)

# Treinando variável
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade),
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', e_maior)
print('Altura em metros:', altura)

"""
CONSTANTE = "Variaveis" que não vai mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61 # Velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # Velocidade maxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distancia onde o radar pega