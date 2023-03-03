"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1 # Variavel fora de uma função
z = 2
def escopo(): # Definido uma função
    global z # Definir uma variavel global indica que o valor dela será o mesmo em todo o sistema até que outra variavel global á altere
    x=10 # Variavel com o mesmo nome porém em um escopo de função, indica que ela terá um valor diferente pois nao estar definida em um mesmo escopo
    z=5 # Até o momento a variável global de z é 5
    def outra_funcao(): # É possível criar uma função dentro de outra, mas ela só pode ser chamada dentro da função anterior
        global z # Novamente indica o z como variável global
        x = 11 # Uma nova variavél x é criada q terá o seu proprio valor sem afetar a anterior
        y = 2 # Variável y recebe um valor
        z = 9 # Como foi caracterizado z como global novamente dentro de uma nova função, a definição anterior como global é ignorada e o valor passa a ser 9
        print(x,y,z)
    outra_funcao()
    print(x,z)

print(x,z)
escopo()
print(x,z)