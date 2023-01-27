"""
For in em python
Iterando strings com o for
Função range(start=0, stop, step=1)


"""
texto = 'Python'
nova = ''
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# O laço for percorre os itens de uma lista, e assim, executa o código declarado no loop.
for letra in texto:
    nova += f'*{letra}'
    print(letra)
print(nova)

# Aqui é definido duas variaveis, uma para que ira receber o texto e a outra numeros ordenadores atraves do enumerate
for n, letra in enumerate(texto):
    print(n, letra)

# No laço a seguir conhecemos o range que basicamente define um alcance, para o funcionamento deve ser definido
# parametros que seguem a seguinte ordem: Função range(start=0, stop, step=1), no caso o compilador vai realizar uma
# contagem dos numeros do 5 até o 10 pulando de 1 em 1, valores esses que podem ser alterados como desejar
for n in range(5, 10, 1):
    print(n)

# Mesmo caso de uso de uma função range, mas dessa vez foi passado apenas um parametro, que indica que a operação a ser
# realizada é de mostrar apenas multiplicados por 8 até o numero limite 100
for n in range(100):
    if n % 8 == 0:
        print(n)

# aqui é mais um exemplo de uso de for, mas agora com o uso de condicionais dentro do laço
for letra in texto:
    if letra == 't':
        nova += letra.upper()
    elif letra == 'h':
        nova += letra.upper()
    else:
        nova += letra