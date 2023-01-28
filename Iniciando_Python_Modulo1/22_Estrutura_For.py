"""
For in em python
Iterando strings com o for
Função range(start=0, stop, step=1)
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
metodo -> Uma ação chamada dentro do objeto
"""
# ------------------------------------------------------------------------------------------------------------------------- 
palavra = iter('Victor') # Aqui conhecemos a função iter, ela é a responsavel por identificar a posição de um objeto iteravel na memoria
print(palavra) # Executado apenas dessa forma o print retornará apenas a descrição da posição onde essa string está alocada na memoria

print(palavra.__next__()) # Aqui conheçemos o metodo next, ele é a demonstração de como o laço for funciona por de tras
print(palavra.__next__()) # dos panos, pois ele indica ao iterador do python cada indice do objeto iteravel, então no caso
print(palavra.__next__()) # cada vez que é executado, uma letra da string será printada, e é assim com qualquer objeto iteravel
print(palavra.__next__()) 
print(palavra.__next__())
print(palavra.__next__())

while True: # Enquanto o laço for verdadeiro
    try: # Tente
        print(next(palavra)) # Mostrar em tela cada indice do objeto iteravel
    except StopIteration: # É tratado o erro StopIteration, que é o erro mostrado quando os iteração chegou ao fim
        break # O erro é tratado com um break no laço

# -------------------------------------------------------------------------------------------------------------------------
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

# -------------------------------------------------------------------------------------------------------------------------
# Aqui é definido duas variaveis, uma para que ira receber o texto e a outra numeros ordenadores atraves do enumerate
for n, letra in enumerate(texto):
    print(n, letra)

# No laço a seguir conhecemos o range que basicamente define um alcance, para o funcionamento deve ser definido
# parametros que seguem a seguinte ordem: Função range(start=0, stop, step=1), no caso o compilador vai realizar uma
# contagem dos numeros do 5 até o 10 pulando de 1 em 1, valores esses que podem ser alterados como desejar
for n in range(5, 10, 1):
    print(n)

numeros = range(0, 100, 8)

for num in numeros:
    print(numeros)

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