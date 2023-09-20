"""
string.Template para substituir variável de uma texto
doc: https://docs.python.org/3/library/string.html#template-strings
Métodos:
substitute: substitui mas gera erros se faltar chaves
safe_substitute: substitui sem gerar erros
Você também pode trocar o delimitador e outras coisas criando uma subclasse
de template.
"""
import json
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'Aula9_Texto_teste.txt'  # variável que armazena o caminho de um arquivo de texto

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float | int) -> str:  # Função que usa o localização atual e converte simbolos monetários
    brl = locale.currency(numero, symbol=True, grouping=True)
    return brl


data = datetime(2022, 10, 28)  # Variável com uma data pré-estabelecida
dados = dict(  # Dicionário de onde os valores serão repassados para o arquivo txt
    nome='Victor',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='Golden Shop',
    telefone='+55 (47) 3642-2479'
)

print(json.dumps(dados, indent=2, ensure_ascii=False))  # Converte as informações do dicionário para JSON
print()

# O texto abaixo, é um texto normal que será passado para o arquivo, as informações que vão receber os dados do dicionário ficam
# após o símbolo $ e seguido de colchetes, dentro dos colchetes informamos a chave da informação que será passada da mesma forma
# que está escrito no dicionário, ou podemos usar apenas o símbolo de cifrão $ seguido da chave.
texto = """
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso deseje cancelar o serviço, entre em contato
com a $empresa pelo telefone $telefone.

Atenciosamente,

${empresa},
Abraços
"""
template = string.Template(texto)  # Variável que recebe o template do texto acima, dando assim a posibilidade de substituição
print(template.substitute(dados))  # A função substitute troca os colchetes com chaves pelos dados do dicionário
print()

# class MyTemplate(string.Template): # Alterar o delimitador do texto, não aconselhavel mas se for usar nao esquecer de aplica-lo
#     delimiter = '%'                # no código de leitura do arquivo

# Também podemos ler um arquivo pronto e somente realizar as substituiçõe, dessa forma precisamos criar o arquivo de texto em
# txt ou qualquer escrito de texto nos mesmo padrões acima e executar as substituições
with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
