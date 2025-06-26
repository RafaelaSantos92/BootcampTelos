# criar estrutura de dados
produtos = {}
id_produto = 1 #Id inicial do produto

# Função para cadastrar um produto
def cadastrar_produto(nome, quantidade, preco):
    global id_produto
    produtos[id_produto] = {"nome": nome, "quantidade":quantidade, "preco":preco}
    print(f"Produto {nome} cadastrado com sucesso! ID: {id_produto}")
    id_produto += 1

# Função para listar Produtos
def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado")
        return
    print("\nEstoque: ")
    for id, dados in produtos.items():
        print(f"ID:{id}   |   Nome: {dados["nome"]}    |   quantidade: {dados["quantidade"]}   |   preco: {dados["preco"]} ")
        
# Função para alterar a quantidade do estoque
def alterar_quantidade():
    nome_produto = input("Qual o nome do produto você deseja alterar? ")
    for id, dados in produtos.items():
        if dados['nome'].lower() == nome_produto.lower():
            try:
                quantidade = int(input("Digite a quantidade para adicionar ao estoque: "))
                produtos[id]['quantidade'] += quantidade
                print(f"Estoque atualizado. Novo estoque de {dados['nome']}: {produtos[id]['quantidade']}")
            except ValueError:
                print("Quantidade inválida.")
            return
    print("Produto não cadastrado.")
        
# Função para aplicar desconto
def aplicar_desconto():
       nome_produto = input("Digite o nome do produto que deseja conceder o desconto: ")
       for id, dados in produtos.items():
        if dados['nome'].lower() == nome_produto.lower():
            try:
                desconto = float(input("Digite o valor do desconto (ex: 0.10 para 10%): "))
                produtos[id]['preco'] *= (1 - desconto)
                print(f"Desconto concedido com sucesso, Novo preço de {dados['nome']}: R${produtos[id]['preco']:.2f}")
            except ValueError:
                print("Produto não cadastrado")
                
# Função para verificar o total do estoque
def total_estoque():
    if not produtos:
        print("Produto não cadastrado")
        return
    
    valor_total = 0
    print("\nResumo do estoque:")
    for id, dados in produtos.items():
        valor_produto = dados['quantidade'] * dados['preco']
        valor_total += valor_produto
        print(f"{dados['nome']} (ID: {id}) -> {dados['quantidade']} x R${dados['preco']:.2f} = R${valor_produto:.2f}")
    print(f"\nValor total do estoque: R${valor_total:.2f}")
    
           
def menu():
    while True:
        print("\nMenu de controle de estoque")
        print("1. Cadastrar novo produto")
        print("2. Listar todos os produtos cadastrados")
        print("3. Alterar quantidade do estoque")
        print("4. Conceder desconto em produto")
        print("5. Consultar valor total do estoque")
        print("6. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: digite um número válido.")
            continue
        
        if opcao == 1:
            nome = input("Nome: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preco: "))
            cadastrar_produto(nome, quantidade, preco)
            
        elif opcao == 2:
            listar_produtos()
            
        elif opcao == 3:
            alterar_quantidade()
            
        elif opcao == 4:
            aplicar_desconto()
            
        elif opcao == 5:
            total_estoque()
            
        elif opcao == 6:
            print("Saindo do sistema!")
            break
        
        else:
            print("Erro, opção inválida!")

# Executar o menu
menu()