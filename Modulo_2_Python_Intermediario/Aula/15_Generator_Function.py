"""
Introdução às Generator Functions em Python
Generator = (n for n in range(1000))
Continuação da Aula 22 do Modulo 1 Estrutura_For Seção iterator
"""
def generator(n=0): # Seguindo com o generator, conhecemos a palavra chave yield, funciona como o return na função, mas em vez de encerrar a execução dela, o yield retorna um dos valores e pausa
    yield 1 # Para ser acessado quando for chamado novamente, nessa função de exemplo temos 3 palavra chave yield, a primeira retorna o valor 1, após isso ela congela e espera a proxima chamada
    print('Continuando...') # A proxima chamda da função continuará de ontem parou ou seja, mostrará o print e o valor 2 que é onde está presente o segundo yield
    yield 2 # Assim por diante até encontrar o fim, que no caso é a palavra chave ja conhecida return
    print('Mais uma...')
    yield 3
    print('Terminar')
    return 'ACABOU'

gen = generator(n=0) # Executamos a função a cima que se inicia com o valor do argumento n em 0
print(next(gen)) # Então chamamos o primeiro yield, modificando o valor de n para 1
print(next(gen)) # Aqui executamos o segundo yield, mudamos o valor de n para 2 e executamos o print e pausamos novamente
"""
Vantagem de utilizar o yield é que ocupamos menos espaço na memória, uma vez que a execução acontece somente quando o chamador itera sobre o objeto.
E que como a variável salva o seu estado quando o yield "pausa a execução" podemos retomar ele quando quisermos
"""
print()

for n in gen: # Demonstração de continuidade fica clara nesta iteração, a execução da funçãoestava manual usando o método next, mas ao iterar a função não é executado nem o primeiro e nem o segundo yield
    print(n) # Mas sim seguimos com o terceiro yield pois foi onde a variável salvou a execução da função

def generator2(n=0, maximun=None):
    while True:
        yield n
        n +=1

        if n > maximun:
            return

gen2 = generator2(maximun=100)
for n in gen2:
    print(n)

print()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yield From
"""
O yield from é usado para seguir um sequencial apartir de duas ou mais funções.
"""
def generator3(): # Quando criamos uma função e queremos unir o yields com o de outra função então usamos a palavra chave yield from
    yield 1
    yield 2
    yield 3
    print('Acabou o gen3')
    print()

def generator4(gen):
    yield from gen() # Aqui podemos ver que a função tem um argumento e o yield from vai receber esse argumento quando a função for executada
    yield 4
    yield 5
    yield 6

g = generator4(generator3) # No caso o argumento é a primeira função, então ao iterar essa variável que executa a segunda função, teremos uma união de dados da primeira e segunda função
for i in g:
    print(i)