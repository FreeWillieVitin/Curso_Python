"""
O módulo os para interação com o sistema
Doc: https://docs.python.org/3/library/os.html
O módulo `os` fornece funções para interagir com o sistema operacional.
Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
diretório. O método os.system() permite executar comandos do sistema
operacional a partir do seu código Python.
Windows 11 (PowerShell), Linux, Mac = clear
Windows (antigo, cmd) = cls
"""
import os
os.system('cls') # Limpa o prompt a cada execução
os.system('echo "Hello World"') # Exibe a frase Hello World no prompt através do comando echo, pode ser implementado no codigo python através do módulo os e usando a função system, ou pode ser executado direto no prompt


print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print()
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Doc: https://docs.python.org/3/library/os.path.html#module-os.path
os.path é um módulo que fornece funções para trabalhar com caminhos de
arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
entre esses sistemas.
Exemplos do os.path:
os.path.join: junta strings em um único caminho. Desse modo,
os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
'pasta1\\pasta2\arquivo.txt' no Windows.
os.path.split: divide um caminho uma tupla (diretório, arquivo).
Por exemplo, os.path.split('/home/user/arquivo.txt')
retornaria ('/home/user', 'arquivo.txt').
os.path.exists: verifica se um caminho especificado existe.
os.path só trabalha com caminhos de arquivos e não faz nenhuma
operação de entrada/saída (I/O) com arquivos em si.
"""
import os

caminho = os.path.join('\\Modulo_4_Modulos_em_Python', 'Aula', 'Aquivo.txt') #  A função join do módulo os, monta um caminho para criação de pastas, localização de arquivos, tranfêrencias de arquivos e outras funções
print(caminho) # Exibe o caminho criado
diretorio, arquivo = os.path.split(caminho) # A função split divide o caminho do arquivo entre o seu diretório e o nome do arquivo com sua extensão, usasse duas variáveis na função, uma parareceber o caminho e a outra para receber o arquivo
caminho_arquivo, extensao = os.path.splitext(caminho) # Já o splitext divide entre o caminho do arquivo e a extesão do arquivo, pode ser usado para filtragem de tipos de arquivo, por exemplo .txt
print(diretorio) 
print(arquivo)
print(caminho_arquivo)
print(extensao)
print()
print(os.path.exists(caminho)) # Verifica se o caminho passado como parâmetro existe ou não, podendo ser uma variável ou o caminho escrito manualmente
print(os.path.exists('C:\\Users\\Victor\\Documents\\GitHub\\professor\\Curso_Python\\Modulo_4_Modulos_em_Python'))
print()
print(os.path.abspath('.')) # Retorna o caminho absoluto
print(os.path.basename(caminho)) # Retorna o ultimo digamos item pertencente ao caminho, no caso do exemplo a última parte do caminho é o arquivo.txt
print(os.path.dirname(caminho)) # Retorna somente o diretório, sem os arquivos presentes
print()
# ----------------------------------------------------------------------------------------------------------------------------------------

"""
os.listdir para navegar em caminhos
C:\\Users\\Victor\\Desktop\\imagens
"""
caminho2 = ('C:\\Users\\Victor\\Desktop\\imagens') # Variável armazenando o caminho completo do arquivo

for pasta in os.listdir(caminho2): # A função listdir é usada para listar tudo o que está dentro do arquivo, seus documentos, subpastas, imagens e etc
    caminho_completo = os.path.join(caminho2, pasta) # É uma função iteravel, o python itera sobre o caminho e retorna item por item
    print(pasta)

    if not os.path.isdir(caminho_completo):
        continue
    
    for imagem in os.listdir(caminho_completo):
        print('  ', imagem)
print()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
os.walk
os.walk é uma função que permite percorrer uma estrutura de diretórios de maneira recursiva.
Ela gera uma sequencia de tuplas, onde cada tupla possui três elementos: O diretório atual (root), uma lista de subdiretórios (dirs)
e uma lista dos arquivos do diretório atual (files).
"""
import os
from itertools import count

caminho3 = os.path.join('\\Users', 'Victor', 'Desktop', 'Xpadder 5.7 JogoGames Br (Atualizado)')
counter = count()

for root, dirs, files in os.walk(caminho3):
    the_counter = next(counter)
    print(the_counter, 'Root:', root)

    for dir_ in dirs:
        print(the_counter, 'Dir', dir_)

    for file_ in files:
        print(the_counter, 'Files', file_)
        caminho_completo2 = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', caminho_completo2)
        # os.unlink(caminho_completo2) # Exclui todos os arquivos que estão nesse caminho NÃO EXECUTAR DE JEITO NENHUM PELO AMOR DE DEUS
print()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
os.path.getsize e os.stat para dados dos arquivos
"""
import math

def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return '0B'
    
    # Tupla com os tamanhos
    #                      0    1     2     3     4     5 
    abreviacao_tamanhos = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para gerar o tamanho correto
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = round(tamanho_em_bytes / potencia, 2)
    # Abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final} {abreviacao_tamanho}'

print(formata_tamanho(10000))

caminho4 = os.path.join('\\Users', 'Victor', 'Desktop', 'Xpadder 5.7 JogoGames Br (Atualizado)')

for root, dirs, files in os.walk(caminho4):
    the_counter = next(counter)
    print(the_counter, 'Root:', root)

    for dir_ in dirs:
        caminho_completo4 = os.path.join(root, dir_)
        stats = os.stat(caminho_completo4)
        tamanho = stats.st_size
        print(the_counter, 'Dir', dir_, formata_tamanho(tamanho))

    for file_ in files:
        caminho_completo3 = os.path.join(root, file_)
        tamanho1 = os.path.getsize(caminho_completo3)
        print('  ', the_counter, 'FILE:', caminho_completo3, formata_tamanho(tamanho1))
print()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
os + shutil - Mover, copiar e apagar arquivos
1 - Vamos arquivos de uma pasta para outra
Mover/Renomear -> shutil.move
Mover/Renomear -> os.rename
Copiar -> shutil.copy
Apagar -> os.unlink
Apagar diretório recursivamente -> shutil.rmtree
echo $HOME
"""
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'imagens')
NOVA_PASTA = os.path.join(DESKTOP, 'AULA')

# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_original = os.path.join(root, file)
#         caminho_nova_pasta = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
#         shutil.copy(caminho_original, caminho_nova_pasta)
#         print(caminho_nova_pasta)

# shutil.rmtree(NOVA_PASTA, ignore_errors=True)
# os.unlink(NOVA_PASTA)
# shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EU')