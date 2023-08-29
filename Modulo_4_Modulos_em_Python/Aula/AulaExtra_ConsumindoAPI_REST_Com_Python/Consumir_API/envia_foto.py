import requests
from get_token import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

mimetypes = MimeTypes()

link_img = 'Modulo_4_Modulos_em_Python\\Aula\\AulaExtra_ConsumindoAPI_REST_Com_Python\\Consumir_API\\2015-02-03-21-29-27--990592242.jpeg'

mimetypes_arquivo = mimetypes.guess_type(link_img)[0]

multipart = MultipartEncoder(fields={
    'aluno_id': '2',
    'foto': (link_img, open(link_img, 'rb'), mimetypes_arquivo)
})

url = "http://127.0.0.1:3001/fotos"

headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

user_data = {
    "nome": "Victor",
    "password": "12345678",
    "email": "teste@gmail.com"
}

response = requests.post(url=url, headers=headers, data=multipart)

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
