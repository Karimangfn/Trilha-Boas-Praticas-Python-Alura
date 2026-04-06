# **Sistema de Gerenciamento de Pedidos**

## **Descrição**

Este projeto implementa um sistema de gerenciamento de pedidos que simula um fluxo de pedidos de clientes, incluindo cálculo de totais, notificações, pagamento e atualização de status.

---

## **Funcionalidades**

- **Cadastro de Clientes e Itens**: Gerencia informações de clientes e produtos.
- **Gestão de Pedidos**: Suporte a pedidos para delivery e retirada.
- **Sistema de Pagamento**: Simulação de processamento de pagamentos.
- **Notificações**: Envio de notificações por e-mail e SMS.
- **Atualização de Status**: Rastreamento e notificação do status do pedido.
---

## **Tecnologias Utilizadas**

- **Python 3.10+**
- Design Patterns: _Factory Method, Template, Strategy, Facade, Observer_.
- Princípios **SOLID**.

---

## **Estrutura do Projeto**

```
.
├── cliente.py
├── item.py
├── main.py
├── notificacao/
│   ├── notificacao.py
│   ├── notificacao_email.py
│   ├── notificacao_sms.py
│   └── notificacao_facade.py
├── observador/
│   └── observador_status.py
├── pagamento/
│   ├── pagamento.py
│   ├── pagamento_cartao.py
│   └── pagamento_pix.py
├── pedido/
│   ├── pedido.py
│   ├── pedido_delivery.py
│   └── pedido_retirada.py
└── README.md
```

---

## **Como Executar**

1. Acesse o arquivo `main.py`.
2. Execute o programa:
   ```bash
   python main.py
   ```

---

## **Exemplo de Uso**

- **Cadastrar Cliente e Itens**:
  Crie um cliente e adicione itens ao pedido.
- **Criar Pedido**:
  Escolha entre _delivery_ ou _retirada_.
- **Efetuar Pagamento**:
  Simule pagamentos via Pix ou Cartão.
- **Receber Notificações**:
  Clientes recebem notificações do status do pedido.

---

## **Autoria**

Projeto desenvolvido como estudo dos princípios **SOLID** e padrões de design para organização de software escalável e modular.

Feito pela Escola de Programação da Alura!