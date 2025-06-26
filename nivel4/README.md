📦 Sistema de Controle de Estoque em Python

Este é um sistema simples de controle de estoque feito em Python.  
Ele permite cadastrar produtos, listar o estoque, atualizar quantidades, aplicar descontos e verificar o valor total em estoque.

🛠 Funcionalidades:

✅ Cadastro de produtos com nome, quantidade e preço.  
📋 Listagem de todos os produtos cadastrados.  
✏️ Alteração de quantidade em estoque.  
💸 Aplicação de desconto no preço de produtos.  
📊 Consulta do valor total do estoque.  
🚪 Opção de sair do sistema.



💻 Como usar:

Execute o script Python:  
ReatilCo.py

Use o menu interativo no terminal para navegar pelas opções disponíveis:

Menu de controle de estoque
1. Cadastrar novo produto
2. Listar todos os produtos cadastrados
3. Alterar quantidade do estoque
4. Conceder desconto em produto
5. Consultar valor total do estoque
6. Sair

Estrutura do Código:

produtos: Dicionário que armazena os produtos, onde a chave é o ID e o valor é um dicionário com nome, quantidade e preço.  
cadastrar_produto(nome, quantidade, preco): Cadastra um novo produto.  
listar_produtos(): Exibe todos os produtos cadastrados.  
alterar_quantidade(): Permite alterar a quantidade de um produto.  
aplicar_desconto(): Aplica um desconto percentual ao preço de um produto.  
total_estoque(): Calcula e mostra o valor total do estoque.  
menu(): Interface interativa no terminal.  

📌 Observações:

O sistema não utiliza banco de dados, todas as informações são armazenadas em memória (dicionário).  
O ID dos produtos é gerado automaticamente e incrementado a cada novo cadastro.  
O código usa entrada do usuário via input() e é ideal para fins de aprendizado ou pequenos testes em terminal.  

📄 Licença
Este projeto é de uso livre para fins educacionais.
