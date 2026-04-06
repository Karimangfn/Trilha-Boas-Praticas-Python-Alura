## Atualização de Status do Pedido e Princípio da Inversão de Dependências

* Adição do atributo `status` à classe `Pedido` com inicialização "Criado!".
* Utilização de `properties` para criar métodos `getter` e `setter` para o atributo `status`.
* Discussão sobre o Princípio da Inversão de Dependências (DIP), enfatizando a dependência de abstrações e não de implementações concretas.
* Teste da funcionalidade de atualização de status e envio de notificações.
* Introdução à ideia de aprimorar o processo de definição e alteração de status com padrões de projeto.

## Padrão de Design Observador para Monitoramento de Status

* Criação da estrutura do observador com a classe `ObservadorStatus` e o método `atualizar()`.
* Implementação do método de notificação para enviar mensagens sobre mudanças de status.
* Gerenciamento de observadores na classe `Pedido` com métodos para adicionar e notificar observadores.
* Modificação do setter do status para notificar os observadores automaticamente.
* Automatização do monitoramento de mudanças de estado do objeto.

## Organização e Melhoria do Código

* Remoção de código desnecessário, incluindo pedido de retirada e simplificação do pedido de delivery.
* Alteração no processamento de pagamento para integração direta da criação e processamento.
* Limpeza de imports não utilizados.
* Importação e configuração do padrão de projeto Observer com a classe `ObservadorStatus`.
* Criação de mensagens constantes para confirmação de pagamento e status do pedido.
* Estrutura de notificação e observador para receber notificações sobre mudanças de status.
* Atualização de status do pedido com constantes e teste no terminal.
* Conclusão da estrutura do projeto com aplicação dos princípios SOLID e design patterns.

## Princípio da Inversão de Dependências (DIP)

O Princípio da Inversão de Dependências (DIP) afirma que módulos de alto nível não devem depender de módulos de baixo nível, mas ambos devem depender de abstrações. Abstrações não devem depender de detalhes, mas detalhes devem depender de abstrações.

**Exemplo de código antes do DIP:**

```python
class NotificadorSMS:
    def enviar(self, mensagem, telefone):
        print(f"Enviando SMS: {mensagem} para {telefone}")

class Pedido:
    def __init__(self, cliente, itens, telefone):
        self.cliente = cliente
        self.itens = itens
        self.telefone = telefone
        self.notificador = NotificadorSMS()

    def confirmar_pedido(self):
        # Lógica de confirmação do pedido
        self.notificador.enviar("Pedido confirmado!", self.telefone)
```

Neste exemplo, a classe Pedido depende diretamente da classe NotificadorSMS, violando o DIP. Se quisermos adicionar outro tipo de notificação (por exemplo, e-mail), precisamos modificar a classe Pedido.

**Exemplo de código após o DIP:**

```python
from abc import ABC, abstractmethod

@abstractmethod
class Notificador(ABC):
    def enviar(self, mensagem, contato):
        pass

class NotificadorSMS(Notificador):
    def enviar(self, mensagem, telefone):
        print(f"Enviando SMS: {mensagem} para {telefone}")

class NotificadorEmail(Notificador):
    def enviar(self, mensagem, email):
        print(f"Enviando email: {mensagem} para {email}")

class Pedido:
    def __init__(self, cliente, itens, notificador):
        self.cliente = cliente
        self.itens = itens
        self.notificador = notificador

    def confirmar_pedido(self):
        # Lógica de confirmação do pedido
        self.notificador.enviar("Pedido confirmado!", self.cliente.email)
```

Neste exemplo, a classe Pedido depende de uma abstração Notificador, permitindo que usemos diferentes tipos de notificadores sem modificar a classe Pedido, seguindo o DIP.