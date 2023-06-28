"""
O que é JSON - JavaScript Object Notation
JSON - JavaScript Object Notation (extensão .json)
É uma estrutura de dados que permite a serialização
de objetos em texto simples para facilitar a transmissão de
dados através da rede, APIs web ou outros meios de comunicação.
O JSON suporta os seguintes tipos de dados:
Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
  As strings devem ser envolvidas por aspas duplas
Booleanos: são os valores verdadeiro (true) ou falso (false)
Arrays: são listas ordenadas de valores, como [1, 2, 3] ou
  ["Oi", "Olá", "Bom dia"]
Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 30}
null: é um valor especial que representa ausência de valor

Ao converter de Python para JSON:
Python        JSON
dict          object
list, tuple   array
str           string
int, float    number
True          true
False         false
None          null
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
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Carregar um arquivo json
with open('arquivo-python.json', 'r', encoding='utf-8') as file: # Agora iremos ler esse arquivo json, para isso abrimos o arquivos em modo read de leitura
    arquivos = json.load(file) # Salvamos em variável o arquivo carregado usando a função load(alias do caminho e modo do arquivo)
    print(arquivos) # Exibimos o conteúdo que será convertido para modo de leitura python
    print()
    for arquivo in arquivos: # É possivel também iterar sobre o arquivo json e retornar valores desejados
       print(arquivo['nome']) 
print()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import json
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list
    budget: None


string_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel", 
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''

movie: Movie = json.loads(string_json) # Transforma de json para python
pprint(movie)
print(movie['title'])
print(movie['characters'][1])
print(movie['year'] + 10)
print()
return_to_json = json.dumps(movie, ensure_ascii=False, indent=2) # Transforma de python para json
print(return_to_json)
print()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
json.dump e json.load com arquivos
"""
import json
import os

string_json2 = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel", 
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''

dict_movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 
    'is_movie': True,
    'imdb_rating': 8.8, 
    'year': 2001, 
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 
    'budget': None
}

json_to_python = json.loads(string_json2)
 
NOME_ARQUIVO = 'aula_sobre_json.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join('\\Users', 'Victor', 'Desktop','AULA_EU', NOME_ARQUIVO)
)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as desc_filme:
    json.dump(dict_movie, desc_filme, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as desc_filme:
    filme_do_json = json.load(desc_filme)
    print(filme_do_json)