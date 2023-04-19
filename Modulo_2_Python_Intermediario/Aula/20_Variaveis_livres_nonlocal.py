# Variáveis livres + nonlocal
def fora():
    a = 1

    def dentro():
        return a
    return dentro

