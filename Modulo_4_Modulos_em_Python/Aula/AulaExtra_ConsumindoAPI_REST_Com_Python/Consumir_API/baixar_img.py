import requests

url = "http://localhost:3001/images/1693271310538_15537.jpeg"

nome_arquivo = url.split('/')[-1]

response = requests.get(url)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status Code', response.status_code)
    print('Reason', response.reason)

    with open(nome_arquivo, 'wb') as file:
        file.write(response.content)

else:
    # Erros
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Texto', response.text)
