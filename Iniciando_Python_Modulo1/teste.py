cpf = '11131867980'
conta = 10
soma = 0
result = 0
verificador = []

for i in range(0, len(cpf)-1):
    soma += (int(cpf[i]) * conta)
    i += 1
    conta -= 1
    print(soma)
result = (soma * 10) % 11
print(result)
if result > 9:
    verificador.append(0)
elif result <= 9:
    verificador.append(result)
        