"""
Enviando e-mails SMTP com python
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
CAMINHO_HTML = pathlib.Path(__file__).parent / 'Aula10_EmailPython.html'

# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = 'tirinho123@gmail.com'

# Configurações (SERVIDOR SMTP)

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with open(CAMINHO_HTML, 'r', encoding='utf8') as arquivo:
    texto_arquivo = arquivo.read()
    template = s.Template(texto_arquivo)
    texto_email = template.substitute(nome='Victor', valor='10000', data='10/07/2023', empresa='Golden Shop', telefone='+55 (47) 3642-2479')

# print(texto_email)

# Transformar mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Assunto do email'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-Mail enviado com sucesso')
