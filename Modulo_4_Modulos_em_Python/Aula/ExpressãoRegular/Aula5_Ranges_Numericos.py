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