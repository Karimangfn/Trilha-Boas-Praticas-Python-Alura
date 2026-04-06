# Nomenclatura, Tipagem e Organização de Código

## Convenções de Nomenclatura (PEP 8)
- **Classes**: Devem seguir o padrão **PascalCase**.
- **Variáveis, funções e métodos**: Devem ser escritos em **snake_case**.
- **Constantes**: Devem ser declaradas em **SCREAMING_SNAKE_CASE**.

### Exemplo de correção:
```python
class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

contador_produto = 0  # Correto (antes: ContadorProduto)
def criar_produto(nome: str, preco: float):  # Correto (antes: criarproduto)
    return Produto(nome, preco)
```
Seguir essas convenções melhora a clareza e a padronização do código.

## Tipagem em Python
- Importação de tipos do módulo `typing` como `List` e `Dict`.
- Definição explícita do tipo de variáveis e funções para maior clareza.
- Uso da seta (`->`) para indicar o tipo de retorno de funções.

### Exemplo:
```python
from typing import List, Dict

contador_produto: int = 0
usuarios: List[str] = ["Alice", "Bob"]

def criar_produto(nome: str, preco: float) -> Dict[str, str]:
    return {"nome": nome, "preco": str(preco)}
```
A tipagem melhora a legibilidade e evita erros no código.

## Organização do Projeto

### Separação entre Modelos e Rotas
- Criar uma pasta `models` para armazenar modelos de dados:
  - `models/models_produtos.py`
  - `models/models_usuarios.py`
- Uso da classe `BaseModel` do **Pydantic** para validação de dados.
- Criar um arquivo `__init__.py` em cada pasta para que sejam reconhecidas como módulos Python.

Organizar os modelos facilita a manutenção e a escalabilidade do projeto.

### Estruturando Rotas com FastAPI
- Criar uma pasta `routers` para armazenar as rotas:
  - `routers/routers_usuarios.py`
  - `routers/routers_produtos.py`
- Utilizar `@router.post()` e `@router.get()` para definir rotas ao invés de `@app.post()` e `@app.get()`.
- Criar um arquivo `main.py` para inicializar o FastAPI e incluir os roteadores.

### Exemplo de `main.py`:
```python
from fastapi import FastAPI
from app.routers import routers_usuarios, routers_produtos

app = FastAPI()

app.include_router(routers_usuarios.router)
app.include_router(routers_produtos.router)
```
Executar o servidor com:
```
uvicorn app.main:app --reload
```
A estrutura modular torna o código mais organizado, facilitando o desenvolvimento e a manutenção.