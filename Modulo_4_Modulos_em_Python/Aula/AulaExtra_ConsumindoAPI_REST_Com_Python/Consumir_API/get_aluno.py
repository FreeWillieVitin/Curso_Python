import requests
# from get_token import token

url = "http://127.0.0.1:3001/alunos/1"


response = requests.get(url=url)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    # print('Texto', response.text)
    response_data = response.json()
    print(response_data)
    print(response_data['nome'])
    print(response_data['email'])
    # print('Bytes', response.content)
else:
    # Erros
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Texto', response.text)
