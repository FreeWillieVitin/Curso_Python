"""
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de indices inexistentes na lista
"""
compras = []

while True:
    print('Selecione uma Opção')
    opcoes = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if opcoes == 'i':
        compras.append(input('Digite o produto que voce quer inserir ná lista: '))

    elif opcoes == 'l':
        if compras == []:
            print('Lista de compras vazias')
            continue    
        for i, item in enumerate(compras):
            print(i, item)

    elif opcoes == 'a':
        try:
            compras.pop(int(input('Digite o código do produto a ser excluído: ')))
            print('Produto excluído')
        except:
            print('Produto inexistente')

    elif opcoes == 's':
        break

    else:
        print('Opção inválida')