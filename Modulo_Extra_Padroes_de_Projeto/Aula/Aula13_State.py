"""
O padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""


class Order:
    # Context
    def __init__(self) -> None:
        self.state: 