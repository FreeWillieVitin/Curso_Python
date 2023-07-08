"""
Secrets gera números aleatórios seguros
"""
import secrets
import random


print(secrets.randbelow(100))
print(secrets.choice([10,11,12]))
print()

random = secrets.SystemRandom()

"""
Funções:
seed
  -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
random.seed(0)
"""
# random.seed(0) # Não faz nada com o SystemRandom ativo

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
print()

# --------------------------------------------------------------------------------------------------------------------------------------
import string as s
from secrets import SystemRandom as sr

print(s.ascii_letters + s.digits + s.punctuation)
print(''.join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))

