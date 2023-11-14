"""
Documentação SQLite: https://www.sqlite.org/doclist.html
Dicas SQL: https://www.techonthenet.com/sqlite/index.php
"""
import sqlite3  # Importa o SQLITE3, ele já vem instalado junto no pacote do Python
from pathlib import Path

ROOT_DIR = Path(__file__).parent  # Caminho raíz onde ficara a base de dados
DB_NAME = 'db.sqlite3'  # Nome da base de dados
DB_FILE = ROOT_DIR / DB_NAME  # O arquivo em si
TABLE_NAME = 'Customers'

con = sqlite3.connect(DB_FILE)  # Conecta ao arquivo passado no parâmetro, no caso é passado o caminho criado acima
cursor = con.cursor()  # Cria um objeto de cursor, que é um apontador que permite executar comandos SQL

# CUIDADO O COMANDO A SEGUIR È EXTREMAMENTE PERIGOSO
# DELETE SEM WHERE
# cursor.execute(f'delete from {TABLE_NAME}')
# con.commit()

# Criando a tabela
cursor.execute(  # Eis aqui a função de um cursor após ser criado, executando o comando de criar uma tabela no sqlite3
    f'create table if not exists {TABLE_NAME}'  # Se a tabela não existir criar ela com o nome passada na constante
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
con.commit()  # Commit aplica as alterações passada ao cursor no banco de dados

# Registrar valores nas colunas da tabela
cursor.execute(
    f'insert into {TABLE_NAME} (name, weight) '
    'values ("Marieli", 4.6), ("Luiz", 15.8), ("Judite", 7.4)'
)
con.commit()

# cursor.executemany('')

cursor.close()  # Fecha o cursor
con.close()  # Fecha a conexão com o banco
