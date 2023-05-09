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
tarefas = []
tarefas_refazer = []

def adiciona_tarefa(tarefa, lista):
    lista = tarefas
    lista.append(tarefa)
    return lista

def desfaz_tarefa(lista1):
    ultimo = tarefas.pop()    
    lista1.append(ultimo)
    return lista1

