from abc import ABC, abstractmethod

class Notificacao(ABC):
    def enviar_notificacao(self, cliente, mensagem):
        pass