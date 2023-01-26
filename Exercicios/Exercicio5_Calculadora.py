"""
Calculadora com while
"""
while True:
    val_1 = input('Digite um número: ')
    val_2 = input('Digite um número: ')
  

    op = input('Digite um dos operadores(+ - * /): ')

    if val_1.isnumeric():
        val_1 = float(val_1)
    else:
        print(f"{val_1} Não é um número inteiro")
        exit()

    if val_2.isnumeric():
        val_2 = float(val_2)
    else:
        print(f"{val_2} Não é um número inteiro")
        exit()

    if op not in '+-*/':
        print('Operador inválido')
        continue
        
    if op == '+':
        print(val_1 + val_2)
    elif op == '-':
        print(val_1 - val_2)   
    elif op == '*':
        print(val_1 * val_2)     
    elif op == '/':
        print(val_1 / val_2)
    else:
        print('erro')
        exit()
    
    sair = input('Deseja continuar a calcular? \n'
    '(S - Sim N - Não): ').upper()
    while sair not in 'SN':
        print('Opção não reconhecida.')
    if sair == 'N':
        print('Tchau')
        break







        


