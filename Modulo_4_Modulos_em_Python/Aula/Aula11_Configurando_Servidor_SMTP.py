"""
Enviando e-mails SMTP com python (SMTP = Protocolo de Transferência de Correio Simples)
"""
import os
from dotenv import load_dotenv
import pathlib
import string as s
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

# Caminho HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'Aula10_EmailPython.html' # Caminho para o arquivo HTML, onde está o corpo do E-Mail que será enviado

# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '') # Variável que recebe o valor referente ao qie foi passado como valor para a respectiva variavel de ambiente no arquivo .env, lembrando que o arquivo não deve ser mostrado junto com o resto do sistema, ou seja deve estar no gitignore
destinatario = 'tirinho123@gmail.com' # Variável que recebe o email de destino

# Configurações (SERVIDOR SMTP), o servido SMTP é o resposavel por apenas enviar o email

smtp_server = 'smtp.gmail.com' # Neste caso do exercício, estamos usando o gmail para enviar os emails, então para isso usamos esse servidor gmail passado na variável
smtp_port = 587 # A porta padrão de um protocolo SMTP é 587, por isso esse número de porta é passado para a variável
smtp_username = os.getenv('FROM_EMAIL', '') # Então passamos o email de remetente para o servidor
smtp_password = os.getenv('EMAIL_PASSWORD', '') # E Enfim a senha, lembrando que todas essas informações devem ficar no arquivo .env, que deve ser configurado com muito cuidado, pois os protocolos de seguraça podem mudar com o passar do tempo

# Mensagem de texto
with open(CAMINHO_HTML, 'r', encoding='utf8') as arquivo: # Como exemplo vamos abrir o arquivo de texto criado no arquivo html, onde o seu corpo foi contruído, em modo de leitura ('r'), e com encoding utf-8 para não ter problemas com acentos ou caracteres especiais
    texto_arquivo = arquivo.read() # O arquivo então é lido
    template = s.Template(texto_arquivo) # E usando o modulo string, armazenamos na variável a classe template para que possa ser passado os valores mutaveis do corpo do email
    texto_email = template.substitute(nome='Victor', valor='10000', data='10/07/2023', empresa='Golden Shop', telefone='+55 (47) 3642-2479') # Usando a função substitute, alteramos as variaveis do corpo do email para o que for passado nos parametros, lembrando que os nomes devem ser os mesmos

# print(texto_email)

# Transformar mensagem em MIMEMultipart
mime_multipart = MIMEMultipart() # Define a variável para usarmos a classe MimeMultiPart, essa classe permite usarmos a extensão mime que é um time de conversor para usarmos tipos de arquivos de dados em emails, como por exemplo audio e video
mime_multipart['from'] = remetente # Usando a variável passamos o remetente e o destinátario, essa classe constroí o email, definindo o assunto
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Assunto do email'

corpo_email = MIMEText(texto_email, 'html', 'utf-8') # E com o MIMEText definimos o conteúdodo e-mail permitindo também o uso de outros tipos de arquivos non-ascii
mime_multipart.attach(corpo_email)

# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-Mail enviado com sucesso')
