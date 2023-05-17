"""
__dict__ e vars para atributos de instância
(Usando o mesmo exemplo da aula anterior)
"""
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self): 
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Victor', 25)
print(p1.__dict__)
print(vars(p1))
p1.__dict__['outra'] = 'coisa'
p1.__dict__['nome'] = 'EITA'
print(p1.__dict__)
print(vars(p1))
print(p1.outra)
print(p1.nome)
