"""
Context Manager com classes - Criando e Usando gerenciadores de contexto
Você pode implementar seus próprios protocolos
apenas implementando os dunder methods que o
Python vai usar.
Isso é chamado de Duck typing. Um conceito
relacionado com tipagem dinâmica onde o Python não
está interessado no tipo, mas se alguns métodos existem
no seu objeto para que ele funcione de forma adequada.
Duck Typing:
Quando vejo um pássaro que caminha como um pato, nada como
um pato e grasna como um pato, eu chamo aquele pássaro de pato.
Para criar um context manager, os métodos __enter__ e __exit__
devem ser implementados.
O método __exit__ receberá a classe de exceção, a exceção e o
traceback. Se ele retornar True, exceção no with será
suprimidas.
"""

# Ex:
# with open('caminho.txt', 'w') as arquivo:
#     ...

class MyContextManager:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
        print('Init')

    def __enter__(self):
        print('Enter')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Exit')
        self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        # exception_.add_note('Minha nota')

        # raise ConnectionError('Não de para conectar')
        # return True  # Tratei a exceção


instancia = MyContextManager('Aula_Context_manager.txt', 'w')

with instancia as alguma_coisa:
    alguma_coisa.write('Linha 1\n')
    # alguma_coisa.write('Linha 2\n', 123)
    alguma_coisa.write('Linha 3\n')
    print('With', alguma_coisa)

# -----------------------------------------------------------------------------------------------------------------------------------------
"""
Context manager com função - Criando e Usando gerenciadores de contexto
"""
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo Arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu uum erro', e)
    finally:
        print('Fechando Arquivo')
        arquivo.close()

with my_open('ContextLib.txt', 'a') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('With', arquivo)