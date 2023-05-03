"""
Criando arquivos com Python + Context Manager with
Usamos a função open para abrir
um arquivo em Python (ele pode ou não existir)
Modos:
r (leitura), w (escrita), x (para criação)
a (escreve ao final), b (binário)
t (modo texto), + (leitura e escrita)
Context manager - with (abre e fecha)
Métodos úteis
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)
Vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo
Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json
json.load
"""
# Se não especificar o caminho, o arquivo vai ser criado na pasta em que o módulo está
caminho = 'arquivo_da_aula_30_modulo_2.txt'

# O arquivo vai ser criado na pasta especificada, no windows para usar a barra invertida é necessario que seja colocada duas seguidas uma da outra
# Pois o python identifica uma unica barra invertida como caracter de escape
caminho_arquivo = 'C:\\Users\\HSVP\\Documents\\GitHub\\Curso_Python\\Modulo_2_Python_Intermediario\\Aula\\Pacote_teste\\'
caminho_arquivo += 'arquivo_da_aula_30_modulo_2.txt'
caminho_arquivo2 = 'C:\\Users\\HSVP\\Documents\\GitHub\\Curso_Python\\Modulo_2_Python_Intermediario\\Aula\\Pacote_teste\\arquivo_da_aula_30_modulo_2(2).txt'


nome = ['Victor', 'Marieli']

# Para a criação de um arquivo precisamos usar a função open e como parametro, o caminho do arquivo inteiro ou em forma de variável, e o modo do arquivo
# Na criação do arquivo precisamos q ele esteja sempre em modo de escrita (w, a, +, r+, w+, x)
arquivo = open(caminho_arquivo, 'w')
arquivo.close() # Sempre que abrir um arquivo, é obrigatorio que ele seja fechado

# Context manager - with - Usando o with open o arquivo é criado, aberto e fechado automaticamente sem precisar do close, sua sintaxe é praticamente a mesma
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha 1')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 2\n')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

print('#' * 40)

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', *nome)
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline())

with open(caminho_arquivo2, 'a') as arquivo:
    arquivo.write('Linha 1')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Atenção\n')

# with open(caminho_arquivo, 'b') as arquivo:
