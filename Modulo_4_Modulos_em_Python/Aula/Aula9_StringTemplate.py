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

CAMINHO_ARQUIVO = Path(__file__).parent / 'Aula9_Texto_teste.txt'

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float | int) -> str:
    brl = locale.currency(numero, symbol=True, grouping=True)
    return brl

data = datetime(2022, 10, 28)
dados = dict(
    nome='Victor',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='Golden Shop',
    telefone='+55 (47) 3642-2479'
)

print(json.dumps(dados, indent=2, ensure_ascii=False))
print()

texto = """
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso deseje cancelar o serviço, entre em contato 
com a $empresa pelo telefone $telefone.

Atenciosamente,

${empresa},
Abraços
"""
template = string.Template(texto)
print(template.substitute(dados))
print()

# class MyTemplate(string.Template): # Alterar o delimitador do texto, não aconselhavel mas se for usar nao esquecer de aplica-lo no código de leitura do arquivo
#     delimiter = '%'

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
