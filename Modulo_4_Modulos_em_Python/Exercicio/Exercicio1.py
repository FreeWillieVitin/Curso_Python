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

formato = '%d/%m/%Y'
data_emprestimo = datetime.strptime('20/12/2020', formato)
data_pagamento = datetime.strptime('20/12/2025', formato)
data_emprestimo_fmt = data_emprestimo.strftime('%d/%m/%Y')
data_pag_fmt = data_pagamento.strftime('%d/%m/%Y')

valor_empr = 1000000


