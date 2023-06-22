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

formata_data = '%d/%m/%Y'
emprestimo = 1_000_000
data_emprestimo = datetime(2020,12,20)
delta1 = relativedelta(years=5)
data_final = data_emprestimo + delta1

data_parcela = data_emprestimo
while data_parcela < data_final:
    data1 = data_parcela + relativedelta(months=+1)
    print(data1)


    




    





