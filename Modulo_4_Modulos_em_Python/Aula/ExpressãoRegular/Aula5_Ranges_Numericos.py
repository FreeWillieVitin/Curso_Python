"""
Ranges numéricos
https://regex101.com/ -> Site para criar espressões regulares usando strings de teste, e o site exibe em tempo real os resultados
"""
import re

cpf = '789.546.136-68'
cpf_verifica = re.compile(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$')
print(cpf_verifica.search(cpf))
print()

# ------------------------------------------------------------------------------------------------------------------------------------------
"""
Verifica IP
"""
ip_verifica = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5]| # 250 - 255                     
            2[0-4][0-9]| # 200 - 249
            1[0-9]{2}| # 100 - 199
            [1-9][0-9]| # 10 - 99
            [0-9] # 0 - 9
        )
        \.
    ){3}
        (?:
            25[0-5]| # 250 - 255                     
            2[0-4][0-9]| # 200 - 249
            1[0-9]{2}| # 100 - 199
            [1-9][0-9]| # 10 - 99
            [0-9] # 0 - 9
        )$
''', flags=re.X)

""" 
Versão compacta
"""
# ip_verifica = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$')

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_verifica.findall(ip))
print()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
usando o site regex101 para gerar códigos de expressão regular
"""
# Lista de CPF fictícios
# 698.547.520-54
# 060.235.190-16
# 683.134.960-96
# 899.344.730-62
# 103.778.870-21
# 721.478.580-30
# 366.310.090-14
# 794.289.350-26
# 190.259.410-01
# 000.000.000-01
# 900.000.000-00

# 000.000.000-00
# 111.111.111-11
# 222.222.222-22
# 333.333.333-33
# 444.444.444-44
# 555.555.555-55
# 666.666.666-66
# 777.777.777-77
# 888.888.888-88
# 999.999.999-99

"""https://regex101.com/r/S00xrk/1 link da expressão regular""" 

# Abaixo o código erado automáticamente pelo site de expressão regular

import re
from pprint import pprint

regex = r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})\d{3}\.\d{3}\.\d{3}-\d{2}$"

test_str = ("698.547.520-54\n"
	"060.235.190-16\n"
	"683.134.960-96\n"
	"899.344.730-62\n"
	"103.778.870-21\n"
	"721.478.580-30\n"
	"366.310.090-14\n"
	"794.289.350-26\n"
	"190.259.410-01\n"
	"000.000.000-01\n"
	"900.000.000-00\n\n"
	"000.000.000-00\n"
	"111.111.111-11\n"
	"222.222.222-22\n"
	"333.333.333-33\n"
	"444.444.444-44\n"
	"555.555.555-55\n"
	"666.666.666-66\n"
	"777.777.777-77\n"
	"888.888.888-88\n"
	"999.999.999-99")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    pprint ("Match {matchNum} was found: {match}".format(matchNum = matchNum, match = match.group()))
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
print()

"""
Validando número de telefone
"""
import re

re_meu = re.compile(r"^.\d{2}..\d{1}.\d{4}\-\d{4}$", flags=re.M) # Minha resolução
re_prof = re.compile(r"^(\(\d{2}\)\s*)(9\s*)(\d{4}-\d{4})$", flags=re.M) # Resolução do professor 

tel = ("(47) 3642-2414\n"
	"(47) 9 9292-6812\n"
	"(41) 9 9195-1123\n"
	"(31) 3851-2587\n"
	"1234-4567\n"
	"9 8571-5213")

for telefone in re_meu.findall(tel):
    print(telefone)
pprint(re_prof.findall(tel))