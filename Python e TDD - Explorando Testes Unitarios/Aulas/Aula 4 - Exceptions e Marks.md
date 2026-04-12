# Exceptions e Marks

## Método `calcular_bonus`

* Regra de negócio:

  * Funcionário recebe bônus se:

    * 10% do salário ≤ 1000
* Caso contrário:

  * Não recebe bônus

### Implementação inicial

```python
def calcular_bonus(self):
    valor = self._salario * 0.1
    if valor > 1000:
        valor = 0
    return valor
```

---

## Teste do Bônus (cenário válido)

```python
def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
    entrada = 1000  # given
    esperado = 100

    funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
    resultado = funcionario_teste.calcular_bonus()  # when

    assert resultado == esperado  # then
```

---

## Uso de Exceptions

### Alteração da regra

* Em vez de retornar `0`:

  * Deve lançar uma **exception**

### Implementação

```python
def calcular_bonus(self):
    valor = self._salario * 0.1
    if valor > 1000:
        raise Exception('O salário é muito alto para receber um bônus')
    return valor
```

---

## Teste com Exception

```python
import pytest

def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
    with pytest.raises(Exception):
        entrada = 100000000  # given

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()  # when

        assert resultado  # then
```

---

## Execução de Testes Específicos

* Rodar todos:

```bash
pytest -v
```

* Filtrar por nome:

```bash
pytest -k idade
```

---

## Marks (Markers)

* Marks são **tags** para organizar testes

### Uso

```python
from pytest import mark

@mark.calcular_bonus
def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
    ...
```

```python
@mark.calcular_bonus
def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
    ...
```

---

## Executar por Mark

```bash
pytest -v -m calcular_bonus
```

---

## Marks úteis

### Skip

```python
@mark.skip(reason="não executar agora")
def test_exemplo():
    ...
```

### Skipif

```python
import sys

@mark.skipif(sys.version_info < (3, 10), reason="Requer Python 3.10+")
def test_exemplo():
    ...
```

### Xfail

```python
@mark.xfail
def test_exemplo():
    ...
```

---

## Arquivo `pytest.ini`

* Configuração do Pytest

```ini
[pytest]
markers =
    calcular_bonus: Teste para o metodo calcular_bonus
```

* Remove warnings de markers personalizados

---

## Customização de padrões

```ini
[pytest]
python_functions=*_testando
python_classes=testando_*
python_files=muitos_testes_*
```
