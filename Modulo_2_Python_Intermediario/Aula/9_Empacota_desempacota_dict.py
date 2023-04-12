# Empacotamento e desempacotamento de dicionarios
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Hugo', # Dicionario de nomes
}

dados_pessoa = {
     'idade': 25,
     'altura': 1.71 # Dicionario de dados
}

pessoa_completa = {**pessoa, **dados_pessoa}  # Aqui acontece o desempacotamento do dicionario, com o uso de kwargs(**) desempacota os dicionarios e os une em um novo dicionario
print(pessoa_completa) # Exibe todos as chaves e valores de ambos os dicionarios que foram unidos, como é um dicionario onde cada item é nomeado, usamos kwargs(**)

a, b = pessoa # Armazena como padrão apenas as chaves do dicinario
print(a, b) # Exibe apenas as chaves. EX: nome sobrenome

a, b = pessoa.values() # Usando o .values() podemos assim definir a variavel como sendo os valores de cada chave
print(a, b) # Como descrito no dicionario pessoa os valores de cada chave é Victor Hugo

a, b = pessoa.items() # Da mesma forma temos a função .items() que define os itens, ou seja cada conjunto de informações
print(a, b) # Ao definir a variável para retornar os itens, são demonstradas em forma de tuplas cada conjunto. EX: ('nome','Victor')('sobrenome','Hugo')

(a1, a2), (b1, b2) = pessoa.items() # Aqui temos uma forma de conversão desses itens, pois as variaveis ja estão sendo encapsuladas com tuplas
print(a1, a2) # Então ao executar, vai ser retornada os items em forma de string
print(b1, b2)

for chave, valor in pessoa.items(): # Obviamente que a situação acima é bem melhor contornada se for iterado no items dos dicionarios
     print(chave, valor) # Mas é bom entender que existe formas de separar e receber valores unicos se necessario

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# args e kwargs
# *args(argumentos não nomeados)
# **kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs): # Função que recebe como parametro args e kwargs descrito acima
    print('Não Nomeados', args) # O args entra como padrão para casos em que haja argumentos não nomeados, que serão demonstrados como tuplas
    
    for a, b in kwargs.items(): # Então é iterado sobre os items e mostrado em tela todos os items passados que sejam nomeados
        print(a, b)

mostro_argumentos_nomeados(1, 2, nome='Victor', segundo='Hugo', sobrenome='Jurczyszyn') # Execução da função que temos 5 valores, 2 deles entram como args pois não tem nomeção que são o (1,2), o rewssto é nomeado
mostro_argumentos_nomeados(**pessoa_completa) # Também podemos executar a função dando como parametro uma variável, que no caso é a variável que recebe a união dos dois dicionarios