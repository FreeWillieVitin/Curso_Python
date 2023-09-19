"""
O Python 3 inclui o módulo pathlib para manipular caminhos de sistema de arquivos de maneira independente,
seja qual for o sistema operacional.
Documentação: https://docs.python.org/3/library/pathlib.html
"""
from pathlib import Path

caminho_projeto = Path()  # Variável que recebe a classe Path, essa classe é responsavel por encontrar os diretórios do sistema
# O caminho é passado como argumento da classe, sendo ela vazia o caminho atual do projeto

print(caminho_projeto.absolute())  # Exibe o caminho absoluto, ou seja todos os diretórios até chegar na pasta atual do projeto
print()

caminho_arquivo = Path(__file__)  # Ao passar a variável __file__ no parâmetro, indica o que o Path é o caminho atual do módulo
print(caminho_arquivo)
print(caminho_arquivo.parent)  # parent recua para um diretório o que seria como a pasta pai
print(caminho_arquivo.parent.parent)  # Podemos usar a propriedade parent quantas vezes for necesário até chegar ao ínicio
print()

ideias = caminho_arquivo.parent / 'ideias'  # Podemos acrescentar caminhos ao diretório usando / e o nome, util para criar pastas
print(ideias)
print()

print(Path.home() / 'Desktop' / 'abcd.txt')  # Informa que o path é a home ou seja o caminho inicial do sistema operacional
print()

cria_arquivo = Path.home() / 'Desktop' / 'abcd.txt'  # Variável recebe o caminho da área de trabalho para a criação de um txt
cria_arquivo.touch()  # Cria um arquivo txt no caminho passado na variável
print(cria_arquivo)  # Exibe o caminho da variável
cria_arquivo.write_text('Olá Mundo\n')  # Usando a função write_text, escrevemos o que for passado como parâmetro no arquivo
print(cria_arquivo.read_text())  # Com base no caminho passado para a variável, lemos o seu conteúdo
# cria_arquivo.unlink()  # Unlink exclui o arquivo definitivamente
print()

caminho_arquivo2 = Path.home() / 'Desktop' / 'abcd.txt'  # Variável que recebe o caminho de um arquivo

with caminho_arquivo2.open('a+') as arquivo:  # Usando o variável acima, abrimos o documento em modo append(Modo de inserção)
    arquivo.write('Uma Linha\n')  # Escrevemos no documento uma linha de texto
    arquivo.write('Duas Linhas\n')

print(caminho_arquivo2.read_text())  # Lê o documento
print()

caminho_pasta = Path.home() / 'Desktop' / 'Pasta PathLib'  # Outra variável dessa vez ela será responsável por criar uma pasta
caminho_pasta.mkdir(exist_ok=True)  # Função mkdir cria uma pasta com base na variável passada, se a pasta já existir ignora
subpasta = caminho_pasta / 'SubPasta'  # Dentro da pasta criada acima, criamos uma subpasta
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'  # Variável que recebe o caminho para a criação de um arquivo txt
outro_arquivo.touch()  # Cria o arquivo txt com base na variável
outro_arquivo.write_text('Oi Mundo')  # Escreve no arquivo

files = caminho_pasta / 'files'  # Variável para criação de outra pasta
files.mkdir(exist_ok=True)  # Se a pasta ja existir ignora, caso contrário é criada a pasta 'files'

for i in range(10):  # Iteramos em um range de 0 a 9
    file = files / f'file_{i}.txt'  # Variável recebe o caminho da pasta acima e um nome de arquivo txt que segue a iteração

    if file.exists():  # Checa se existe arquivos no caminho da variável acima
        file.unlink()  # Se existir excluir os arquivos
    else:
        file.touch()  # Atualiza a ultima modificação do arquivo, mas por consequência cria o arquivo também

    with file.open('a+') as text_file:
        text_file.write('Ola mundo\n')
        text_file.write(f'file_{i}.txt')


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('Dir:', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('Dir:', file)
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)
