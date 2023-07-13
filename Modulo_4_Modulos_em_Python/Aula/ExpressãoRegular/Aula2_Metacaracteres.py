"""
Meta Caracteres: . ^ $ * + ? { } [ ] \ | ( )
| = ou
. = Qualquer caractere (com exceção da quebra de linha)
[] = Conjunto de caracteres
"""
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem vem veem jã"!
'''

print(re.findall(r'João|Maria|maria|sua', texto))
print(re.findall(r'João|.aria|sua', texto))
print(re.findall(r'[a-zA-Z0-9]oão|[Mm]aria|sua', texto))
print(re.findall(r'jOãO|MaRiA|SUa', texto, flags=re.I)) # flags=re.I = Encontra a palavra independende da case das letras
print()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Meta Caracteres: . ^ $ * + ? { } [ ] \ | ( )
Quantificadores
* 0 ou n
+ 1 ou n Sempre aplicado ao caracter á esquerda
? 0 ou 1
{n}
{min, max}
{10,} 10 ou mais
{,10} de zero a 10
{5,10} De 5 a 10
()+ [a-zA-Z0-9]
"""
print(re.findall(r'jo+ão|Ve+m', texto, flags=re.I)) 
print(re.findall(r'jo*ão*|Ve+m', texto, flags=re.I)) 
# print(re.sub(r'jo+ão+', 'Victor', texto, flags=re.I)) 
print(re.findall(r'jo{1,2}ão{1,}|Ve+m', texto, flags=re.I)) 
print(re.findall(r'Ve{3}m{1,2}', texto, flags=re.I)) 
print()

texto2 = 'João ama ser amado'
print(re.findall(r'ama', texto2, flags=re.I)) 
print(re.findall(r'ama[do]', texto2, flags=re.I)) 
print(re.findall(r'ama[do]{2}', texto2, flags=re.I)) 
print(re.findall(r'ama[od]*', texto2, flags=re.I)) 
print(re.findall(r'ama[od]{0,2}', texto2, flags=re.I)) 
print()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Quantificadores (Greedy e non-Greedy (l'azy))
* 0 ou n
+ 1 ou n 
? 0 ou 1
"""
texto3 = """
<p>Te amo</p> <p>muito</p> <p>meu amor</p> <div></div>
"""

print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto3)) # Comportamento Greedy(guloso)
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto3)) # Comportamento non-greedy (não gulosd ou preguiçoso)
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto3))
print()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Meta Caracteres
Grupos e retrovisores: ^ $
() = Grupo
"""
texto4 = """
<p>Te amo</p> <p>muito</p> <p>meu amor</p> <div>1</div>
"""
tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', texto4)
print(tags)

for tag in tags:
    um, dois, tres = tag
    print(um)
    print(dois)
    print(tres)

print(re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto4))
print(re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', texto4))

cpf = 'sdasdas145.138.874-98'
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}', cpf))
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1Abublé"\3"\4', texto4))





