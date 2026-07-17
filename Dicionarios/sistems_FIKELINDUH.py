clientes = {
    "12345678901": 
        {"nome": "Ana Silva", 
         "idade": 28, 
         "compras": [120.50, 89.90, 45.00], 
         "categoria": "VIP"
         },
    "98765432100": 
        {"nome": "Bruno Costa", 
         "idade": 34, 
         "compras": [350.00, 500.00], 
         "categoria": "Premium"
         },
    "45678912344": 
        {"nome": "Carla Souza", 
         "idade": 22, 
         "compras": [50.00], 
         "categoria": "Regular"
         },
    "78912345655": 
    {"nome": "Diego Lima", 
     "idade": 41, 
     "compras": [15.00, 30.00, 25.50, 40.00], 
     "categoria": "Regular"
     }
}
def cadastrar_cliente():
    #Captura o CPF para usar como chave principal)
    cpf_chave = input("Digite o CPF do cliente: ")
    #Cria um dicionário para os dados do cliente
    novo_cliente = {}
    novo_cliente["nome"] = input("Digite o nome do cliente: ")
    novo_cliente["idade"] = int(input("Digite a idade do cliente: ")) 
    novo_cliente["compras"] = []
    novo_cliente["categoria"] = "Regular" 
    #Associa CPF aos Dados do Cliente no banco global
    clientes[cpf_chave] = novo_cliente
    print(f"Cliente {novo_cliente['nome']} cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    
    print("\nLista de Clientes:")
    for cpf, dados in clientes.items():
        print(f"""CPF: {cpf}, 
    Nome: {dados['nome']}, 
    Idade: {dados['idade']}, 
    Categoria: {dados['categoria']}, 
    Compras: {dados['compras']}
    faturamento {sum(dados['compras'])} \n""")

def buscar_cliente(cpf_busca):
    if cpf_busca in clientes:
        dados = clientes[cpf_busca]
        print(f"Cliente encontrado: {dados['nome']}")
        return dados
    else:
        print("Cliente não encontrado.")
        return False

def atualizar_cliente():
    cpf_atualizar = input("Digite o CPF do cliente que deseja Atualizar: ")
    cliente = buscar_cliente(cpf_atualizar)
    if cliente:
        cliente["nome"] = input("Digite o nome do cliente: ")
        cliente["idade"] = int(input("Digite a idade do cliente: ")) 
        print(f"Cliente {cliente['nome']} atualizado com sucesso!")
   
def excluir_cliente():
    cpf_deletar = input("Digite o CPF do cliente que deseja Deletar: ")
    cliente = buscar_cliente(cpf_deletar)
    if cliente:
        del clientes[cpf_deletar]
        print("Cliente excluido com sucesso!")

def calcular_faturamento_cliente():
    cpf_cliente = input("Digite o CPF do cliente que deseja calcular o faturamento: ")
    cliente = buscar_cliente(cpf_cliente)
    if cliente:
        faturamento = sum(cliente["compras"])
        print(f"Faturamento total do cliente {cliente["nome"]} é R$ {faturamento:.2f}")

def fazer_compra():
    cpf_cliente = input("Digite o CPF do cliente que deseja fazer a compra: ")
    cliente_compra = buscar_cliente(cpf_cliente)

    if cliente_compra:
        valor_compra = float(input("Digite o valor da Compra: "))
        cliente_compra["compras"].append(valor_compra)
        verificar_status_cliente(cliente_compra)

def verificar_status_cliente(cliente):
    faturamento = sum(cliente["compras"])
    if faturamento >= 100:
        cliente["categoria"] = "Vip"
        print(f"Categoria de {cliente["nome"]} atualizado para {cliente["categoria"]}.")

while True:
    print("\nSistema de Gerenciamento de Clientes FIKELINDUH")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente")
    print("4. Atualizar cliente")
    print("5. Excluir cliente")
    print("6. Fazer compra")
    print("7. Faturamento cliente")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        cpf_cliente = input("Digite o CPF do cliente que deseja buscar: ")
        buscar_cliente(cpf_cliente)
    elif opcao == "4":
        atualizar_cliente()
    elif opcao == "5":
        excluir_cliente()
    elif opcao == "6":
        fazer_compra()
    elif opcao == "7":
        calcular_faturamento_cliente()
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")