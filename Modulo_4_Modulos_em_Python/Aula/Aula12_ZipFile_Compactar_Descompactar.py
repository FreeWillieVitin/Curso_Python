"""
ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
"""
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminho
CAMINHO_RAIZ = Path(__file__).parent  # Acessa a pasta raiz do sistema, ou seja a pasta onde a aula está salva
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'Aula12_Diretorio_zip'  # Uma pasta dentro do caminho raiz
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'Aula12_Compactado.zip'  # E Dentro da raiz também teremos o arquivo em formato zip
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'Aula12_Descompactado'  # E ainda no diretório raíz é onde será descompactado o arquivo zip

# Excluimos tudo como forma de limpeza pós teste, para não ficar apagando manualmente
shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)  # Exclui a pasta dentro do arquivo zip
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)  # Exclui a pasta zipada apenas para teste, caso execute mais de uma vez não precise ficar apagando manualmente
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)  # Diretório é criado usando mkdir


def criar_arquivos(qtd: int, zip_dir: Path):  # Então criamos uma função para criar conteúdo para o arquivo zip, passando 2 argumentos a quantidade de arquivos e o caminho
    for i in range(qtd):  # Realiza a iteração on i é o valor que será recebido no argumento quantidade
        texto = 'arquivo_%s' % i  # Variável que armazena o nome do arquivo usando um marcador de posição que artera o valor a cada iteração
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:  # Então abrimos o caminho passado como argumento para a função concatenado com o nome do arquivo em modo de escrita, ou seja a cada iteração um arquivo novo é criado dentro da pasta zip até que tenha o total de arquivos referente a quantidade passada como argumento
            arquivo.write(texto)  # Então escrevemos o conteúdo da variável texto dentro de cada arquivo


criar_arquivos(10, CAMINHO_ZIP_DIR)  # Execução da função com o 10 sendo a quantidade e o segundo argumento o caminho para a criação dos arquivos

# Criando arquivos zip
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:  # Com a classe ZipFile, passamos o caminho compactado com final .zip em modo de escrita = 'w'
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):  # E percorremos todo o caminho da pasta passada no parâmetro da função walk
        for file in files:  # Iteração nos arquivos do caminho passado na função walk
            zip.write(os.path.join(root, file), file)  # Escreve cada arquivo para dentro da pasta zipada

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:  # Para ler usamos a mesma estrutura acima porém em modo de leitura = r
    for arquivo in zip.namelist():  # Itera sobre o arquivo compactado e usando a função namelist recebemos os nomes dos arquivos
        print(arquivo)  # Exibe o resultado

# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)  # Para extrair o conteúdo é só usar a função extractall com o cmainho passado como argumento
