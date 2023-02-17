"""
Operador or em Python
and, or, not, in, not in

or:  Qualquer condição verdadeira avalia toda a expressão como verdadeira.
Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: # Nesta linha é dada duas condições para o interpretador então ambas as letras e serão aceitas, pois uma delas será verdadeira
    print('Entrar')
else:
    print('Sair')


nome = input('Qual o seu nome? ') # Esta parte do código demonstra bem como funciona o operador or

print(nome or 'Você não digitou nada') # Já temos um valor que será verdadeiro que é o texto de não digitou nada, então nesse caso o interpretador sempre retornará algo

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Victor'

var = a or b or c or d or e or f or g
print(var) # O interpretador vai para no primeiro valor verdadeiro que encontrar, no caso a variavel f de valor 22