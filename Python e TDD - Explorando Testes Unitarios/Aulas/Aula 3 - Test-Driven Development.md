# Test-Driven Development (TDD)

## Conceito de TDD

* **TDD (Test-Driven Development)** = desenvolvimento guiado por testes.
* Ideia principal:

  * Criar **testes antes do código**.
* Fluxo diferente do comum:

  * Tradicional: código → teste
  * TDD: teste → código → melhoria

## Ciclo do TDD

* O processo segue um ciclo contínuo:

  1. **Testes**
  2. **Código**
  3. **Refatoração**

### Funcionamento

* Criar teste baseado na regra de negócio.
* Executar:

  * Teste **falha** (código ainda não existe).
* Implementar código mínimo:

  * Objetivo: fazer o teste passar.
* Refatorar:

  * Melhorar legibilidade e estrutura.
* Repetir o ciclo.

## Vantagens do TDD

* Testes refletem diretamente as **regras de negócio**.
* Código mais seguro para alterações.
* Facilita trabalho em equipe.
* Base sólida para evolução do sistema.

## Aplicação Prática

### Nova funcionalidade

* Regra:

  * Funcionários com salário ≥ 100000
  * E que sejam diretores/sócios
  * Devem ter **redução de 10% no salário**

---

## Criação do Teste

* Nome do teste deve:

  * Começar com `test_`
  * Ser **descritivo (verboso)**

```python
def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
    entrada_salario = 100000  # given
    entrada_nome = 'Paulo Bragança'
    esperado = 90000

    funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

    funcionario_teste.decrescimo_salario()  # when
    resultado = funcionario_teste.salario

    assert resultado == esperado  # then
```

* Etapas:

  * **Given**: dados de entrada
  * **When**: ação executada
  * **Then**: verificação do resultado

---

## Implementação do Código

```python
def decrescimo_salario(self):
    sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
    
    if self._salario >= 100000 and (self.sobrenome() in sobrenomes):
        decrescimo = self._salario * 0.1
        self._salario = self._salario - decrescimo
```

* Lógica:

  * Verifica salário mínimo
  * Verifica se é diretor/sócio
  * Aplica desconto de 10%

---

## Refatoração

### Problema

* Método com múltiplas responsabilidades:

  * Verifica tipo de funcionário
  * Aplica desconto

### Solução

* Separar responsabilidades

```python
def _eh_socio(self):
    sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
    return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)
```

```python
def decrescimo_salario(self):
    if self._eh_socio():
        decrescimo = self._salario * 0.1
        self._salario = self._salario - decrescimo
```

### Melhorias

* Código mais organizado
* Cada método com **uma única responsabilidade**
* Mais legível e “pythônico”

---
