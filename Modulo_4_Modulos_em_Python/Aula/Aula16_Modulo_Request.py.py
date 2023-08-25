"""
Módulo requests - Usado para requisições HTTP
Tutorial de requests -> https://www.youtube.com/watch?v=Qd8JT0bnJGs
"""
import requests

# http:// -> Significa que o site esta rodando na porta 80 por padrão
# https:// -> Significa que o site esta rodando na porta 443 por padrão

url = 'https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api'

response = requests.get(url)

print(response)
print(response.headers)
print(response.status_code)
# print(response.content)
print(response.text)


