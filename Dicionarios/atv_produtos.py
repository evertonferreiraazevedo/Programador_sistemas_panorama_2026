#Crie um dicionário que represente o estoque de uma loja, com produtos como chaves e quantidades em estoque como valores. Permita que o usuário insira um produto e verifique se ele está em estoque. Se estiver, informe a quantidade em estoque; caso contrário, informe que o produto não está disponível.
estoque = {
    "maçã": 10,
    "banana": 15,
    "laranja": 8,
    "uva": 12,
    "morango": 5
}

def verificar_estoque(produto):
    if produto in estoque:
        return f"O produto '{produto}' está em estoque com quantidade: {estoque[produto]}"
    else:
        return f"O produto '{produto}' não está disponível em estoque."

def adicionar_produto(produto, quantidade):
    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade
    print(f"Produto '{produto}' adicionado com sucesso com estoque: {estoque[produto]}")

while True:
    print("\nEstoque da Loja")
    print("1. Verificar estoque")
    print("2. Adicionar produto")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        produto_busca = input("Digite o nome do produto: ")
        resultado = verificar_estoque(produto_busca)
        print(resultado)

    elif opcao == "2":
        produto_novo = input("Digite o nome do produto: ")
        quantidade_nova = int(input("Digite a quantidade a ser adicionada: "))
        adicionar_produto(produto_novo, quantidade_nova)

    elif opcao == "3":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")