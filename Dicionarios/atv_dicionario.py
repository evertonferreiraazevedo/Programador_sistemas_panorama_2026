dicionario_ingles = {
    "apple": "maçã",
    "car": "carro",
    "house": "casa",
    "dog": "cachorro",
    "cat": "gato",
    "book": "livro",
    "computer": "computador",
    "phone": "telefone",
    "table": "mesa",
    "chair": "cadeira",
    "window": "janela",
    "door": "porta",
    "water": "água",
    "food": "comida",
    "sun": "sol",
    "moon": "lua",
    "star": "estrela",
    "tree": "árvore",
}

def buscar_traducao(palavra):
    if palavra in dicionario_ingles:
        return dicionario_ingles[palavra]
    else:
        return "Palavra não encontrada no dicionário."
def adicionar_palavra(palavra, traducao):
    dicionario_ingles[palavra] = traducao
    print(f"Palavra '{palavra}' adicionada com sucesso!")
while True:
    print("\nDicionário Inglês-Português")
    print("1. Buscar tradução")
    print("2. Adicionar palavra")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        palavra_busca = input("Digite a palavra em inglês: ")
        traducao = buscar_traducao(palavra_busca)
        print(f"Tradução: {traducao}")
    elif opcao == "2":
        palavra_nova = input("Digite a palavra em inglês: ")
        traducao_nova = input("Digite a tradução em português: ")
        adicionar_palavra(palavra_nova, traducao_nova)
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")