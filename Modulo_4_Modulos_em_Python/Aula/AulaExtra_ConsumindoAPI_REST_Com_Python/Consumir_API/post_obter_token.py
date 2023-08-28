import requests

url = "http://127.0.0.1:3001/tokens"

user_data = {
    "password": "12345678",
    "email": "teste@gmail.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    # print('Texto', response.text)
    response_data = response.json()
    token = response_data['token']

    with open('Modulo_4_Modulos_em_Python\\Aula\\AulaExtra_ConsumindoAPI_REST_Com_Python\\Consumir_API\\token.txt', 'w') as file:
        file.write(token)
    # print('Bytes', response.content)
else:
    # Erros
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Texto', response.text)
