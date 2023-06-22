"""
Locale para internacionalização
https://docs.python.org/3/library/locale.html
https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
Get-WinSystemLocale - Ver o locale do sistema operacional
locale -a no linux - Mostra todos as localizações 
"""
import calendar
import locale

locale.setlocale(locale.LC_ALL, '')

print(calendar.calendar(2023))
print(locale.getlocale())