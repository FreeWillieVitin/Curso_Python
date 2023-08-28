import requests
from get_token import token

url = "http://127.0.0.1:3001/alunos/3"

headers = {
    'Authorization': token
}

aluno_data = {
    "nome": "Luiz",
    "sobrenome": "Carlos Jurczyszyn",
    "email": "Pai@gmail.com",
    "idade": "25",
    "peso": "84.04",
    "altura": "1.70"
}

response = requests.put(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    # print('Texto', response.text)
    response_data = response.json()
    print(response_data)
    # print('Bytes', response.content)
else:
    # Erros
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Texto', response.text)
