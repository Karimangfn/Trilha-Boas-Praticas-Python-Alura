# Formatação e Documentação de Código em Python  

## Organização dos Imports  
- Separar os imports em linhas distintas e garantir um espaço após a vírgula.  
- Ordem correta:  
  1. Bibliotecas padrão do Python  
  2. Imports de terceiros  
  3. Imports locais

## Formatação de Variáveis e Constantes  
- Utilizar espaçamentos adequados ao definir variáveis e constantes.  
- Seguir diretrizes para comentários, que devem ser claros e agregar valor ao código.  

## Indentação  
- Utilizar quatro espaços para indentação, evitando o uso de "Tab" para manter a consistência.  

## Comentários  
- Devem ser utilizados apenas quando necessários e seguir um padrão, seja com aspas simples ou duplas.  

## Uso do Black Formatter  
- O Black Formatter é uma extensão do VS Code que automatiza a formatação do código.  
- Ele mantém um código bem formatado, evita espaços desnecessários e melhora a indentação.  
- Passos:  
  1. Instalar o Black Formatter no VS Code.  
  2. Aplicar a formatação em arquivos como `main.py`, `routers_produtos.py`, `routers_usuarios.py`, etc.  
  3. Reorganizar manualmente as importações para seguir as convenções.  
  4. Garantir que o código termine com uma linha em branco, conforme a PEP 8.  

## Uso de Docstrings para Documentação  
- Docstrings são blocos de comentários utilizados para descrever funções e classes.  
- Elas explicam o propósito da função, seus argumentos e o retorno esperado.  
- Exemplos de aplicação:  
  - Em funções de rotas, como `criar_usuario()` e `listar_usuarios()`.  
  - Em funções como `criar_produto()` e `recomendar_produtos()`.  
- Projetos bem documentados podem não precisar de muitas docstrings, mas devem ser usadas quando agregam valor.  

A formatação e documentação adequadas são essenciais para a legibilidade e manutenção do código, facilitando o desenvolvimento e colaboração em equipe.