"""
# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
"""
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

RAIZ = Path(__file__).parent
PASTA_PDF = RAIZ / 'PDFS'
PASTA_NOVA = RAIZ / 'arquivos novos'
RELATORIO = PASTA_PDF / 'RelatorioFocus.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

leitor = PdfReader(RELATORIO)

print(len(leitor.pages))

for pages in leitor.pages:
    print(pages)
print()

# Extrair imagem de um PDF
pagina1 = leitor.pages[0]
imagem1 = pagina1.images[1]

print(pagina1.extract_text())
print(len(pagina1.images))
print(pagina1.images[1])
print('')

with open(PASTA_NOVA / imagem1.name, 'wb') as imagem:
    imagem.write(imagem1.data)
print('')
# --------------------------------------------------------------------------------------------------------------------------------

# Manipular PDFs e Criar novos
pagina2 = leitor.pages[1]
escrever = PdfWriter()

# escrever.add_page(pagina2)
# with open(PASTA_NOVA / 'pagina2.pdf', 'wb') as arquivo:
#     escrever.write(arquivo)  # type: ignore

# with open(PASTA_NOVA / 'pagina2.pdf', 'wb') as arquivo:
#     for page in escrever.pages:
#         escrever.add_page(page)
#     escrever.write(arquivo)


for i, page in enumerate(leitor.pages):
    escrever = PdfWriter()
    with open(PASTA_NOVA / f'pagina{i}.pdf', 'wb') as arquivo:
        escrever.add_page(page)
        escrever.write(arquivo)
print('')
# --------------------------------------------------------------------------------------------------------------------------------

# Unir PDFs
files = [
    PASTA_NOVA / 'pagina0.pdf',
    PASTA_NOVA / 'pagina1.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / 'merge.pdf')
merger.close
