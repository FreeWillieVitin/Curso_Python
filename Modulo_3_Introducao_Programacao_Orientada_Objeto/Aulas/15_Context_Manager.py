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

class MyContextManager: # classe que vai receber os atributos para a criação de um arquivo de texto com context manager
    def __init__(self, caminho_arquivo, modo): # Método inicializador criando os atributos de caminho onde o arquivo será gerado e o o atributo que recebe o modo, se é um arquivo de leitura ou escrita
        self.caminho_arquivo = caminho_arquivo 
        self.modo = modo
        self._arquivo = None # Temos também o atributo que vai receber a abertura do arquivo e a finalização dele
        print('Init')

    def __enter__(self): # Método enter retorna um objeto que representa o contexto e pode ser atribuído a uma variável opcional, no caso atribuímos a abertura do arquivo ao atributo _arquivo
        print('Enter') # Esse método é chamado antes do bloco de with
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_): # Após o termino do bloco with chamamos o método with, é nele que será feita a limpeza de recursos e o tratamento de exceções
        print('Exit') # Para essas exceções que inserimos 3 argumentos, que normalmente tem os nomes acima mas isso é apenas por convenção
        self._arquivo.close() # No caso do exemplo o método é o  responsável pelo fechamoento de forma correta e segura do arquivo de texto criado

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        # exception_.add_note('Minha nota')

        # raise ConnectionError('Não de para conectar')
        # return True  # Tratei a exceção


instancia = MyContextManager('Aula_Context_manager.txt', 'w') # Então instanciamos a classe e damos a ela os parâmetros necessários que é o caminho do arquivo e o seu modo w - writer

with instancia as alguma_coisa: # Enfim criamos o bloco with que irá criar o arquivo, não precisamos chamas os métodos eles reconhecem o bloco with e são disparados apenas pela instanciação da classe
    alguma_coisa.write('Linha 1\n')
    # alguma_coisa.write('Linha 2\n', 123)
    alguma_coisa.write('Linha 3\n')
    print('With', alguma_coisa)

# -----------------------------------------------------------------------------------------------------------------------------------------
"""
Context manager com função - Criando e Usando gerenciadores de contexto
"""
from contextlib import contextmanager # Podemos também trabalhar com context manager em funções usando o módulo contextlib e o seu decorador @contextmanager

@contextmanager # O decorador é chamado antes da função sendo assim não precisamos criar métodos enter ou exit, pois está tudo incluido no decorador
def my_open(caminho_arquivo, modo): # temso então uma função que recebe dois argumentos como parâmetro
    try: # Tentamos criar o arquivo
        print('Abrindo Arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8') # Criando assim uma variável que vai receber o que for passado como parâmetro
        yield arquivo # Dentro do bloco yield podemos realizar operações com a variável arquivo
    except Exception as e: # Caso ocorrá um erro exibirá a mensagem abaixo
        print('Ocorreu uum erro', e)
    finally: # Caso tudo ocorrá de forma correta o arquivo é fechado executando o que seria o exit no exemplo acima
        print('Fechando Arquivo')
        arquivo.close()

with my_open('ContextLib.txt', 'a') as arquivo: # Criado então a função, podemos executa-lá e vê-la funcionar
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('With', arquivo)