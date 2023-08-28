import requests

url = "http://127.0.0.1:3001/users"

user_data = {
    "nome": "Victor",
    "password": "12345678",
    "email": "teste@gmail.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Texto', response.text)
    print('JSON', response.json())
    # print('Bytes', response.content)
else:
    # Erros
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Texto', response.text)
