convidados = []

while True:
    print("""================ Menu ===============
          1 - Adicionar convidado
          2 - listar convidados
          3 - Consultar convidados
          4 - Remover convidado
          5 - Quantidade de convidados
          0 - Sair\n""")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        while True:
            nome = input("Digite o nome do convidado (ou 'sair' para voltar ao menu): ")
            if nome.lower().replace(" ", "") == 'sair':
                break
            elif nome in convidados:
                print(f"{nome} já está na lista de convidados.\n")
            else:
                convidados.append(nome)
                print(f"{nome} adicionado à lista de convidados.\n")
    elif opcao == 2:
        print("Lista de convidados:")
        if not convidados:
            print("Nenhum convidado na lista.\n")
        else:
            for convidado in convidados:
                print(convidado)
        print()
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
    elif opcao == 0:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.\n")

