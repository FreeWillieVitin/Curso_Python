"""
sys.argv - Executando arquivos com argumentos no sistema
Fonte = Fira Code (Outro tipo de fonte, sem vinculo com a aula)
"""
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

print(argumentos)
print(qtd_argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com o argumento {argumentos[1]}')
        print(f'Faça alguma coisa com o argumento {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')
print()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
argparse.ArgumentParser para argumentos mais complexos
Tutorial Oficial:
https://docs.python.org/pt-br/3/howto/argparse.html
"""
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-b', '--basic',
                    help='Mostra "Olá Mundo" na tela',
                    # type=str, # Tipo do argumento
                    metavar='STRING',
                    # default='Olá Mundo', # Valor padrão
                    # required=True
                    # nargs='+' # Recebe mais de um valor
                    action='append' # Recebe o argumento mais de uma vez, salvos em uma lista
)

parser.add_argument('-v', '--verbose',
                    help='Mostrar logs',
                    action='store_true'
)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de B')
    print(args.basic)
else:
    print(args.basic)

print(args.verbose)