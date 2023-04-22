"""
    Funções decoradoras e decoradores(DECORATOR)
    Decorar = Adicionar / Remover/ Restringir / Alterar
    Funções decoradoras são funções que decoram outras funções
    Decoradores são usados para fazer o Python
    usar as funções decoradoras em outras funções.
    Decoradores são "Syntax Sugar" (Açúcar Sintético)
"""
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print('Ok, agora voce foi decorada')
        return resultado
    return interna

@criar_funcao # Syntax Sugar
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser string')

# inverte_string_checando_parametro = criar_funcao(inverte_string)

invertida = inverte_string('Victor')
print(invertida)
print()
# ------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Decoradores com parâmetros
"""

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
# multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
# dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
# print(dez_vezes_cinco)
print()
# ------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Ordem dos decoradores
"""
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)