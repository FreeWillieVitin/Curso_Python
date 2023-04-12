# Empacotamento e desempacotamento de dicionarios
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Hugo',
}

dados_pessoa = {
     'idade': 25,
     'altura': 1.71
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

a, b = pessoa
print(a, b)

a, b = pessoa.values()
print(a, b)

a, b = pessoa.items()
print(a, b)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
     print(chave, valor)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# args e kwargs
# *args(argumentos não nomeados)
# **kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não Nomeados', args) 
    
    for a, b in kwargs.items():
        print(a, b)

mostro_argumentos_nomeados(1, 2, nome='Victor', segundo='Hugo', sobrenome='Jurczyszyn')
mostro_argumentos_nomeados(**pessoa_completa)