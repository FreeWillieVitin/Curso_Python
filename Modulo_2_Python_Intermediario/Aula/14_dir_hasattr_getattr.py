# dir, hasattr e getattr em python
string = 'Luiz'
metodo = 'upper'

teste = dir(string) 
print(teste)
print()

if hasattr(string, 'upper'):
    print('Existe')
    print(string.upper())

if hasattr(string, metodo):
    print('Existe')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)