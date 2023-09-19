"""
# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
"""
import random
import time

"""
Funções:
seed
  -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
random.seed(0)
"""
# random.seed(0)
# random.seed(time.time())
# print(time.time())

"""
random.randrange(início, fim, passo)
  -> Gera um número inteiro aleatório dentro de um intervalo específico
"""
aleatorio = random.randrange(10, 20, 2)
print(aleatorio)
print()

"""
random.randint(início, fim)
  -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
"""
aleatorio1 = random.randint(10, 20)
print(aleatorio1)
print()

"""
random.uniform(início, fim)
  -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
"""
aleatorio2 = random.uniform(10, 20)
print(f'{aleatorio2:.2f}')
print()

"""
random.shuffle(SequenciaMutável) -> Embaralha a lista original
"""
nomes = ['Victor', 'Hugo', 'Marieli', 'Luiz', 'Carlos']
random.shuffle(nomes)
print(nomes)
print()

"""
random.sample(Iterável, k=N)
  -> Escolhe elementos do iterável e retorna outro iterável (não repete)
"""
novos_nomes = random.sample(nomes, k=2)
print(novos_nomes)
print()

"""
random.choices(Iterável, k=N)
  -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
"""
novos_nomes = random.choices(nomes, k=2)
print(novos_nomes)
print()

"""
random.choice(Iterável) -> Escolhe um elemento do iterável
"""
print(random.choice(nomes))
