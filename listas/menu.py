convidados = []
while True:
    print("""================ Menu ===============
          1 - Adicionar convidado
          2 - listar convidados
          3 - Consultar convidados
          4 - Remover convidado
          5 - Quantidade de convidados
          6 - Editar convidado
          0 - Sair\n""")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        # Adicionar convidado
        convidados.append(input("Digite o nome do convidado: "))
    elif opcao == 2:
        # Listar convidados
        print("Lista de convidados:")
        for i in convidados:
            print(i)
    elif opcao == 3:
        nome = input("Digite o nome do convidado a ser consultado: ")
        if nome in convidados:
            print(f"{nome} está na lista de convidados.\n")
        else:
            print(f"{nome} não está na lista de convidados.\n")
    elif opcao == 4:
        nome = input("Digite o nome do convidado a ser removido: ")
        if nome in convidados:
            convidados.remove(nome)
            print(f"{nome} removido da lista de convidados.\n")
        else:
            print(f"{nome} não está na lista de convidados.\n")
    elif opcao == 5:
        print(f"Quantidade de convidados: {len(convidados)}\n") 
    elif opcao == 6:
        nome_antigo = input("Digite o nome do convidado a ser editado: ")
        if nome_antigo in convidados:
            nome_novo = input("Digite o novo nome do convidado: ")
            index = convidados.index(nome_antigo)
            convidados[index] = nome_novo
            print(f"{nome_antigo} foi atualizado para {nome_novo}.\n")
        else:
            print(f"{nome_antigo} não está na lista de convidados.\n")   
    elif opcao == 0:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
