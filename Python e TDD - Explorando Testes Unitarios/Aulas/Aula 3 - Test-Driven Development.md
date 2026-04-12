# Aula 3 - Test-Driven Development

## Transcrição

Na última aula, aprendemos a utilizar o Pytest para criar testes automatizados e exploramos metodologias como Given-When-Then. Agora, vamos aprofundar um conceito muito importante no mundo de testes: o Test-Driven Development (TDD).

Inicialmente, seguimos o fluxo tradicional: primeiro implementamos uma funcionalidade (como o método sobrenome) e depois criamos testes para validá-la. Porém, o TDD propõe exatamente o contrário — primeiro criamos os testes, depois implementamos o código.

O TDD (Desenvolvimento Guiado por Testes) funciona em um ciclo contínuo composto por três etapas:

1. Testes: criamos testes baseados nas regras de negócio.
2. Código: implementamos o mínimo necessário para fazer os testes passarem.
3. Refatoração: melhoramos o código mantendo os testes passando.

Esse ciclo se repete constantemente ao longo do desenvolvimento.

A principal vantagem dessa abordagem é que os testes se tornam a base do projeto, garantindo que o código sempre respeite as regras de negócio. Além disso, o TDD aumenta a segurança ao modificar códigos existentes e melhora a colaboração entre desenvolvedores.

---

## Aplicando TDD na prática

Uma nova funcionalidade foi solicitada: aplicar um decréscimo de 10% no salário de diretores, que possuem salários a partir de R$100.000,00.

### 1. Criando o teste (primeiro passo do TDD)

```python
def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
    entrada_salario = 100000  # Given
    entrada_nome = 'Paulo Bragança'
    esperado = 90000

    funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
    funcionario_teste.decrescimo_salario()  # When
    resultado = funcionario_teste.salario

    assert resultado == esperado  # Then
````

Ao executar esse teste, ele falhará — pois ainda não existe a implementação.

---

### 2. Implementando o código

```python
def decrescimo_salario(self):
    sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
    if self._salario >= 100000 and (self.sobrenome() in sobrenomes):
        decrescimo = self._salario * 0.1
        self._salario = self._salario - decrescimo
```

Após implementar, executamos os testes novamente — agora eles passam.

---

### 3. Refatoração

O método criado realiza múltiplas responsabilidades: verificar se é sócio e aplicar o desconto. Para melhorar isso, podemos separar essas responsabilidades.

#### Criando método auxiliar:

```python
def _eh_socio(self):
    sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
    return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)
```

#### Atualizando método principal:

```python
def decrescimo_salario(self):
    if self._eh_socio():
        decrescimo = self._salario * 0.1
        self._salario = self._salario - decrescimo
```

Após a refatoração, rodamos os testes novamente e verificamos que tudo continua funcionando corretamente.

---
