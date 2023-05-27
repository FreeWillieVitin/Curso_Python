"""
Teoria: python Special Methods, Magic Methods ou Dunder Methods
Dunder = Double Underscore = __dunder__
Antigo e útil: https://rszalski.github.io/magicmethods/
https://docs.python.org/3/reference/datamodel.html#specialnames
__lt__(self,other) - self < other
__le__(self,other) - self <= other
__gt__(self,other) - self > other
__ge__(self,other) - self >= other
__eq__(self,other) - self == other
__ne__(self,other) - self != other
__add__(self,other) - self + other
__sub__(self,other) - self - other
__mul__(self,other) - self * other
__truediv__(self,other) - self / other
__neg__(self) - -self
__str__(self) - str
__repr__(self) - str
"""
class Ponto:
    def __init__(self, x, y, z='String') -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        class_name1 = type(self).__name__
        return f'{class_name1} (x={self.x}, y={self.y}, z={self.z})'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other
    
if __name__ == '__main__':
    r1 = Ponto(4, 6) 
    r2 = Ponto(8, 9)
    r3 = r1 + r2
    print(r3)
    print('R1 é maior que R2', r1 > r2)
    print('R2 é maior que R1', r2 > r1)

p1 = Ponto(1, 2)
p2 = Ponto(987, 876)
print()
print(p1)
print(repr(p2))
print(f'{p2!r}')
print()

# -------------------------------------------------------------------------------------------------------------------------------------------
"""
# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
"""
class A:
    def __new__(cls, *args, **kwargs):
        print('Antes de criar')
        instancia = super().__new__(cls)
        print('Depois')
        instancia.r = 213
        return instancia

    def __init__(self, x) -> None:
        self.x = x
        print('Sou o Init')

    def __repr__(self) -> str:
        return 'A()'

# a = object.__new__(A)
# a.__init__()
a = A(123)
print(a)
print(a.r)
print(a.x)

