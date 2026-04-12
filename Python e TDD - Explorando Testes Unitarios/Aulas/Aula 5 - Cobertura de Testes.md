# Cobertura de Testes

## Conceito

* Cobertura de testes mede **quais partes do código estão sendo testadas**.
* Objetivo ideal:

  * **100% de cobertura**
* Problema:

  * Ter testes **não garante** que todo o código foi testado.

## Ferramenta

* Extensão do Pytest:

  * `pytest-cov`
* Instalação:

```bash
pip install pytest-cov==3.0.0
```

* Atualizar dependências:

```bash
pip freeze > requirements.txt
```

## Executando Coverage

* Rodar coverage geral:

```bash
pytest --cov
```

* Rodar apenas no código:

```bash
pytest --cov=codigo tests/
```

## Relatório

* Exibe:

  * `Stmts`: linhas de código
  * `Miss`: linhas sem teste
  * `Cover`: porcentagem

* Exemplo:

  * 97% cobertura → existe código não testado

## Identificando Falhas

* Mostrar linhas não cobertas:

```bash
pytest --cov=codigo tests/ --cov-report term-missing
```

* Mostra exatamente:

  * **quais linhas não têm teste**

## Testando Linhas Faltantes

* Criar testes para cobrir partes não testadas
* Exemplo:

  * método `__str__`

```python
def test_retorno_str(self):
    nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000
    esperado = 'Funcionario (Teste, 12/03/2000, 1000)'

    funcionario = Funcionario(nome, data_nascimento, salario)
    resultado = funcionario.__str__()

    assert resultado == esperado
```

## Quando NÃO testar

* Não testar:

  * Métodos internos da linguagem (ex: `__str__`)
* Testes devem focar em:

  * **regra de negócio**
  * **lógica criada pelo dev**

## Excluir do Coverage

* Criar `.coveragerc`:

```ini
[run]
source = ./codigo

[report]
exclude_lines =
    def __str__
```

## Relatório Visual

* Gerar HTML:

```bash
pytest --cov=codigo tests/ --cov-report html
```

* Gera pasta:

  * `htmlcov/` (ou personalizada)

## Personalização

* Alterar diretório do HTML:

```ini
[html]
directory = coverage_relatorio_html
```

## Automatizando com pytest.ini

```ini
[pytest]
addopts = -v --cov=codigo tests/ --cov-report term-missing

markers =
    calcular_bonus: Teste para o metodo calcular_bonus
```

* Agora basta rodar:

```bash
pytest
```

## Relatórios adicionais

* XML de testes:

```bash
pytest --junitxml report.xml
```

* XML de coverage:

```bash
pytest --cov-report xml
```
