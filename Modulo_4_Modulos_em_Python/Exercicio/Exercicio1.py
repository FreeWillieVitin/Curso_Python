"""
Exercício solucionado: calculando as datas e parcelas de um empréstimo
Maria pegou um empréstimo de 1.000.000
para realizar o pagamento em 5 anos.
A data em que ela pegou o empréstimo foi
20/12/2020 e o vencimento de cada parcela
é no dia 20 de cada mês.
- Crie a data do empréstimo
- Crie a data do final do empréstimo
- Mostre todas as datas de vencimento e o valor de cada parcela
"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone

emprestimo = 1_000_000  # Define o valor do empréstimo
data_emprestimo = datetime(2020, 12, 20)  # Armazena em uma variável a data em que o empréstimo foi realizado
delta1 = relativedelta(years=5)  # E um relativedelta de 5 anos que será o tempo total para pagamento das parcelas
data_final = data_emprestimo + delta1  # A data final será a data inicial mais o relativedelta de 5 anos

parcelas = []  # uma lista que vai receber as parcelas
data_parcela = data_emprestimo
while data_parcela < data_final:
    parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

num_parcelas = len(parcelas)
valor_parcela = emprestimo / num_parcelas

for data in parcelas:
    print(f'{data}, {valor_parcela:,.2f}')

print()
print(f'Você emprestou {emprestimo:,.2f} para pagar em {delta1.years} anos, são {num_parcelas} parcelas de {valor_parcela:,.2f}')
