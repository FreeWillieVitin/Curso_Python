"""
Exercício - Lista de tarefas com desfazer e refazer
Música para codar =)
Everybody wants to rule the world - Tears for fears
todo = [] -> lista de tarefas
todo = ['fazer café'] -> Adicionar fazer café
todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
desfazer = ['fazer café',] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']
"""
import json
tarefas = []
tarefas_refazer = []

def listar_tarefa(lista):
    print('TAREFAS:')
    print()
    if not lista:
        print('Nenhuma tarefa para listar')
        print()
    for i in lista:
        print(f'\t{i}')

def adiciona_tarefa(tarefa, lista):
    lista = tarefas
    lista.append(tarefa)
    return lista

def desfazer_tarefas(tarefa, tarefa_refazer):
    print()
    if not tarefa:
        print('Nenhuma tarefa para desfazer')
        print()
        return

    lista1 = tarefa.pop()
    print(f'{lista1=} removida da lista de tarefas.')
    tarefa_refazer.append(lista1)
    print()

def salvar_tarefas(lista):
    with open('Modulo_2_Python_Intermediario\\Exercicios\\Lista-Afazeres.json', 'w+') as file:
        json.dump(lista, file, indent=2)

def carregar_tarefas(lista):
    with open('Modulo_2_Python_Intermediario\\Exercicios\\Lista-Afazeres.json', 'r', encoding='utf-8') as file:
        arquivo = json.load(file)
        for a in arquivo:
            lista.append(a)
        return lista
        
def refazer_tarefas(tarefa, tarefa_refazer):
    print()
    if not tarefa_refazer:
        print('Nenhuma tarefa para desfazer')
        print()
        return

    lista2 = tarefa_refazer.pop()
    print(f'{lista2=} removida da lista de tarefas.')
    tarefa.append(lista2)
    print()

while True:
    print('Comandos: [L]istar, [D]esfazer, [R]efazer, [S]alvar, [C]arregar, [E]xit')
    opcoes = input('Adicione um afazer ou um comando: ').upper()

    if opcoes == 'L':
        listar_tarefa(tarefas)

    elif opcoes == 'D':
        desfazer_tarefas(tarefas, tarefas_refazer)

    elif opcoes == 'R':
        refazer_tarefas(tarefas, tarefas_refazer)

    elif opcoes == 'S':
        salvar_tarefas(tarefas)

    elif opcoes == 'C':
        carregar_tarefas(tarefas)

    elif opcoes == 'E':
        print('Fechando lista de afazeres')
        break

    else:
        tarefas.append(opcoes)

# Solução do professor
# import os


# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

# comandos = {
#     'listar': lambda: listar(tarefas),
#     'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
#     'refazer': lambda: refazer(tarefas, tarefas_refazer),
#     'clear': lambda: os.system('clear'),
#     'adicionar': lambda: adicionar(tarefa, tarefas),
# }
# comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
#     comandos['adicionar']
# comando()

