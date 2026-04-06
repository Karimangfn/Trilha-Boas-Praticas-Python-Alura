# Tratamento de Erros, List Comprehensions e Testes em Python  

## Tratamento de Erros em Python  
- Utilização do `raise HTTPException` para levantar erros específicos, como usuário não encontrado ou histórico de compras indisponível.  
- Uso do bloco `try-except` para capturar e tratar erros, levantando exceções apropriadas.  
- Boas práticas:  
  - Validar informações antes do processamento para evitar múltiplos tratamentos de erro.  
  - Evitar uso excessivo de `try-except`, pois pode indicar necessidade de aprimoramento do código.  
  - Reservar `try-except` para erros oriundos de aplicações externas.  

## List Comprehension em Python  
- Permite criar listas de forma concisa utilizando `for` e `if` em uma única linha.  
- Seguir a PEP 8, que recomenda um limite de 79 caracteres por linha para melhor legibilidade.  
- Exemplos:  
  - Filtragem de produtos recomendados com base no histórico de compras e preferências do usuário.  
  - Uso recomendado para lógica simples e clara.  
  - Para lógica mais complexa (ex.: filtragem por tags), é preferível utilizar blocos tradicionais `for` e `if`.  
- Testar sempre o código após alterações para garantir funcionalidade e boas práticas.  

## Testes na Aplicação  
- Testes manuais realizados no terminal para verificar funcionalidades.  
- Passos seguidos:  
  1. Rodar o servidor com `uvicorn app.main:app --reload`.  
  2. Testar a criação de um produto via `POST` e validar a resposta com o ID gerado.  
  3. Verificar o produto criado utilizando `GET`.  
  4. Criar um usuário e adicionar histórico de compras.  
  5. Testar o endpoint de recomendação de produtos baseado no histórico de compras.  