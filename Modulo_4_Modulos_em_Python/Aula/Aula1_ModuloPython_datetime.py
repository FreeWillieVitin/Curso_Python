"""
Criando datas com módulo datetime
datetime(ano, mês, dia)
datetime(ano, mês, dia, horas, minutos, segundos)
datetime.strptime('DATA', 'FORMATO')
datetime.now()
https://pt.wikipedia.org/wiki/Era_Unix
datetime.fromtimestamp(Unix Timestamp)
https://docs.python.org/3/library/datetime.html
Para timezones
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
Instalando o pytz
pip install pytz types-pytz
"""
from datetime import datetime
from pytz import timezone

data_str = '2022-04-12 07:49:23'
data_fmt = '%Y-%m-%d %H:%M:%S'

data = datetime(2022, 4, 12, 12, 46, 23, tzinfo=timezone('Asia/Tokyo'))
data2 = datetime.strptime(data_str, data_fmt)
data3 = datetime.now(timezone('America/Sao_Paulo'))
data4 = datetime.now(timezone('Asia/Tokyo'))
data5 = datetime.now()
data6 = datetime.fromtimestamp(45646)

print(data)
print(data2)
print(data3)
print(data4)
print(data5.timestamp())
print(data6)
print()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
datetime.timedelta e dateutil.relativetimedelta (calculando datas)
Docs:
https://dateutil.readthedocs.io/en/stable/relativedelta.html
https://docs.python.org/3/library/datetime.html#timedelta-objects
"""
from datetime import timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('15/05/1986 08:05:12', fmt)
data_fim = datetime.strptime('23/11/2003 12:45:23', fmt)
calc_data = data_fim - data_inicio
delta = data_fim - data_inicio
delta1 = timedelta(days=10, hours=10)
delta2 = relativedelta(data_fim, data_inicio)

print(calc_data)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(data_fim + delta1)
print(data_fim + relativedelta(seconds=59, minutes=70))
print(data_fim)
print(delta2)
print()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
"""

formata_data = '%d/%m/%Y'
data_para_formatar = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data_para_formatar)
print(data_para_formatar.strftime(fmt))
print(data_para_formatar.strftime('%d/%m/%Y'))
print(data_para_formatar.strftime('%H:%M:%S'))
print(data_para_formatar.strftime('%Y'), data_para_formatar.year)

