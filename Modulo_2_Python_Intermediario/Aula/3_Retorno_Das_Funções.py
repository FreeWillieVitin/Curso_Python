"""
Retorno de valores das funções (return)
"""
def soma (x, y): # Aqui temos uma função que mostrará em tela a soma dos dois valores
    print(x + y) # Porém a função print é uma fução de tipo none, ou seja ela nao retorna valor nenhum, apenas mostra em tela o que está sendo pedido
# Por esse motivo, não podemos colocar em variável um print e esperar q ele execute alguma ação como por exemplo da soma de duas variáveis  
soma1 = soma(2, 4) # Tentamos armazenar em variável a função soma, sendo passado 2 valores que deveriam ser somados e armazenados
soma2 = soma(6, 9) # Mas pela função ter um print como realizador da soma, vai ser armazenado na variavel apenas o valor none e valores none não podem ser somados por nao serem literais
print(soma1 + soma2) # Ao executar a soma das duas variaveis, vamos receber um erro, porque none + none não é aceito pelo python

def somar (x, y): # Para realizar o armazenamento em variavel de dois valores da função, temos uma outra função para isso, a função return
    if x > 10:
        return [10, 20] # A função return literalmente retorna o valor que foi aplicado, nao sendo mais um tipo none
    else:
        return x + y # Então se seguirmos a condição passad acima será retornado para as variaveis os valores passados como parametro para x e y, sendo realizado uma soma entre eles


somar1 = somar(2, 4) # Dessa forma o 2 e o 4 que foram passados como parametro, vai realmente ser o valor que a variavel vai receber e realizar a soma que foi definida na função
somar2 = somar(6, 9)
print(somar1 + somar2) # E dessa forma podemos até usarmos as variáveis para realizar ações, pois dessa vez eles tem valores e tipos validos
print(somar(20, 60))

