"""
Entrada de dados
"""
nome = input('Digite um nome: ')  # Input é a função que permite q seja inserido os dados
idade = input('Digite sua idade: ')

ano_nascimento = 2022 - int(idade)

print(f'Seu nome é {nome} e a usa idade é {idade}.\n'
      f'{nome} você nasceu em {ano_nascimento}.')

numero_1 = int(input('Digite um número: '))  # Casting de um dado string para int
numero_2 = input('Digite outro número: ')
print(numero_1 + int(numero_2))
