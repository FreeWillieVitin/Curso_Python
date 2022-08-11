"""
Manipulando Strings
* String indicas
* Fatiamento de strings
* Funções built-in len, abs, type, print, etc
Essas funções podem ser usadas diretamente em cada tipo.
"""
# Indices positivos  [012345678]
texto               ='Python s2'
print(texto[2])
# Indices negativos -[987654321]
url = 'www.google.com/'
print(url[:-1])
# Fatiamento
fat = texto[0:6]
print(fat)
# Pular caracteres
print(texto[0:6:2]) # 0 = começo, 6 = até onde vai, 2 = de quantos em quantos caracteres ele vai pular
print(len(url))
