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
os.system('cls')
os.system('echo "Hello World"')


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
'pasta1\pasta2\arquivo.txt' no Windows.
os.path.split: divide um caminho uma tupla (diretório, arquivo).
Por exemplo, os.path.split('/home/user/arquivo.txt')
retornaria ('/home/user', 'arquivo.txt').
os.path.exists: verifica se um caminho especificado existe.
os.path só trabalha com caminhos de arquivos e não faz nenhuma
operação de entrada/saída (I/O) com arquivos em si.
"""
import os

caminho = os.path.join('\\Modulo_4_Modulos_em_Python', 'Aula', 'Aquivo.txt')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao = os.path.splitext(caminho)
print(diretorio)
print(arquivo)
print(caminho_arquivo)
print(extensao)
print()
print(os.path.exists(caminho))
print(os.path.exists('C:\\Users\\Victor\\Documents\\GitHub\\professor\\Curso_Python\\Modulo_4_Modulos_em_Python'))
print()
print(os.path.abspath('.')) # Retorna o caminho absoluto
print(os.path.basename(caminho))
print(os.path.dirname(caminho))
print()
# ----------------------------------------------------------------------------------------------------------------------------------------

"""
os.listdir para navegar em caminhos
/Users/Victor/Desktop/Imagens
"""
