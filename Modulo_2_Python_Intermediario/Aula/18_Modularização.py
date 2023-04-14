# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import Teste_de_Modulo, sys, importlib, Outro_Modulo_Teste
from Teste_de_Modulo import variavel, soma

print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')
print(Teste_de_Modulo.variavel)
print(variavel)
print(soma(8,8))
print(Teste_de_Modulo.soma(5,5))
print(Outro_Modulo_Teste.variavel1)
print()
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for i in range(10):
    importlib.reload(Outro_Modulo_Teste)
    print(i)
print('Fim')