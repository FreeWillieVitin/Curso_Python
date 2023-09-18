"""
Usando calendar para calendários e datas
https://docs.python.org/3/library/calendar.html
calendar é usado para coisas genéricas de calendários e datas.
Com calendar, você pode saber coisas como:
- Qual o último dia do mês (ex.: monthrange)
- Qual o nome e número do dia de determinada data (ex.: weekday)
- Criar um calendário em si (ex.: monthcalendar)
- Trabalhar com coisas específicas de calendários (ex.: calendar, month)
Por padrão dia da semana começa em 0 até 6
0 = segunda-feira | 6 = domingo
"""
import calendar # Importa o módulo calendar do python responsável pela manipulação de calendários

print(calendar.calendar(2022)) # Exibe o calendário do ano passado como parâmentro
print()
print(calendar.month(2021, 12)) # Exibe o calendário de um determinado mês de um ano. Parãmetros(ano, mês)
print()
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2023, 2) # É usada para obter informações sobre um mês específico em relação ao calendário. Ela retorna uma tupla contendo dois valores: o número do dia da semana em que o primeiro dia do mês começa e o número total de dias no mês.
print(numero_primeiro_dia) # Indica o indice da semana em que cairá o primeiro dia do mês, seguindo a ordem que 0 = Segunda e 6 = Domingo, no caso desde código, o primeiro dia da semana cai no indice 2 = quarta feira 
print(ultimo_dia) # Exibe a quantidade de dias que tem no mês, ou pode ser chamado de utlimo dia do mês
print(calendar.day_name[numero_primeiro_dia]) # Podemos ver de forma escrita o dia usando a variável day_name
print(calendar.day_name[calendar.weekday(2023, 2, ultimo_dia)]) # E usando a função weekday e passando os parâmetros de ano, mês e dia também vemos de forma escrita o dia, nesse caso o utlimo dia da semana do mês
print()
print(calendar.monthcalendar(2022, 2)) # Se executarmos o monthrange, será retornada uma lista, com várias listas dentro que indicam os dias, o valor 0 representa o dia que não pertence á aquele mês
for week in calendar.monthcalendar(2022, 2):
    for day in week:
        if day == 0:
            continue
        print(day, week) # Podemos também iterar sobre essas informações e ver todos os dias e em qual conjunto de dias da semana ele pertence
print()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
