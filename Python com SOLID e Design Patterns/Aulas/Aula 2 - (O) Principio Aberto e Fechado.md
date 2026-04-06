## Estrutura Base do Pedido

* Criação da classe abstrata `Pedido` com atributos `cliente` e `itens`.
* Implementação do método abstrato `calcular_total` para cálculo do valor total do pedido.
* Utilização de `ABC` e `@abstractmethod` para garantir a implementação de `calcular_total` nas subclasses.
* Aplicação do padrão de design Template Method.

## Pedido de Retirada

* Criação da classe `PedidoRetirada` que herda de `Pedido`.
* Implementação do método `calcular_total` para somar os preços dos itens.
* Teste da classe em `main.py` para verificar o cálculo correto do total.

## Pedido Delivery

* Criação da classe `PedidoDelivery` que herda de `Pedido`.
* Adição do atributo `taxa_entrega` ao construtor.
* Modificação do método `calcular_total` para incluir a taxa de entrega no cálculo.
* Teste da classe em `main.py` para validar o cálculo correto do total com a taxa de entrega.
* Aplicação do princípio aberto/fechado do SOLID para extensão da funcionalidade.

## Princípio Aberto/Fechado (OCP)

O princípio Aberto/Fechado (OCP) afirma que uma entidade de software (classe, módulo, função, etc.) deve estar aberta para extensão, mas fechada para modificação. Isso significa que você deve ser capaz de adicionar novas funcionalidades sem alterar o código existente.

**Exemplo de código antes do OCP:**

```python
class Pedido:
    def __init__(self, cliente, itens, tipo_pedido):
        self.cliente = cliente
        self.itens = itens
        self.tipo_pedido = tipo_pedido

    def calcular_total(self):
        total = sum(item.preco for item in self.itens)
        if self.tipo_pedido == "retirada":
            return total
        elif self.tipo_pedido == "delivery":
            return total + 10  # Taxa de entrega fixa
```

Neste exemplo, se quisermos adicionar um novo tipo de pedido, precisamos modificar a classe `Pedido`, violando o OCP.

**Exemplo de código após o OCP:**

```python
from abc import ABC, abstractmethod

class Pedido(ABC):
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens

    @abstractmethod
    def calcular_total(self):
        pass

class PedidoRetirada(Pedido):
    def calcular_total(self):
        return sum(item.preco for item in self.itens)

class PedidoDelivery(Pedido):
    def __init__(self, cliente, itens, taxa_entrega):
        super().__init__(cliente, itens)
        self.taxa_entrega = taxa_entrega

    def calcular_total(self):
        return sum(item.preco for item in self.itens) + self.taxa_entrega
```

Neste exemplo, criamos subclasses para cada tipo de pedido, permitindo adicionar novos tipos sem modificar a classe Pedido. Isso segue o princípio OCP.

## Link - Refactoring Guru:
- https://refactoring.guru/
