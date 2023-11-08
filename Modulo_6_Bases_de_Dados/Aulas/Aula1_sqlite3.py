import sqlite3  # Importa o SQLITE3, ele já vem instalado junto no pacote do Python
from pathlib import Path

from django.db import connection

ROOT_DIR = Path(__file__).parent  # Caminho raíz onde ficara a base de dados
DB_NAME = 'db.sqlite3'  # Nome da base de dados
DB_FILE = ROOT_DIR / DB_NAME  # O arquivo em si

con = sqlite3.connect(DB_FILE)  # Conecta ao arquivo passado no parâmetro, no caso é passado o caminho criado acima
cursor = connection.cursor()  # Cria um objeto de cursor, que é um apontador que permite executar comandos SQL

cursor.close()  # Fecha o cursor
con.close()  # Fecha a conexão com o banco
