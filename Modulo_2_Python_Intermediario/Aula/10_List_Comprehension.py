# List comprehension em python
# List Comprehension é uma forma rápida para criar listas a partir de iteráveis.
import pprint # Importa um modulo que vai ser visto mais a frente, que executa prints mais organizados
def p(v): # Função para executar o pprint
    pprint.pprint(v, sort_dicts=False, width=40)

# Abaixo temos 3 formas de executar a mesma coisa
print(list(range(10))) # Aqui temos um print de uma lista, que apesar de ser uma linha de codigo curto, não é uma boa pratica de se exibir uma lista e muito menos de armazena-la

lista = [] # Já aqui temos a lista vazia e abaixo será feito uma iteração e com os valores dessa iteração, executamos um append e inserimos dados para a lista
for numero in range(10): # Apesar de correto é usado muitas linas de código para solucionar o problema, então desta para este caso, os é apresentado as list comprehension
    lista.append(numero)
print(lista)

lista2 = [numero * 2 for numero in range(10)] # List comprehension nada mais é que criar a lista usando iteraveis e desta forma teruma certa customização melhor sobre ele
print(lista2) # Acima temos uma variavel que guarda uma lista, dentro desta lista é passado um iteravel, da mesma forma que no exemplo anterior usando o for
print() # E a esquerda do for podemos passar as ações que vao ser realizadas pela iteração, assim conseguimos criar uma lista com valores iteraveis usando apenas uma linha de codigo
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 30,}, # O mapeamento de dados diz que ao transpassarmos valores de uma lista para uma outra, precisamos que esses existam os mesmos indices da anterior na nova
    {'nome': 'p3', 'preco': 40,}, # Aqui temos uma lista com 3 dicionarios dentro, com 1 item em cada, como informações de um produto
]
antigo_preco = [produto_antigo for produto_antigo in produtos] # Para uma explicação melhor criamos uma variavel e nela é inserido uma lista iterando sobre a lista produtos
print(*antigo_preco, sep='\n') # Usando o * mostramos todos os itens presentes nela

print()

novos_produtos = [{**produto, 'preco': produto['preco'] * 2}  # Agora vamos iterar novamente sobre produtos, só que desta vez teremos algumas condições, como o aumento do preço de alguns itens
                  if produto['preco'] > 30 else {**produto} for produto in produtos] # A iteração com o for esta presente e a esquerda dele temos uma condição ternária que indica que
print(*novos_produtos, sep='\n') # Haverá aumento apenas nos produtos com preço acima de 30 e mais a esquerda da condicional, temos a ação que vai receber todos os preços dos produtos
print() # E com os preços ai sim será checado a condicional e naqueles que tiverema condicional verdadeira terá o valor multiplicado por 2
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Filtro
lista3 = [n for n in range(10) if n < 5] # Da mesma forma que em uma iteração for, podemos fazer filtros dentro de um list comprehension, os filtros ficam a direita do iteravel
p(lista3) # Como podemos ver acima temos a variavel iteravel n em um range de 10 e a direita dele temos o filtro com o if, que para a iteração quando chegar a um valor

novos_produtos2 = [{**produto, 'preco': produto['preco'] * 2} 
                  if produto['preco'] > 20 else {**produto} for produto in produtos # Usando o caso dos produtos, estamos filtrando a exibição apenas para produtos com preço maior que 20
                  if (produto['preco'] > 20)] # Tudo isto pode ser escrito em apenas uma linha, mas como boa pratica é importante organizar a sua list comprehension
print(*novos_produtos2, sep='\n')
print()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List Comprehension com mais de um for

lista4 = []
for x in range(3):
    for y in range(3):
        lista4.append((x, y))

p(lista4)

# Aqui temos dois exemplos de iteração com mais de um for, acima iterando de forma convecional e inserindo posteriormente na lista vazia, e abaixo usando o list comprehension
# Mais limpo e de melhor entendimento, as list comprehension facilitam muito quando precisamos iterar listas

lista5 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print()
p(lista5)
print()

# Strings
string = 'Victor Hugo' # Não são apenas listas que podem ser iteradas, podemos usar list comprehension para iterar sobre strings, aqui temoos uma variável que recebe um nome
num_letra = 1 # Essa variável, vai contar quantas letras serão puladas para a inserção de um caracter separador, que no caso é o ., inserido com a função join
nova_string = '.'.join([ # Então a nova string vai receber a iteração da variavel string mais um . após cada letra, com range de 0 até o limite da palavra usada como string
    string[indice:indice + num_letra]
    for indice in range(0, len(string))
])
print(nova_string)

nomes = ['victor', ' marieli', ' luiz', 'judite']
novos_nomes = [f'{nome[:-1]}{nome[-1].upper()}' for nome in nomes]
print(novos_nomes)