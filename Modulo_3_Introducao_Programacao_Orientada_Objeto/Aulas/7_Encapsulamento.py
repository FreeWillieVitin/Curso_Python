"""
Encapsulamento (modificadores de acesso: public, protected, private)
Python NÃO TEM modificadores de acesso
Mas podemos seguir as seguintes convenções
  (sem underline) = public
      pode ser usado em qualquer lugar
_ (um underline) = protected
      não DEVE ser usado fora da classe
      ou suas subclasses.
__ (dois underlines) = private
      "name mangling" (desfiguração de nomes) em Python
      _NomeClasse__nome_attr_ou_method
      só DEVE ser usado na classe em que foi
      declarado.
"""
class Foo:
    def __init__(self):
        self.public = 'Isso é público' # Atributo publico, pode ser acessado de qualquer lugar do sistema
        self._protected = 'Isso é protegido' # Atributo protegido, só pode ser acessado de dentro da classe ou de suas subclasses, isso é uma conveção, o sistema permite acessar de outra parte do sistema, mas não é o correto 
        self.__private = 'Isso é private' # Atributo private, somente deve ser usado dentro da classe e mais de lugar nenhum

        self._metodo_protected()

    def metodo_publico(self):
        self._metodo_protected()
        print(self.__private)
        self.__metodo_private()
        return 'Método_publico'
    
    def _metodo_protected(self):
        print('_Método_protected')
        return '_Método_protected'
    
    def __metodo_private(self):
        print('__Método_private')
        return '__Método_private'



f = Foo()
print(f.public)
print(f.metodo_publico())
print(f._protected) # Forma errada de acessa um instancia com atributo protected
print(f._metodo_protected()) # Forma errada de acessa um instancia com um método protected
print(f._Foo__metodo_private())
