"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
cpf = input('Digite o seu CPF: ').replace('.', '').replace('-', '')
conta = 10
conta2 = 10
soma = 0
soma2 = 0
result = 0
verificador = []
check = cpf[0]
v_repeat = int(cpf == check * len(cpf))

if v_repeat:
    print(f'{cpf} é um valor irregular')
    exit()
else: 
    pass

for i in range(0, len(cpf)-2):
    soma += (int(cpf[i]) * conta)
    i += 1
    conta -= 1
result = (soma * 10) % 11
if result > 9:
    verificador.append(0)
elif result <= 9:
    verificador.append(result)

for i in range(0, len(cpf)-1):
    soma2 += (int(cpf[i]) * conta2)
    i += 1
    conta2 -= 1
result = (soma2 * 10) % 11
if result > 9:
    verificador.append(0)
elif result <= 9:
    verificador.append(result)

print(verificador)

