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

----------------------------------------------------------------------------------------------------------------------------------
|                                           Padrão C para formatar datas e horários                                              |
----------------------------------------------------------------------------------------------------------------------------------

%a - Dias da semana como nomes abreviados da localidade.
-------------------------
Ex:                      |
Sun, Mon, …, Sat (en_US);|
So, Mo, …, Sa (de_DE)    |
-------------------------
Notas = (1)

----------------------------------------------------------------------------------------------------------------------------------

%A - Dia da semana como nome completo da localidade.
------------------------------------
Ex:                                 |
Sunday, Monday, …, Saturday (en_US);|
Sonntag, Montag, …, Samstag (de_DE) |
------------------------------------
Notas = (1)

----------------------------------------------------------------------------------------------------------------------------------

%w - Dia da semana como um número decimal, onde 0 é domingo e 6 é sábado.
----------
Ex:       |
0, 1, …, 6|
----------

----------------------------------------------------------------------------------------------------------------------------------

%d - Dia do mês como um número decimal com zeros a esquerda.
-------------
Ex:          |
01, 02, …, 31|
-------------
Notas = (9)

----------------------------------------------------------------------------------------------------------------------------------

%b - Mês como nome da localidade abreviado.
-------------------------
Ex:                      |
Jan, Feb, …, Dec (en_US);|
Jan, Feb, …, Dez (de_DE) |
-------------------------
Notas = (1)

----------------------------------------------------------------------------------------------------------------------------------

%B - Mês como nome completo da localidade.
---------------------------------------
Ex:                                    |
January, February, …, December (en_US);|
janeiro, fevereiro, …, dezembro (pt_BR)|
---------------------------------------
Notas = (1)

----------------------------------------------------------------------------------------------------------------------------------

%m - Mês como um número decimal com zeros a esquerda.
-------------
Ex:          |
01, 02, …, 12|
-------------
Notas = (9)

----------------------------------------------------------------------------------------------------------------------------------

%y - Ano sem século como um número decimal com zeros a esquerda.
-------------
Ex:          |
00, 01, …, 99|
-------------
Notas = (9)

----------------------------------------------------------------------------------------------------------------------------------

%Y - Ano com século como um número decimal.
----------------------------------------
Ex:                                     |
0001, 0002, …, 2013, 2014, …, 9998, 9999|
----------------------------------------
Notas = (2)

----------------------------------------------------------------------------------------------------------------------------------

%H - Hora (relógio de 24 horas) como um número decimal com zeros a esquerda.
-------------
Ex:          |
00, 01, …, 23|
-------------
Notas = (9)

----------------------------------------------------------------------------------------------------------------------------------

%I - Hora (relógio de 12 horas) como um número decimal com zeros a esquerda.
-------------
Ex:          |
01, 02, …, 12|
-------------
Notas = (9)

----------------------------------------------------------------------------------------------------------------------------------

%p - Equivalente da localidade a AM ou PM.
---------------
Ex:            |
AM, PM (en_US);|
am, pm (de_DE) |
---------------
Notas = (1), (3)

----------------------------------------------------------------------------------------------------------------------------------

%M - Minutos como um número decimal, com zeros a esquerda.
-------------
Ex:          |
00, 01, …, 59|
-------------
Notas = (9)

----------------------------------------------------------------------------------------------------------------------------------

%S = Segundos como um número decimal, com zeros a esquerda.
-------------
Ex:          |
00, 01, …, 59|
-------------
Notas = (4), (9)

----------------------------------------------------------------------------------------------------------------------------------

%f - Microssegundos como um número decimal, com zeros à esquerda até completar 6 dígitos.
-------------------------
Ex:                      |
000000, 000001, …, 999999|
-------------------------
Notas = (5)

----------------------------------------------------------------------------------------------------------------------------------

%z - Diferença UTC no formato ±HHMM[SS[.ffffff]] (string vazia se o objeto é ingênuo).
-----------------------------------------------------
Ex:                                                  |
(vazio), +0000, -0400, +1030, +063415, -030712.345216|
-----------------------------------------------------
Notas = (6)

----------------------------------------------------------------------------------------------------------------------------------

%Z - Nome do fuso horário (string vazia se o objeto é ingênuo).
-----------------
Ex:              |
(vazio), UTC, GMT|
-----------------
Notas = (6)

----------------------------------------------------------------------------------------------------------------------------------

%j - Dia do ano como um número decimal, com zeros a esquerda.
----------------
Ex:             |
001, 002, …, 366|
----------------
Notas = (9)

----------------------------------------------------------------------------------------------------------------------------------

%U - Número da semana do ano (Domingo como o primeiro dia da semana) como um número decimal, com zeros a esquerda.
Todos os dias em um ano novo precedendo o primeiro domingo são considerados como estando na semana 0.
-------------
Ex:          |
00, 01, …, 53|
-------------
Notas = (7), (9)

----------------------------------------------------------------------------------------------------------------------------------

%W - Número da semana do ano (Segunda-feira como o primeiro dia da semana) como um número decimal, com zeros a esquerda.
Todos os dias em um ano novo precedendo a primeira segunda-feira são considerados como estando na semana 0.
-------------
Ex:          |
00, 01, …, 53|
-------------
Notas = (7), (9)

----------------------------------------------------------------------------------------------------------------------------------

%c - Representação de data e hora apropriada da localidade.
---------------------------------
Ex:                              |
Tue Aug 16 21:30:00 1988 (en_US);|
Di 16 Aug 21:30:00 1988 (de_DE)  |
---------------------------------
Notas = (1)

----------------------------------------------------------------------------------------------------------------------------------

%x - Representação de data apropriada de localidade.
-------------------
Ex:                |
08/16/88 (None);   |
08/16/1988 (en_US);|
16.08.1988 (de_DE) |
-------------------
Notas = (1)

----------------------------------------------------------------------------------------------------------------------------------

%X - Representação de hora apropriada da localidade.
-----------------
Ex:              |
21:30:00 (en_US);|
21:30:00 (de_DE) |
-----------------
Notas = (1)

----------------------------------------------------------------------------------------------------------------------------------

%% - Um caractere literal '%'.
---
Ex:|
%  |
---

----------------------------------------------------------------------------------------------------------------------------------

%G - Ano ISO 8601 com o século representando o ano que a maior parte da semana ISO (%V).
----------------------------------------
Ex:                                     |
0001, 0002, …, 2013, 2014, …, 9998, 9999|
----------------------------------------
Notas = (8)

----------------------------------------------------------------------------------------------------------------------------------

%u - Dia de semana ISO 8601 como um número decimal onde 1 é segunda-feira.
----------
Ex:       |
1, 2, …, 7|
----------

----------------------------------------------------------------------------------------------------------------------------------

%V - Semana ISO 8601 como um número decimal, com segunda-feira como o primeiro dia da semana.
A semana 01 é a semana contendo o dia 4 de Janeiro.
-------------
Ex:          |
01, 02, …, 53|
-------------
Notas = (8), (9)

"""
from datetime import datetime  # Para trabalhar com datas e horários usamos o módulo do python chamado datetime
from pytz import timezone  # Uma das funções existentes na biblioteca é a timezone, que basicamente serve para definir a timezone
# que será usada em seu código

data_str = '2022-04-12 07:49:23'  # Aqui temos uma variável que recebe uma data e um horário, escrita de forma manual
data_fmt = '%Y-%m-%d %H:%M:%S'  # Nesta variável temos o formato a ser exibido, seguindo o padrão C, mostrado no descritivo acima

data = datetime(2022, 4, 12, 12, 46, 23, tzinfo=timezone('Asia/Tokyo'))  # Podemos usar o datetime para passar a data e a hora como parâmetro na seguinte ordem: (Ano, Mês, Dia, Hora, Minuto, Segundo, Microsegundo) e usando a função timezone podemos definir de qual localidade será exibido o timezone
data2 = datetime.strptime(data_str, data_fmt) # Com a classe datetime podemos usar o método strptime para passar uma variável de datetime e como segundo atributo, uma variável de formato de data
data3 = datetime.now(timezone('America/Sao_Paulo')) # O método now, exibe a data e horário atual, seguindo a timezone passada
data4 = datetime.now(timezone('Asia/Tokyo'))
data5 = datetime.now() # E usando o método now sozinho exibe apenas a data atual seguindo a timezone padrão do computador
data6 = datetime.fromtimestamp(80000) # A função fromtimestamp converte um valor numérico que faz referência a alguma data/hora para um valor datetime, esse valor númerico representa os segundo e segue o padrão UNIX e POSIX, ou seja passa a valer os segudnos apartir da data 01/01/1970 ás 00:00:00 e cada numéro passado como parâmentro representa uma adição a essa data

print(data)
print(data2)
print(data3)
print(data4)
print(data5.timestamp()) # Exibe o valor em forma timestamp da data/hora atual, ou seja cada segundo e milisegundo apartir da data/hora padrão UNIX 01/01/1970 ás 00:00:00
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

fmt = '%d/%m/%Y %H:%M:%S' # Variável que recebe um formato para data/hora
data_inicio = datetime.strptime('15/05/1986 08:05:12', fmt) # Variável que recebe o método strptime da classe datetime, nela é passado como paramêtro um horario e como ele deve ser formatado, no caso usando a variável acima
data_fim = datetime.strptime('23/11/2003 12:45:23', fmt)
calc_data = data_fim - data_inicio # Calculo sobre duas data, subtração entre a data da variável data_fim, com a data da variável data_inicio
delta = data_fim - data_inicio
delta1 = timedelta(days=10, hours=10) # Usando a classe timedelta, podemos passar argumentos que serão calculados a datas previamente especificadas
delta2 = relativedelta(data_fim, data_inicio) # A Classe relativedelta é basicamente a timedelta melhorada, pois além de trabalhar com dias, ela pode realizar calculos com meses, anos, semanas ou seja, medidas de tempo mais granulares

print(calc_data)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds()) # Exibe a quantidade de segundos total de um valor datetime
print(data_fim + delta1)
print(data_fim + relativedelta(days=5, months=3, seconds=59, minutes=70)) # Neste caso estamos adicionando mais 3 meses além da data_fim, o relativedelta trabalha com mais precisão e flexibilidade
print(data_fim)
print(delta2) # E se executar apenas a variável em que o relativedelta está com seus argumentos de data, será retornado o intervalo entre uma data e outra
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
