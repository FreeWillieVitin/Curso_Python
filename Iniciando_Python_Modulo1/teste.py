while True:
    sair = input('Deseja continuar a calcular? \n'
    '(S - Sim N - Não): ').upper()
    while sair not in 'SN':
        print('tá')
    if sair == 'N':
        break
        
        