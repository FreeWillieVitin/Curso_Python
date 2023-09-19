"""
Secrets gera números aleatórios seguros
Documentação: https://docs.python.org/3/library/secrets.html
"""
import secrets
import random


print(secrets.randbelow(100))
print(secrets.choice([10, 11, 12]))
print()

random = secrets.SystemRandom()

"""
Funções:
seed
  -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
random.seed(0)
"""
random.seed(0)  # Não faz nada com o SystemRandom ativo

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

# --------------------------------------------------------------------------------------------------------------------------------
import string as s
from secrets import SystemRandom as sr

# O modulo string, nos dá acesso aos caracters por exemplo: (ascii_letters = todas as letras maiusculas e minusculas seguindo o
# padrão ascii, digits = números de 0 a 9, punctuation = caracteres especias como *,+,/ e outros)
print(s.ascii_letters + s.digits + s.punctuation)
# A classe SystemRandom, inutiliza as seed, ou seja independente da seed se inserida manualmente ou não o valor gerado é sempre
# aleatorio, no codigo de exemplo é misturado aléatoriamente os caracteres sem se importar com a seed passada
print(''.join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))
