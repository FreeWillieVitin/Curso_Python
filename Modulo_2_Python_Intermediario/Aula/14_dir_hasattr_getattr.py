# dir, hasattr e getattr em python
string = 'Luiz'
metodo = 'upper'

teste = dir(string) # Função dir mostr atodos os métodos que podem ser usados para um determinado tipo de dado
print(teste)
print()

if hasattr(string, 'upper'): # A Função hasattr serve para checar se o objeto especificado tem o atributo desejado
    print('Existe')
    print(string.upper())

if hasattr(string, metodo): # A função getattr acessa e define um atributo para um objeto e caso não seja encontrado esse atributo no objeto desejado, podemos definir um atributo padrão no paramêntro da função
    print('Existe')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)