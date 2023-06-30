from pathlib import Path

caminho_projeto = Path()

print(caminho_projeto.absolute())
print()

caminho_arquivo = Path(__file__)
print(caminho_arquivo)
print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)
print()

ideias = caminho_arquivo.parent / 'ideias'
print(ideias)
print()

print(Path.home() / 'Desktop' / 'abcd.txt')
print()

cria_arquivo = Path.home() / 'Desktop' / 'abcd.txt'
cria_arquivo.touch()
print(cria_arquivo)
cria_arquivo.write_text('Olá Mundo\n')
print(cria_arquivo.read_text())
# cria_arquivo.unlink()
print()

caminho_arquivo2 = Path.home() / 'Desktop' / 'abcd.txt'

with caminho_arquivo2.open('a+') as arquivo:
    arquivo.write('Uma Linha\n')
    arquivo.write('Duas Linhas\n')

print(caminho_arquivo2.read_text())
print()

caminho_pasta = Path.home() / 'Desktop' / 'Pasta PathLib'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'SubPasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Oi Mundo')

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch() # Atualiza a ultima modificação do arquivo, mas por consequência cria o arquivo também

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