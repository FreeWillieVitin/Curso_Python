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

    def salvar_json(objeto):
        with open('Modulo_3_Introducao_Programacao_Orientada_Objeto\\Exercicios\\Exercicio_JSON\\classe.json', 'w+') as file:
            json.dump(objeto, file, indent=2)

car = Carro('Ford', 'Vermelho')
car2 = Carro('Fiat', 'Preto')
car3 = Carro('Kia', 'Azul')
bd = [vars(car),vars(car2),vars(car3)]

Carro.salvar_json(bd)
