"""
Positional-Only Parameters (/) e Keyword-Only Arguments (*)
*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)
🟢 Positional-only Parameters (/) - Tudo antes da barra deve
ser ❗️APENAS❗️ posicional.
PEP 570 – Python Positional-Only Parameters
https://peps.python.org/pep-0570/
🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
PEP 3102 – Keyword-Only Arguments
https://peps.python.org/pep-3102/
"""
def soma(x, y, /, a, b, *, c):# Tudo o que vier antes da barra não pode ser nomeado e tudo o que vier após o asterisco deve ser nomeado
    print(x + y + a + b)


# soma(1, y=2, b=1, a=3)
soma(1, 2, b=1, a=3, c='5')
soma(1, 2, 1, 3, c=5)
