## Estrutura Base do Pagamento

* Criação da pasta `pagamento` e do arquivo `__init__.py` para definir o módulo.
* Desenvolvimento da classe abstrata `Pagamento` herdando de `ABC`.
* Implementação do método abstrato `processar()` para o processamento de pagamentos.
* Discussão sobre os princípios O (Aberto/Fechado) e S (Segregação de Interface) do SOLID.

## Implementação de Pagamentos Específicos e Princípio de Liskov

* Criação das classes `PagamentoCartao` e `PagamentoPIX`, herdando de `Pagamento`.
* Implementação do método `processar()` em cada classe para pagamentos específicos.
* Teste do sistema em `main.py`, instanciando as classes e processando pagamentos.
* Aplicação do Princípio da Substituição de Liskov (LSP), permitindo que as subclasses substituam a superclasse sem quebrar o código.
* Menção à possibilidade de implementar outros padrões de design.

## Fábrica de Pagamentos e Padrão Factory

* Criação do arquivo `pagamento_factory.py` com a classe `PagamentoFactory`.
* Implementação do método estático `criar_pagamento(tipo)` para criar instâncias de pagamento.
* Utilização de condições para retornar a instância correta (por exemplo, `PagamentoPIX` ou `PagamentoCartao`).
* Tratamento de erros para tipos de pagamento não suportados.
* Integração da fábrica em `main.py` para facilitar a criação de pagamentos.
* Facilitação da expansão do sistema com novos métodos de pagamento.

## Princípio da Substituição de Liskov (LSP)

O Princípio da Substituição de Liskov (LSP) afirma que objetos de uma superclasse devem ser substituíveis por objetos de suas subclasses sem alterar a correção do programa. Em outras palavras, uma subclasse deve poder substituir sua classe base sem introduzir comportamentos inesperados.

**Exemplo de código antes do LSP:**

```python
class Pagamento:
    def processar(self, valor, tipo_pagamento):
        if tipo_pagamento == "cartao":
            print(f"Processando pagamento de R${valor:.2f} via cartão.")
        elif tipo_pagamento == "pix":
            print(f"Processando pagamento de R${valor:.2f} via PIX.")
        else:
            raise ValueError("Tipo de pagamento não suportado.")

def realizar_pagamento(pagamento, valor, tipo_pagamento):
    pagamento.processar(valor, tipo_pagamento)

pagamento = Pagamento()
realizar_pagamento(pagamento, 100.00, "cartao")
```

Neste exemplo, a classe Pagamento precisa conhecer todos os tipos de pagamento, violando o LSP. Se adicionarmos um novo tipo de pagamento, precisamos modificar a classe Pagamento.

**Exemplo de código após o LSP:**

```python
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class PagamentoCartao(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} via cartão.")

class PagamentoPIX(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} via PIX.")

def realizar_pagamento(pagamento, valor):
    pagamento.processar(valor)

pagamento_cartao = PagamentoCartao()
realizar_pagamento(pagamento_cartao, 100.00)

pagamento_pix = PagamentoPIX()
realizar_pagamento(pagamento_pix, 50.00)
```

Neste exemplo, cada tipo de pagamento tem sua própria classe, que implementa o método processar(). A função realizar_pagamento não precisa conhecer os tipos de pagamento, apenas a interface Pagamento, seguindo o LSP.