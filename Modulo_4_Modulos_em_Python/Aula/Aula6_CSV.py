"""
CSV (Comma Separated Values - Valores separados por vírgulas)
É um formato de arquivo que armazena dados em forma de tabela, onde cada
linha representa uma linha da tabela e as colunas são separadas por vírgulas.
Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
plataformas, como por exemplo, para importar ou exportar dados para uma
planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
editor de texto ou em uma planilha eletrônica.
Um exemplo de um arquivo CSV pode ser:
Nome,Idade,Endereço
Luiz Otávio,32,"Av Brasil, 21, Centro"
João da Silva,55,"Rua 22, 44, Nova Era"
A primeira linha do arquivo define os nomes das colunas da, enquanto as
linhas seguintes contêm os valores das linhas, separados por vírgulas.
Regras simples do CSV
1 - Separe os valores das colunas com um delimitador único (,)
2 - Cada registro deve estar em uma linha
3 - Não deixar linhas ou espaços sobrando
4 - Use o caractere de escape (") quando o delimitador aparecer no valor.

csv.reader e csv.DictReader
csv.reader lê o CSV em formato de lista
csv.DictReader lê o CSV em formato de dicionário
"""
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'Aula6_CSV.csv' # Busca o caminho do arquivo o dunder (__file__) é o caminho atual do arquivo, esse mesmo onde estou digitando e o .parent volta para uma "casa de diretório" quanto mais parents tiver mais casa voltarão e por final temos o / e o arquivo que precisamos
print(CAMINHO_CSV)


with open(CAMINHO_CSV, 'r') as arquivo: # Tendo o caminho definido vamos abrir o arquivo em modo de leitura
    leitor = csv.reader(arquivo) # Então definimos uma variável que vai receber o leitor do arquivo usando o .reader, essa função lê o arquivo e o retorna em formato de lista
    # print(next(leitor)) # Usando o next acessamos uma linha por vez

    for linha in leitor: # Então iteramos o arquivo para ter cada linha do arquivo exibida
        print(linha)
print()

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor2 = csv.DictReader(arquivo) # Aqui temos o mesmo uso do código anterior, mas lendo o arquivo em formato de dict

    for linha in leitor2:
        print(linha)
        print(linha['Nome'], linha['Idade'], linha['Endereco'])
print()
# ------------------------------------------------------------------------------------------------------------------------------------------

# Escrita
CAMINHO_CSV2 = Path(__file__).parent / 'Aula6_CSV_ESCREVER.csv'
print(CAMINHO_CSV2)

lista_clientes = [ # Uma lista com dicionários
    {'Nome': 'Victor Hugo', 'Idade': 25},
    {'Nome': 'Marieli', 'Idade': 24},
    {'Nome': 'Luiz Carlos', 'Idade': 51},
]

with open(CAMINHO_CSV2, 'w', encoding='utf8', newline='') as arquivo: # Abrimos o arquivo em modo de escrita, parece-me que no windows é necessário configurar o parâmetro newline='' pois a cada iteração o acab sendo adicionada uma linha em branco no arquivo
    nome_colunas = lista_clientes[0].keys() # Definimos a variável informando a ela que o seu valor será as chaves do indíce, não importando o valor do indíce, pois a chave é a mesma para todos os dict NESTE CASO
    # nome_colunas = ['Nome', 'Idade'] # Também podemos definir as colunas assim
    escritor = csv.writer(arquivo) # Então criamos a variável escritor, com ela poderemos inserir linhas do arquivo csv

    escritor.writerow(nome_colunas) # E usando a função writerow, indicamos ao python que o que for passado como parâmetro no caso apenas as chaves do primeiro dict da lista será escrito no arquivo, se tornando assim as colunas do arquivo csv

    for cliente in lista_clientes: # E para o resto dos dados iteramos sobre a lista
        # print(cliente.values())
        escritor.writerow(cliente.values()) # E escrevemos os seus valores

# print()

# lista = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV2, 'w') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     # coluna = ['Nome', 'Idade']
#     escritor = csv.DictWriter(
#         arquivo,
#         fieldnames=nome_colunas
#         )
    
#     escritor.writeheader()

#     for clientes in lista_clientes:
#         print(clientes)
#         escritor.writerow(clientes)