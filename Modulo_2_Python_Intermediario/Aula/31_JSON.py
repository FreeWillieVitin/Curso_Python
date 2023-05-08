"""
O que é JSON?
É Basicamente uma estrutura de dados que foi criado para transportar ou salvar dados

Tipos de dados em JSON
true or false - Boolean
1234.12 - number
null - false
''string'' - texto
[] - array
{} - objeto

"""
import json
import os
# pessoas = [
#     {
#         "nome": 'Victor',
#         "sobrenome": 'Hugo',
#         "idade": 25,
#         "ativo": False,
#         "notas": ['A','A+'],
#         "telefones":{
#             "residencial": '47 3642-2414',
#             "celular": '47 99292-6812',
#         }
#     },
#     {
#         "nome": 'Luiz',
#         "sobrenome": 'Carlos',
#         "idade": 51,
#         "ativo": True,
#         "notas": ['B','A'],
#         "telefones":{
#             "residencial": '47 3642-2414',
#             "celular": '47 98402-7387',
#         },
#     },
# ]

# BASE_DIR = os.path.dirname(__file__)
# SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

# with open(SAVE_TO, 'w+') as file:
#     json.dump(pessoas, file, indent=2)

# print(json.dumps(pessoas, indent=2))
# -----------------------------------------------------------------------------------------------------------------------------------
# Carregar um arquivo json

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')


with open(JSON_FILE, 'r') as file:
    arquivos = json.load(file)
    print(arquivos)
    print()
    for arquivo in arquivos:
       print(arquivo['nome']) 