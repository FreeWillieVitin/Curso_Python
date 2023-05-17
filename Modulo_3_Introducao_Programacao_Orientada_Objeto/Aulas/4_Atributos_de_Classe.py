"""
Atributos de clase
"""
# ANO_ATUAL = 2023

class Pessoa: # Atributos são variáveis que armazenam um valor específico relacionado a classe atual
    ano_atual = 2023 # Aqui teos um exemplo de atributo ano_atual, é quase que um valor que vai ser usado para descrever algo da classe(no caso do exemplo também pode ser usado uma constante)

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self): # Função para calcular idade
        return Pessoa.ano_atual - self.idade # É retornado a idade da pessoa subtraída pelo atributo do ano_atual
    
p1 = Pessoa('Victor', 25) # Então para isso é passado para o objeto apenas a classe e seus argumentos nome e idade, o atributo já foi definido e executado pela função
p2 = Pessoa('Marieli', 24)
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())