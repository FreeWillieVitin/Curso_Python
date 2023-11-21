import sqlite3  # Importa o SQLITE3, ele já vem instalado junto no pacote do Python
from Aula1_sqlite3 import DB_FILE, TABLE_NAME  # Importa o caminho do banco de dados do módulo anterior

con = sqlite3.connect(DB_FILE)  # Conecta ao arquivo passado no parâmetro
cursor = con.cursor()  # Cria um objeto de cursor, que é um apontador que permite executar comandos SQL

cursor.execute(f'select * from {TABLE_NAME}')  # Query de seleção na base de dados

row = cursor.fetchone()  # fetchone armazena apenas o primeiro registro encontra pela query
print(row)  # Exibe o registro armazenado
print()

row = cursor.fetchmany(2)  # fetchmany armazena a quantidade de registros de forma ordenada que foi passado como parâmetro
print(row)  # Exibe os registros armazenados
print()

for row in cursor.fetchall():  # O fetchall armazena todos os registro buscados pela query
    _id, nome, peso = row  # Podemos iterar pelas colunas da tabela para exibir os dados
    print(_id, nome, peso)  # Exibe os registros armazenados

cursor.close()  # Fecha o cursor
con.close()  # Fecha a conexão com o banco
