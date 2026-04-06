# Testes Automatizados com PyTest e FastAPI  

## Introdução aos Testes Automatizados  
- Substituir testes manuais por testes automatizados facilita a verificação de funcionalidades.  
- PyTest é um dos frameworks mais utilizados para testes em Python.  
- Configuração inicial:  
  - Instalação do PyTest.  
  - Organização do projeto com uma pasta `tests`.  
  - Criação de arquivos de teste específicos para a API.  
- Uso do `assert` para validar se os resultados das funções estão corretos.  
- Integração com FastAPI utilizando `TestClient` para simular requisições e validar respostas.  
- Instalação do `HTTPX` para possibilitar testes com FastAPI.  

## Testes para Rotas de Produtos e Usuários  
### Testes de Produtos  
1. **Criação de Produtos** (`test_criar_produtos`)  
   - Envio de um JSON via `client.post()`.  
   - Validação da resposta (status 200 e nome correto).  
2. **Listagem de Produtos** (`test_listar_produtos`)  
   - Requisição `client.get()` para listar produtos.  
   - Verificação da resposta e do número de produtos retornados.  

### Testes de Usuários  
1. **Criação de Usuários** (`test_criar_usuarios`)  
   - Envio do nome do usuário via parâmetro na URL.  
   - Validação do ID e nome na resposta.  
2. **Listagem de Usuários** (`test_listar_usuarios`)  
   - Requisição `client.get()` para listar usuários.  
   - Verificação do status e do número de usuários retornados.  

- Todos os testes foram executados e passaram com sucesso.  
- Destacada a importância de boas práticas na organização do código.  

### Teste do Histórico de Compras  
- Verificação do endpoint `/historico_compras/{usuario_id}`.  
- Envio de um JSON contendo IDs dos produtos comprados.  
- Validação da resposta da API.  

### Teste das Recomendações de Produtos  
- Verificação do endpoint `/recomendacoes/{usuario_id}`.  
- Envio de JSON com categorias e tags de preferências.  
- Confirmação do número esperado de produtos recomendados na resposta.  

- Importância de testar APIs com clareza sobre funcionamento e resposta esperada.  
- Introdução à existência de outros tipos de testes além dos unitários. 