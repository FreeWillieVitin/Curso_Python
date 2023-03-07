"""
Closure e funções que retornam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom Dia')
s2 = criar_saudacao('Bom Noite')

for nome in ['Victor', 'Marieli', 'Judite']:
    print(s1(nome))
    print(s2(nome))