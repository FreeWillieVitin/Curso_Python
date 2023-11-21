"""
Documentação SQLite: https://www.sqlite.org/doclist.html
Dicas SQL: https://www.techonthenet.com/sqlite/index.php
CRUD = CREATE  -  READ  - UPDATE - DELETE
SQL -  INSERT  - SELECT - UPDATE - DELETE
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
cursor.execute(f'delete from {TABLE_NAME}')
con.commit()

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
# CUIDADO: sql injection
cursor.execute(
    f'insert into {TABLE_NAME} (name, weight) '  # Insere um registro no banco de dados
    'values ("Marieli", 4.6), ("Luiz", 15.8), ("Judite", 7.4)'
)
con.commit()

insert_date = (  # Variável com o comando de inserção
    f'insert into {TABLE_NAME} (name, weight)'
    'values (?, ?)'  # As ? são chamados de bindings ou placeholders elas servem como um substituto para o python entender
)  # Ali serão passados dados, o :weight também é um placeholder
cursor.execute(insert_date, ['Kleber', 4])  # Usando bindings as informações são passada na hora da execução do cursor
# cursor.execute(insert_date, {weight: 2}) dessa forma usamos um dicionário para inserir dados na tabela
# cursor.executemany(insert_date, (('Kleber', 4), ('Samanta', 8.9)))  # Executemany insere mais de um registro na base de dados
con.commit()

# Reseta o valor sequencial de uma tabela ou seja quandoum dado é excluído o ID é pulado e ficam furos no banco
# O comando abaixo reseta o sequencial voltando a preencher os buracos dos dados excluídos
cursor.execute(
    f'delete from sqlite_sequence where name="{TABLE_NAME}"'
)
con.commit()

cursor.close()  # Fecha o cursor
con.close()  # Fecha a conexão com o banco

if __name__ == '__main__':
    print(insert_date)
