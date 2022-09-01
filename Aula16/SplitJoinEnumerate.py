"""
Funções Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
* Strip - Retira da strings os caracteres desejados, como espaços, pontos, virgulas e etc
* Capitalize - Deixa a primeira letra da string maiúscula
"""
string = 'O Brasil é o país do futebol, o Brasil é penta e é tbm muito lindo.'  # Variável
lista = string.split(' ')  # Variável com split indica que a ‘string’ inserida será fatiada com espaços
lista2 = string.split(',')  # Mesma coisa da anterior, porém fatia com vírgulas
string2 = '+'.join(lista)  # Variável utilizando join, quer dizer que vai unir todos os itens da lista referenciada com
# o character desejado

palavra = ''  # Variável de String vazia que vai receber o valor in run
contagem = 0  # Variável que indica o início da contagem em 0

for i in lista:  # Iteração com a lista, printando quantas vezes uma palavra aparece na frase através da função count
    print(f'A palavra {i} aparece {lista.count(i)}x na frase.')

for x in lista:  # Itera sobre a lista novamente
    qtd_vezes = lista.count(x)  # Cria a variável que vai armazenar a contagem de vezes que uma palavra aparece

    if qtd_vezes > contagem:  # Verifica se existe uma palavra na variável e se ela é maior que a variável contagem
        contagem = qtd_vezes  # Se conferir então a contagem se iguala a quantidade de vezes
        palavra = x  # Agora sim, a variável vazia indicada mais acima é preenchida com o x q é as palavras da String

for indice, real in enumerate(lista):  # Demonstra o uso do enumerate para enumerar as linhas da lista iterando sobre
    print(indice, real)  # a lista


print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

print(lista)
print(lista2)
print(string2)
