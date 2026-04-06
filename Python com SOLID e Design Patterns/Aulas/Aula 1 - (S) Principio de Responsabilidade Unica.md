# Curso de Boas Práticas com Python

## Introdução ao Curso  
- **Objetivo:** Aplicar boas práticas em projetos Python utilizando design patterns.  
- **Projeto:** Construção de um sistema de gerenciamento de pedidos, incluindo:  
  - Pagamentos.  
  - Notificações.  
  - Atualização de status.  
- **Pré-requisitos:**  
  - Conhecimento intermediário em Python.  

## Classe Cliente e Main
- Revisão da estrutura do projeto (`.gitignore`, `README.md`).  
- Importância de utilizar Python 3.10 ou superior.  
- Conceitos abordados:  
  - **Design Patterns.**  
  - **Princípios SOLID.**  
  - **Programação Orientada a Objetos (POO).**  
- Configuração do ambiente virtual para o projeto.  
- Implementação da **classe Cliente**:  
  - Atributos: `nome` e `endereco`.  
  - Definição do método especial `__init__`.  
- Testes da classe no `main.py`:  
  - Importação e criação de uma instância.  
  - Verificação dos atributos.  
- **Resultado:** Cadastro de clientes implementado com sucesso.

## Classe Item e Separação de Responsabilidades
- Aplicação do **Princípio da Responsabilidade Única**.  
- Criação da classe **Item** em `item.py`:  
  - Atributos: `nome` e `preco`.  
  - Evita adicionar métodos na classe Cliente, garantindo separação de responsabilidades.  
- Testes no `main.py`:  
  - Importação da classe `Item`.  
  - Criação de dois itens (exemplo: pizza e refrigerante).  
  - Exibição das informações de um item.  
- **Conclusão:** Estrutura do sistema organizada, pronta para a gestão de pedidos. 

## Princípio da Responsabilidade Única (SRP)
- O Princípio da Responsabilidade Única (SRP) afirma que uma classe deve ter apenas uma razão para mudar, ou seja, ela deve ter uma única responsabilidade.

### Exemplo antes de aplicar o SRP:

```python
# Classe com múltiplas responsabilidades
class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    def calculate_total(self):
        return sum(item['price'] for item in self.items)

    def save_order(self):
        # Lógica para salvar o pedido no banco de dados
        print("Order saved to database")
```

## Explicação:

No exemplo acima, a classe `Order` possui duas responsabilidades:

1. Calcular o total do pedido (método `calculate_total`).
2. Salvar o pedido no banco de dados (método `save_order`).

Isso viola o Princípio da Responsabilidade Única, pois a classe tem mais de uma razão para mudar: mudanças no cálculo do total ou na lógica de persistência no banco de dados.

## Exemplo após aplicar o SRP:

```python
# Responsabilidade de calcular o total
class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    def calculate_total(self):
        return sum(item['price'] for item in self.items)

# Responsabilidade de salvar o pedido
class OrderRepository:
    def save_order(self, order):
        # Lógica para salvar o pedido no banco de dados
        print("Order saved to database")
```
 