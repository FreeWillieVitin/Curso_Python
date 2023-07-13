"""
Expressão regular -  Verificar padrões de caracteres em strings
https://docs.python.org/3/library/re.html
https://docs.python.org/3/howto/regex.html#regex-howto

"""
import re

string = 'Teste de Expressão regular. Teste, Teste'
print(re.search(r'Teste', string)) # <re.Match object; span=(0, 5), match='Teste'>
print(re.findall(r'Teste', string)) # Retorna uma lista com todas as vezes que a palavra aparece na string
print(re.sub(r'Teste', 'ABCD', string))
print(re.sub(r'Teste', 'ABCD', string, count=1))
print()

regexp = re.compile(r'Teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('Truco', string))
