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
import sys

# Aqui conhecemos a função iter, ela é a responsavel por identificar a posição de um objeto iteravel na memoria
palavra = iter('Victor')
# Executado apenas dessa forma o print retornará apenas a descrição da posição onde essa string está alocada na memoria
print(palavra)

print()

print(palavra.__next__())  # Aqui conheçemos o metodo next, ele é a demonstração de como o laço for funciona por de tras
print(palavra.__next__())  # dos panos, pois ele indica ao iterador do python cada indice do objeto iteravel, então no caso
print(palavra.__next__())  # cada vez que é executado, uma letra da string será printada, e é assim com qualquer objeto iteravel
print(palavra.__next__())
print(palavra.__next__())
print(palavra.__next__())

print()

while True:  # Enquanto o laço for verdadeiro
    try:  # Tente
        print(next(palavra))  # Mostrar em tela cada indice do objeto iteravel
    except StopIteration:  # É tratado o erro StopIteration, que é o erro mostrado quando os iteração chegou ao fim
        break  # O erro é tratado com um break no laço

# Generator expression - É uma forma de iterar sobre algo mas sem executar toda a iteração de uma vez, mas sim de forma
# pausadamente poupando uso de memória

# Aqui temos uma lista composta por um list comprehension, uma lista quando criada automaticamente passa a ocupar o seu valor
# inteiro na memória, pois armazena tudo de uma vez
lista = [n for n in range(1000)]
# O contrário acontece com um generator, pois ele itera apenas o primeiro valor e espera a sua proxima chamada(next()) para
# continuar sua iteração
Generator = (n for n in range(1000))

# Função getsizeof mostra quanto ocupa determinada coisa na memória, no caso está apontando para a lista,
# assim podemos observar que uma lista ocupa o seu espaço total na memória
print(sys.getsizeof(lista))
print()  # Pois ela é ja está com todos os seus valores á preenchendo
print(lista)
print()
# Já um generator ocupa um valor fixo na memória, pois ele itera sobre um valor apenas e mesmo que ele tenha outros para iterar,
# pois aguarda a sua ação next ser chamada
print(sys.getsizeof(Generator))
print()  # Desta forma sempre terá o mesmo valor, porém não temos indices em um generator sendo assim seus valores são imutáveis
print(Generator)  # Executa o generator e exibe apenas o valor 0 esperando a sua proxima chamada
print()
# Generator sendo chamado novamente, agora sim exibira o valor 1, mas continuará tendo o mesmo valor em memoria
print(next(Generator))
print()
# for n in Generator:
# Aqui iteramos o generator, fazendo assim com que ele execute todos os valores de uma vez, mas é retornado de forma diferente da
# lista que mostra toda ela de uma vez só
#     print(n)
# print() # Aqui cada valor é exibido por vez pulando-se uma linha como se fosse algum algoritmo em looping
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

# -------------------------------------------------------------------------------------------------------------------------
# No laço a seguir conhecemos o range que basicamente define um alcance, para o funcionamento deve ser definido
# parametros que seguem a seguinte ordem: Função range(start=0, stop, step=1), no caso o compilador vai realizar uma
# contagem dos numeros do 5 até o 10 pulando de 1 em 1, valores esses que podem ser alterados como desejar
for n in range(5, 10, 1):
    print(n)

numeros = range(0, 100, 8)

for num in numeros:
    print(numeros)

# -------------------------------------------------------------------------------------------------------------------------
# Mesmo caso de uso de uma função range, mas dessa vez foi passado apenas um parametro, que indica que a operação a ser
# realizada é de mostrar apenas multiplicados por 8 até o numero limite 100
for n in range(100):
    if n % 8 == 0:
        print(n)

# -------------------------------------------------------------------------------------------------------------------------
# aqui é mais um exemplo de uso de for, mas agora com o uso de condicionais dentro do laço
for letra in texto:
    if letra == 't':
        nova += letra.upper()
    elif letra == 'h':
        nova += letra.upper()
    else:
        nova += letra

# -------------------------------------------------------------------------------------------------------------------------
# Da mesma forma que no while, no laço for tambem podemos usar continuem break e else, realizando as mesmas funçoes
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
