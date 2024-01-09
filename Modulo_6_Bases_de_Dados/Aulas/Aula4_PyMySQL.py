"""
PyMySQL - um cliente MySQL feito em Python Puro
Doc: https://pymysql.readthedocs.io/en/latest/
Pypy: https://pypi.org/project/pymysql/
GitHub: https://github.com/PyMySQL/PyMySQL
"""
from tkinter import INSERT
import pymysql
import pymysql.cursors

from typing import cast

# import dotenv

# dotenv.load_dotenv()

NOME_TABELA = 'USUARIO'
CURSOR_ATUAL = pymysql.cursors.DictCursor

connection = pymysql.connect(
    host='localhost',
    port=6612,
    user='usuario',
    password='senha',
    database='base_de_dados',
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        # SQL VAI AQUI
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS USUARIO ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome varchar(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        cursor.execute(f'TRUNCATE TABLE {NOME_TABELA}')
        print(cursor)
    connection.commit()
    print()

    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        resultado = cursor.execute(
            f'INSERT INTO {NOME_TABELA} '
            '(nome, idade) VALUES ("Victor", 25) '
        )
        print(resultado)
    connection.commit()
    print()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {NOME_TABELA} '
            '(nome, idade) VALUES (%s, %s) '
        )
        dados = ('Marieli', 24)
        executa = cursor.execute(sql, dados)  # type: ignore
        print(sql, dados)
        print(executa)
    connection.commit()
    print()

    # Inserindo vários valores usando placeholder e um tupla de dicionários
    with connection.cursor() as cursor:
        sql2 = (
            f'INSERT INTO {NOME_TABELA} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(age)s) '
        )
        dados2 = {
            "nome": "Judite",
            "age": 72,
        }
        executa2 = cursor.execute(sql2, dados2)  # type: ignore
        print(sql2)
        print(dados2)
        print(executa2)
    connection.commit()
    print()

    # Inserindo vários valores usando placeholder e um tupla de tuplas
    with connection.cursor() as cursor:
        sql3 = (
            f'INSERT INTO {NOME_TABELA} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(age)s) '
        )
        dados3 = (
            {"nome": "Luiz", "age": 52, },
            {"nome": "Carla", "age": 48, },
            {"nome": "Antonio", "age": 78, },
        )
        executa3 = cursor.executemany(sql3, dados3)  # type: ignore
        print(sql3)
        print(dados3)
        print(executa3)
    connection.commit()
    print()

    with connection.cursor() as cursor:
        sql4 = (
            f'INSERT INTO {NOME_TABELA} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        dados4 = (
            ("Kleber", 12,),
            ("FreeWillie", 25,),
        )
        executa4 = cursor.executemany(sql4, dados4)  # type: ignore
        print(sql4)
        print(dados4)
        print(executa4)
    connection.commit()
    print()

    # Lendo os valores com SELECT

    with connection.cursor() as cursor:
        sql5 = (
            f'SELECT id, nome from {NOME_TABELA} '
        )
        cursor.execute(sql5)  # type: ignore

        data5 = cursor.fetchall()

        for row in data5:
            print(row)
    print()

    # Lendo os valores filtrados por where

    # with connection.cursor() as cursor:
    # escolhe_menor = int(input('Digite um id: '))
    # escolhe_maior = int(input('Digite um id: '))
    # sql6 = (
    #     f'SELECT id, nome from {NOME_TABELA} '
    #     'where id between %s and %s'
    # )
    # cursor.execute(sql6, (escolhe_menor, escolhe_maior))  # type: ignore
    # # Exibe a consulta passada para o banco de dados
    # print(cursor.mogrify(sql6, (escolhe_menor, escolhe_maior)))

    # data6 = cursor.fetchall()

    # for row in data6:
    #     print(row)
    # print()

    # Realizando Delete com segurança no PyMySQL

    with connection.cursor() as cursor:
        sql7 = (
            f'DELETE FROM {NOME_TABELA} WHERE id = %s'
        )
        cursor.execute(sql7, (12,))  # type: ignore
        connection.commit()

        cursor.execute(f'select * from {NOME_TABELA}')

        data7 = cursor.fetchall()

        for row in data7:
            print(row)
    print()

    # Realizando Update com segurança no PyMySQL

    with connection.cursor() as cursor:
        sql7 = (
            f'UPDATE {NOME_TABELA} '
            'SET nome = %s, idade= %s '
            'WHERE id = %s'
        )
        cursor.execute(sql7, ('Marcos', 15, 11))  # type: ignore

        result = cursor.execute(f'select * from {NOME_TABELA}')

        data7 = cursor.fetchall()

        sql8 = (
            f'INSERT INTO {NOME_TABELA} '
            '(nome, idade) '
            'values'
            '(%s, %s)')

        data8 = ('Gumercinda', 76)
        cursor.execute(sql8, data8)

        for row in data7:
            print(row)
        print('Valores retornados: ', result)
        print('Valores retornados: ', len(data7))
        print('Valores retornados: ', cursor.rowcount)
        print('Ultimo valor adicionado: ', cursor.lastrowid)
        print('Número da linha atual: ', cursor.rownumber)
        connection.commit()
    print()
