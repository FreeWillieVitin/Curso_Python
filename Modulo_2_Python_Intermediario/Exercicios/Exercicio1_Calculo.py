# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
def duplica(x):
    return x * 2

def triplica(x):
    return x * 3

def quadruplica(x):
    return x * 4

def multiplicar(y):
    def multiplicando(z):
        return y * z
    return multiplicando

num1 = multiplicar(int(input("Digite um número: ")))
print(num1(int(input('Digite um numero: '))))
print(num1(2))
print(num1(3))
print(num1(4))


# d = duplica(int(input('Digite um número: ')))
# t = triplica(int(input('Digite um número: ')))
# q = quadruplica(int(input('Digite um número: ')))
# print(d)
# print(t)
# print(q)
