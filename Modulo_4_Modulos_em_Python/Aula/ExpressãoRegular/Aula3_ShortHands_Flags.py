"""
\w = [a-zA-Z0-9À-ú_] 
\w = [a-zA-Z0-9_] -> re.A re.ASCII
\W = [^a-zA-Z0-9_] com a letra w maiuscula é a negação, ou seja se com o minusculo é retornado palavras sem as pontuações, a negação mostra apenas as pontuações
\d = [0-9] retorna somente numéros
\D = [^0-9] retorna tudo menos os números, SEMPRE QUE A LETRA FOR MAIÚSCULA É NEGAÇÃO
\s = [ \r\n\f\n\t] encontra os espaços e quebras de linha
\b = Encontra bordas

re.A = ASCII
re.I = IGNORECASE
re.M = Multiline -> (^) Começa com, Termina com ($)
re.S = Dotall
"""
import re
 
texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve_5_filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem vem veem jã"!
'''
print(re.findall(r'[a-z]+', texto, re.I))
print()
print(re.findall(r'[a-zA-Z]+', texto))
print()
print(re.findall(r'[a-zA-Z0-9]+', texto))
print()
print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
print()
print(re.findall(r'\w+', texto))
print()
print(re.findall(r'\W+', texto))
print()
print(re.findall(r'\w+', texto, flags=re.ASCII))
print()
print(re.findall(r'\d+', texto, flags=re.ASCII))
print()
print(re.findall(r'\D+', texto, flags=re.ASCII))
print()
print(re.findall(r'\s+', texto, flags=re.ASCII))
print()
print(re.findall(r'\S+', texto, flags=re.ASCII))
print(re.findall(r'\be\w+', texto, flags=re.ASCII)) # Busca tudo que começa com uma determinada sequência de caractéres
print()
print(re.findall(r'\w+e\b', texto, flags=re.ASCII)) # Ou que terminam com determinada sequência
print()
print(re.findall(r'\b\w{4}\b', texto, flags=re.ASCII)) # Também é possível encontrar ppalavras com quantidades de caracteres
print()

cpf = """
111.258.879-56 ACB
135.685.785-98 FSSA
235.356.785-64
"""

print(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', cpf))
print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', cpf, flags=re.M))
print()

texto2 = '''O joão gosta de folia 
E adora ser amado'''

print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S)) # A flag re.S encontra as quebras de linha das strings





