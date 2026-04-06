# Primeiros passos em boas praticas

## Instalação e Configuração

- Criar um ambiente virtual com `python -m venv venv` para isolar dependências.
- Ativar o ambiente virtual (`venv\Scripts\activate` no Windows ou `source venv/bin/activate` no macOS/Linux).
- Instalar dependências com `pip install -r requirements.txt`.
- Verificar pacotes instalados com `pip freeze` e atualizar `requirements.txt` usando `pip freeze > requirements.txt`.
- O uso de um ambiente virtual evita conflitos entre bibliotecas de diferentes projetos.

## Estrutura do Projeto

- **Arquivos Principais**:
  - `app.py`: Arquivo principal da aplicação.
  - `requirements.txt`: Lista de dependências do projeto.
  - `.gitignore`: Define arquivos que não devem ser versionados.
  - `README.md`: Documentação do projeto.

## Desenvolvimento da API

### Importação de Bibliotecas

- Importação de **FastAPI** e **pydantic** para a construção da API e manipulação de modelos de dados.

### Modelos de Dados

- Utilização de `BaseModel` do **pydantic** para definir modelos, como:
  - `ProdutoBase`
  - `CriarProduto`
  - `Produto`
  - `HistoricoCompras`
  - `Preferencias`
  - `Usuario`

### Estruturação das Variáveis

- Listas para armazenar produtos e usuários.
- Contadores e um dicionário para o histórico de compras.

### Implementação das Rotas

- Rotas para:
  - Criar e listar produtos e usuários.
  - Registrar histórico de compras.
  - Gerar recomendações com base nas preferências do usuário.

### Execução do Projeto

- Rodar a API com `uvicorn app:app --reload`.
- Acessar a documentação automática via FastAPI em `http://127.0.0.1:8000/docs`.

### Testes

- Testes para:
  - Criar produtos e usuários.
  - Registrar compras.
  - Validar recomendações baseadas nas preferências.

## Boas Práticas de Codificação

- Seguir a **PEP 8** para manter um código organizado e legível.
- Diretrizes incluem:
  - Nomeação adequada de variáveis e funções.
  - Uso consistente de indentação e espaçamentos.
  - Limitação do tamanho das linhas de código.
- Aplicar boas práticas melhora a manutenção e a legibilidade do código.

## Link Documentação PEP8: 
- https://peps.python.org/pep-0008/