"""
Módulo requests - Usado para requisições HTTP
Tutorial de requests -> https://www.youtube.com/watch?v=Qd8JT0bnJGs
Vebos HTTP => https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods
"""
import requests

# http:// -> Significa que o site esta rodando na porta 80 por padrão
# https:// -> Significa que o site esta rodando na porta 443 por padrão

url = 'http://localhost:3333/'  # Define o valor da variável como sendo o link

# Cria uma variável que recebe a função get do modulo request, get é o método que requisita dados do servidor
# response = requests.get(url)

# print(response)  # Exibe a mensagem de resposta do servidor
# print(response.headers)  # Exibe todo o cabeçalho, ou seja informações de data de moificação, conteúdo, servidor e etc
# print(response.status_code)  # Exibe apenas o código HTTP enviado ao usuário
# # print(response.content)
# print(response.text)  # Se permitido exibe o código html da página, se permitido porque isso pode ser restrito conforme a página

"""
+ Web Scraping com Python usando requests e bs4 BeautifulSoup
- Web Scraping é o ato de "raspar a web" buscando informações de forma
automatizada, com determinada linguagem de programação, para uso posterior.
- O módulo requests consegue carregar dados da Internet para dentro do seu
código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
em formato de objetos Python para facilitar a vida do desenvolvedor.
- Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
+ Instalação
- pip install requests types-requests bs4
"""
from bs4 import BeautifulSoup
import requests
import re

url1 = 'http://localhost:3333/'

response1 = requests.get(url)
raw_html = response1.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

if parsed_html.title is not None:
    print(parsed_html.title.text)

h2_html = parsed_html.select_one('#main-header > div.main-header-content > h2')
print(h2_html)
if h2_html is not None:
    print(h2_html.text)
    div = h2_html.parent
    print(div)
    print('')

    if div is not None:
        for p in div.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
