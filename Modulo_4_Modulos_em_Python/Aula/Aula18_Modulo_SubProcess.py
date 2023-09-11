"""
Usando subprocess para executar e comandos externos
subprocess é um módulo do Python para executar
processos e comandos externos no seu programa.
O método mais simples para atingir o objetivo é usando subprocess.run().
Argumentos principais de subprocess.run():
- stdout, stdin e stderr -> Redirecionam saída, entrada e erros
- capture_output -> captura a saída e erro para uso posterior
- text -> Se True, entradas e saídas serão tratadas como texto
e automaticamente codificadas ou decodificadas com o conjunto
de caracteres padrão da plataforma (geralmente UTF-8).
- shell -> Se True, terá acesso ao shell do sistema. Ao usar
shell (True), recomendo enviar o comando e os argumentos juntos.
- executable -> pode ser usado para especificar o caminho
do executável que iniciará o subprocesso.
Retorno:
stdout, stderr, returncode e args
Importante: a codificação de caracteres do Windows pode ser
diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
mac, use utf_8.
Comando de exemplo:
Windows: ping 127.0.0.1
Linux/Mac: ping 127.0.0.1 -c 4
"""
import subprocess
import sys

print(sys.platform)  # Exibe o sistema operacional da máquina

cmd = ['ping', '127.0.0.1']

pingar = subprocess.run(  # Executa a função run do módulo subprocess usando o comando passado na lista acima com o capture = true
    cmd, capture_output=True  # capture_output = true significa que o sistema vai executar em segundo plano e vai apenas retornar
)  # o resulta obtido.

print()
print(pingar.args)  # Retorna os argumentos na lista
print(pingar.stderr)  # Retorna um erro se houver, no caso aqui não tivemos erro nenhum então é retonado b", b = bytes
print(pingar.stdout)  # Exibe o retorno do sistema para aquele comando, todo em bytes pois não foi decodificado
print(pingar.stdout.decode('cp852'))  # O mesmo retorno porém decodificado usando a função decode e o tipo de codificação
print(pingar.returncode)
print()
