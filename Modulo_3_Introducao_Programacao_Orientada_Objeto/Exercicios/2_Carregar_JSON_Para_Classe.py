"""
Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON
e depois crie novamente as instâncias
da classe com os dados salvos
Faça em arquivos separados.
"""
import json
class Carro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

with open('Modulo_3_Introducao_Programacao_Orientada_Objeto\\Exercicios\\Exercicio_JSON\\classe.json', 'r', encoding='utf-8') as file:
    arquivo = json.load(file)
    p1 = Carro(**arquivo[0])
    p2 = Carro(**arquivo[1])
    p3 = Carro(**arquivo[2])  

print(p1.nome)
print(p2.nome)
print(p3.nome)
