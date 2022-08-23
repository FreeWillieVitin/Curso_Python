"""
For/Else em python
Iterar = passar por cada valor da lista
"""
var = ['victor', 'hugo', 'marieli', 'luiz', 'valdirene']
teste = False
# for i in var:
#     if i.startswith('v'):  # Função startswith checa se os valores da lista começam com a letra parametrizada
#         print(i, 'começa com v')
#     else:
#         print(i, 'não começa com v')
for i in var:
    if i.startswith('v'):
        teste = True

if teste:
    print('Existe uma palavra que começa com V')
else:
    print('Não existe uma palavra que começa com V')