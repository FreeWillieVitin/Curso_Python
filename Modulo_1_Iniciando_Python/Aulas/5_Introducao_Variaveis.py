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
#  Exercício de variáveis
#  Calculo de IMC
print(nome, 'você tem', idade, 'e seu imc é', imc)

# Treinando variável
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', e_maior)
print('Altura em metros:', altura)

"""
CONSTANTE = "Variaveis" que não vai mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

Abaixo temos uma demonstração de codigo mais limpo, ele ocupa algumas linhas a mais devido a criação
das variáveis, porém para quem está lendo e tem um pouco de conhecimento fica muito melhor de ler e
interpretar
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_passa_radar = velocidade > RADAR_1
passou_entre1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
passou_entre2 = local_carro <= (LOCAL_1 + RADAR_RANGE)
passou_radar = passou_entre1 and passou_entre2
multado_radar = passou_radar and vel_passa_radar

if vel_passa_radar:
    print('Velocidade carro passou do radar 1')

if passou_radar:
    print('Carro passou radar 1')

if multado_radar:
    print('carro multado em radar 1')
