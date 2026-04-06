## Estrutura Base das Notificações

* Criação da classe abstrata `Notificacao` herdando de `ABC`.
* Implementação do método abstrato `enviar_notificacao`.
* Remoção de métodos específicos (e-mail e SMS) da classe base para evitar implementação desnecessária.
* Aplicação do Princípio da Segregação de Interfaces (ISP) e do Princípio da Responsabilidade Única (SRP).

## Implementação de Notificações Específicas

* Criação das classes `NotificacaoEmail` e `NotificacaoSMS`, herdando de `Notificacao`.
* Implementação do método `enviar_notificacao` em cada classe para notificações específicas.
* Teste das notificações em `main.py`, instanciando as classes e enviando mensagens.
* Ênfase na importância de seguir um padrão para facilitar a manutenção e expansão.

## Padrão Façade para Centralização de Notificações

* Criação do arquivo `notificacao_facade.py` com a classe `NotificacaoFacade`.
* Implementação do método `enviar_notificacoes` para enviar mensagens através de múltiplos canais.
* Uso do padrão Façade para simplificar o envio de notificações em `main.py`.
* Facilitação da adição de novos meios de notificação sem modificar outras partes do sistema.

## Princípio da Segregação de Interfaces (ISP)

O Princípio da Segregação de Interfaces (ISP) afirma que é melhor ter várias interfaces específicas do que uma interface genérica. Isso evita que classes implementem métodos que não utilizam.

**Exemplo de código antes do ISP:**

```python
from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def enviar_email(self, mensagem, destinatario):
        pass

    @abstractmethod
    def enviar_sms(self, mensagem, telefone):
        pass

class Notificador(Notificacao):
    def enviar_email(self, mensagem, destinatario):
        print(f"Enviando e-mail: {mensagem} para {destinatario}")

    def enviar_sms(self, mensagem, telefone):
        print(f"Enviando SMS: {mensagem} para {telefone}")
```

Neste exemplo, se uma classe precisa apenas enviar e-mails, ela é forçada a implementar o método enviar_sms, violando o ISP.

**Exemplo de código após o ISP:**

```python
from abc import ABC, abstractmethod

class NotificacaoEmail(ABC):
    @abstractmethod
    def enviar_email(self, mensagem, destinatario):
        pass

class NotificacaoSMS(ABC):
    @abstractmethod
    def enviar_sms(self, mensagem, telefone):
        pass

class NotificadorEmail(NotificacaoEmail):
    def enviar_email(self, mensagem, destinatario):
        print(f"Enviando e-mail: {mensagem} para {destinatario}")

class NotificadorSMS(NotificacaoSMS):
    def enviar_sms(self, mensagem, telefone):
        print(f"Enviando SMS: {mensagem} para {telefone}")
```

Neste exemplo, cada interface é específica para um tipo de notificação, permitindo que as classes implementem apenas os métodos necessários, seguindo o ISP.