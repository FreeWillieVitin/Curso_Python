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
pessoas = [
    {
        "nome": 'Víctor',
        "sobrenome": 'Hugo',
        "idade": 25,
        "ativo": False,
        "notas": ['A','A+'],
        "telefones":{
            "residencial": '47 3642-2414',
            "celular": '47 99292-6812',
        }
    },
    {
        "nome": 'Luiz',
        "sobrenome": 'Carlos',
        "idade": 51,
        "ativo": True,
        "notas": ['B','A'],
        "telefones":{
            "residencial": '47 3642-2414',
            "celular": '47 98402-7387',
        },
    },
]

# Salvando dados em json
with open('arquivo-python.json', 'w+') as file: # Cria um arquivo de tipo json em modo de escrita
    json.dump(pessoas, file, ensure_ascii=True, indent=2) # Salva todos os dados possiveis de serem salvos dentro desse arquivo criado, passado 2 parametros, ensure_ascii para reconhecer caracteres em ascii
    # E o parametro indent que vai organizar o arquivos json de forma mais visualizavel
print(json.dumps(pessoas, indent=2))
# -----------------------------------------------------------------------------------------------------------------------------------

# Carregar um arquivo json
with open('arquivo-python.json', 'r', encoding='utf-8') as file: # Agora iremos ler esse arquivo json, para isso abrimos o arquivos em modo read de leitura
    arquivos = json.load(file) # Salvamos em variável o arquivo carregado usando a função load(alias do caminho e modo do arquivo)
    print(arquivos) # Exibimos o conteúdo que será convertido para modo de leitura python
    print()
    for arquivo in arquivos: # É possivel também iterar sobre o arquivo json e retornar valores desejados
       print(arquivo['nome']) 