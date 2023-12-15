"""
Polimorfismo em Python Orientado a Objetos
Polimorfismo é o princípio que permite que
classes deridavas de uma mesma superclasse
tenham métodos iguais (com mesma assinatura)
mas comportamentos diferentes.
Assinatura do método = Mesmo nome e quantidade
de parâmetros (retorno não faz parte da assinatura)
Opinião + princípios que contam:
Assinatura do método: nome, parâmetros e retorno iguais
SO"L"ID
Princípio da substituição de liskov
Objetos de uma superclasse devem ser substituíveis
por objetos de uma subclasse sem quebrar a aplicação.+
Sobrecarga de métodos (overload)
Sobreposição de métodos (override)
"""
from abc import ABC, abstractmethod


class Notificacao(ABC):  # Classe pai que herda método abstrato da classe ABC
    def __init__(self, mensagem) -> None:  # Contrutor com um atributo mensagem
        self.mensagem = mensagem

    # Método abstrato do tipo bool, ou seja os seus métodos implementados nas outras classes devem ter um retorno desse mesmo tipo
    @abstractmethod
    def enviar(self) -> bool:
        ...


# As duas classes abaixo fazem a mesma coisa, herdam da classe notificação e implementam os seus métodos da classe pai
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando: ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando:', self.mensagem)
        return False


# O polimorfismo, é uma função que recebe a classe pai como paramêtro, e acessa os seus métodos e os métodos dos seus filhos
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()  # Para que dessa forma possa realizar suas próprias ações
    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação não enviada')


notificacao_email = NotificacaoEmail('Testando E-Mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)

n = NotificacaoSMS('Testando')
n.enviar()
