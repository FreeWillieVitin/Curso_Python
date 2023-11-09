"""
    Ambientes virtuais em Python (venv)
    Um ambiente virtual carrega toda a sua instalação
    do Python para uma pasta no caminho escolhido.
    Ao ativar um ambiente virtual, a instalação do
    ambiente virtual será usada.
    venv é o módulo que vamos usar para
    criar ambientes virtuais.
    Você pode dar o nome que preferir para um
    ambiente virtual, mas os mais comuns são:
    venv env .venv .env
"""

# python -m venv venv - esse é o comando no powersheel para criação de um
# ambiente virtual (O nome da venv é o segundo, pode ser qualquer nome)
# gcm python - Localiza o caminho de instalação do python ou de qualquer
# arquivo que for passado após o gcm
# gcm python -Syntax - Mostra apenas o caminho, não traz outras informações
# No linux ou IOS o comando a cima é executado por which python
# Esse é o caminho do python global no computador do meu trabalho
# C:\Users\HSVP\AppData\Local\Programs\Python\Python311\python.exe

"""
Como Ativar o ambiente virtual no windows
"""
# NomeDoAmbienteVirtual\Scripts\activate
# Executar a venv ao iniciar o VS-CODE = SetExecutionPolicy Unrestricted -Force
"""
Como Ativar o ambiente virtual no Linux
Qlquer um dos modos abaixo executa
"""
# . NomeDoAmbienteVirtual/bin/activate
# source NomeDoAmbienteVirtual/bin/activate

"""
Instalar ou desinstalar pacotes e bibliotecas
"""
# Para instalar pacotes que não vem com o python,
# usamos o comando pip install NomeDoPacoteOuBiblioteca
# E o pip uninstall NomeDoPacoteOuBiblioteca para desinstalar

"""
Listar pacotes instalados
"""
# pip freeze - Exibe todos os pacotes instalados, o pip freeze também é
# utlizado para criar um arquivo requirements.txt,
# Esse requirements.txt serve como um instalador de pacotes padrão, quando for
# criado uma venv nova para nao ter que ficar instalando pacote por pacote
# Executamos o requirements e tudo o que estiver
# especificado nele será instalado
# Comando para criar o requirements.txt - pip freeze > NomeDoArquivo.txt
# E para instalar os pacotes e bibliotecas do
# requirements - pip install -r NomeDoArquivo.txt
