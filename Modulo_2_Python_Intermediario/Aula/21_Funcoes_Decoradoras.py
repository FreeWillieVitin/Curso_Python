"""
    Funções decoradoras e decoradores(DECORATOR)
    Decorar = Adicionar / Remover/ Restringir / Alterar
    Funções decoradoras são funções que decoram outras funções
    Decoradores são usados para fazer o Python
    usar as funções decoradoras em outras funções.
"""
def inverte_string(string):
    return string[::-1]

invertida = inverte_string('Victor')
print(invertida)