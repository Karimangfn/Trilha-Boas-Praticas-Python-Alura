# Pytest e Estrutura de Testes

## Introdução ao Pytest

- Framework de testes mais utilizado no Python.
- Alternativa mais moderna e "pythônica" ao `unittest`.
- Principais vantagens:
  - Simples de usar
  - Altamente escalável
  - Suporte a plugins e extensões
- Permite executar testes com poucos comandos no terminal.

## Instalação e Configuração

- Ativar ambiente virtual:
  - `source venv/bin/activate`
- Instalar o Pytest:
  - `pip install pytest==7.1.2`

### Gerenciamento de Dependências

- Ver pacotes instalados:
  - `pip freeze`
- Gerar/atualizar arquivo de dependências:
  - `pip freeze > requirements.txt`
- O `requirements.txt` facilita a reprodução do projeto.

## Estrutura de Testes

- Criar diretório:
  - `tests/` (obrigatório esse nome)
- Criar arquivo:
  - `__init__.py` (define o diretório como módulo)
- Criar arquivo de testes:
  - Deve começar com `test_`
  - Exemplo: `test_bytebank.py`

## Padrões do Pytest

- Nome dos métodos deve começar com:
  - `test_`
- Nomes devem ser:
  - **Verbosos e descritivos**

### Exemplo de Nome de Teste

- `test_quando_idade_recebe_13_03_2000_deve_retornar_22`

## Metodologia Given-When-Then

- **Given (Contexto)**:
  - Dados de entrada
- **When (Ação)**:
  - Execução do método
- **Then (Resultado)**:
  - Validação com `assert`

### Exemplo de Teste

```python
from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given
        esperado = 22

        funcionario = Funcionario('Teste', entrada, 1111)
        resultado = funcionario.idade()  # When

        assert resultado == esperado  # Then
````

## Execução dos Testes

* Rodar todos os testes:

  * `pytest`
* Rodar com detalhes:

  * `pytest -v`
* Também é possível rodar testes pela IDE.

### Observações Importantes

* Diretório deve se chamar `tests`
* Arquivos devem começar com `test_`
* Caso contrário, o Pytest não reconhece os testes.

## Metodologia AAA (Arrange-Act-Assert)

* Alternativa ao Given-When-Then:

  * **Arrange**: preparar contexto
  * **Act**: executar ação
  * **Assert**: validar resultado

## Novo Método: sobrenome

* Implementação:

  * Remove espaços com `strip()`
  * Divide o nome com `split(' ')`
  * Retorna o último elemento

### Exemplo

```python
def sobrenome(self):
    nome_completo = self.nome.strip()
    nome_quebrado = nome_completo.split(' ')
    return nome_quebrado[-1]
```

## Teste do Método sobrenome

```python
def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
    entrada = ' Lucas Carvalho '  # Given
    esperado = 'Carvalho'

    funcionario = Funcionario(entrada, '11/11/2000', 1111)
    resultado = funcionario.sobrenome()  # When

    assert resultado == esperado  # Then
```

## Execução de Múltiplos Testes

* `pytest`:

  * Mostra `.` para cada teste que passou
* `pytest -v`:

  * Mostra detalhes de cada teste

## Boas Práticas

* Usar nomes descritivos para testes
* Organizar testes em classes
* Separar testes do código principal
* Manter estrutura padrão do Pytest
* Utilizar metodologias como Given-When-Then ou AAA
