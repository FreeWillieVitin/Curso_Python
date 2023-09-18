"""
Locale para internacionalização
https://docs.python.org/3/library/locale.html
https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
Get-WinSystemLocale - Ver o locale do sistema operacional
locale -a no linux - Mostra todos as localizações
"""
import calendar
import locale

# Seta o local para internacionalização, por exemplo como padrão o python retorna os meses em língua inglesa, se for definido a
# localização para ragião pt_BR, o python automáticamente muda a sua linguagem de localização
locale.setlocale(locale.LC_ALL, '')

print(calendar.calendar(2023))
print(locale.getlocale())  # getlocale() exibe a localização atual
