# Testes Automatizados

## Introdução ao Curso

* Curso focado em **testes automatizados** e **TDD (Test-Driven Development)**.
* Voltado para quem já possui conhecimento em Python, especialmente:

  * Orientação a objetos (classes, métodos, instâncias).
* Testes são aplicáveis em diversas áreas:

  * Web
  * Automação
  * DevOps

## Preparação do Ambiente

* Versões utilizadas:

  * Python 3.8+
  * PyCharm (ou VSCode como alternativa)
* Criar ambiente virtual:

  * `python3 -m venv venv`
* Ativar ambiente:

  * Linux/macOS: `source venv/bin/activate`
* Utilizar ambiente virtual evita conflitos entre projetos.

## Contexto do Projeto

* Projeto baseado na empresa fictícia **Bytebank**.
* Personagem:

  * Dominique (dev iniciante).
* Objetivo:

  * Desenvolver uma classe `Funcionario`.

### Estrutura Inicial

* Pasta `codigo`

  * Arquivo `bytebank.py` com a classe `Funcionario`
* Atributos principais:

  * Nome
  * Data de nascimento
  * Salário

### Métodos da Classe

* `idade`: calcula idade do funcionário.
* `calcular_bonus`: regra de negócio.
* `__str__`: retorna dados do funcionário.

## Execução e Teste Manual

* Criar arquivo `main.py`:

  * Instanciar objeto:

    * `Funcionario('Lucas Carvalho', 2000, 1000)`
* Executar:

  * `print(lucas)`
  * `print(lucas.idade)`

## Correção de Bug

### Problema

* Data de nascimento informada apenas como ano.
* Ao usar formato completo (`"13/03/2000"`), ocorre erro.

### Solução

* Quebrar a string da data:

  * `split('/')`
* Extrair o ano:

  * `data_nascimento_quebrada[-1]`
* Converter para inteiro:

  * `int(ano_nascimento)`

## Criação do Primeiro Teste Automatizado

* Criar função de teste:

```python
def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')
```

* Executar chamando:

```python
teste_idade()
```

* Teste verifica automaticamente se o comportamento está correto.

## Conceito de Testes Automatizados

* Testes verificam se o código:

  * Respeita regras de negócio
  * Retorna resultados esperados

### Vantagens

* Execução rápida
* Feedback imediato
* Mais segurança ao alterar código
* Facilita refatoração

## Testes Manuais vs Automatizados

### Testes Manuais

* Feitos por pessoas (testers)
* Mais detalhados
* Mais lentos e sujeitos a erro humano

### Testes Automatizados

* Executados automaticamente
* Mais rápidos
* Reutilizáveis
* Ideais para validação contínua

## Tipos de Testes

### Testes Unitários

* Testam pequenas partes do código:

  * Funções
  * Métodos
  * Classes

### Testes de Integração

* Testam interação entre partes do sistema.

### Testes End-to-End (E2E)

* Testam o sistema completo:

  * Simulam o usuário real

## Evolução dos Testes

* Testar múltiplos cenários:

```python
funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
funcionario_teste2 = Funcionario('Teste', '01/12/1999', 1111)
```

* Problema:

  * Código cresce muito
* Solução:

  * Uso de frameworks como **Pytest**

## Próximos Passos

* Aprender sobre:

  * Pytest
  * Organização de testes
  * TDD
* Evoluir testes para algo mais escalável e profissional

---
