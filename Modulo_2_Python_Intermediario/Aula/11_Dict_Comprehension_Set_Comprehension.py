# Dictionary COmprehension e Set Comprehension
produto = {
    'nome': 'caneta Azul',
    'preco': 2.5,  # Da mesma forma que temos os list comprehension, temos os dict comprehension e os set comprehension, eles tem a estrutura basicamente igual aos list
    'categoria': 'Escritório', # Precisamos de um dict com items, e para realizar ações com ele como iterações, filtragens e tudo mais criamos uma nova variavel com um novo dict da mesma forma que as list comprehension
}

for chave , valor in produto.items(): # Aqui temos a iteração convencional como já foi feita anteriormente
    print(chave, valor)

print()

dc = { # E Aqui um um dict comprehension, nesse exemplo queremos seja retornado apenas valores que são string e que sua categoria seja diferente de escritorio
    chave: valor.upper() # Também queremos que o valor da chave seja mostrado em letra maiúscula
    if isinstance(valor, str) else valor # Como podemos ver temos um valor inteiro no dict e valores numéricos não tem método upper() então é retornado um erro, para isso usamos o isinstance() 
    for chave, valor # Essa função recebe como paramêtro qual variável queremos e qual o tipo de dado que no caso são os tipos str, então todos os str que são reprensentados pela variável valor ficará maiúsculo
    in produto.items() # Então iteramos sobre o dict e definimos as variáveis que representarão as chaves e os valores do dict
    if chave != 'categoria' # E aqui filtramos apenas por chaves que não são escritório
}

print(dc)
print()

s1 = {2 ** i for i in range(10)} # Dá mesma forma que os anteriores iteramos dentro do set, tendo assim um set comprehension
print(s1)