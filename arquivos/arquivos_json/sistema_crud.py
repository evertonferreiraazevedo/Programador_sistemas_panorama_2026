import json
lista_animais_cadastrados = []

def menu():
    while True:
        print("""Qual a sua opcao:
            1 - Cadastrar
            2 - Buscar
            3 - Listar
            4 - Atualizar
            5 - Deletar
            0 - Sair""")
        opcao = input("Qual a opcao desejada? ")

        if opcao == "1":
            cadastrar_animal()

        elif opcao == "2":
            buscar_animal()

        elif opcao == "3":
            listar_animais()

        elif opcao == "4":
            atualizar_animal()

        elif opcao == "5":
            apagar_animal()

        elif opcao == "0":
            print("Ate a proxima")
            break
        else:
            print("Opcao invalida!\n")

def cadastrar_animal():
    novo_animal = {}
    novo_animal["nome"] = input("Qual o nome do bicho? ")
    novo_animal["especie"] = input("Qual a especie do bicho? ")
    novo_animal["idade"] = float(input("Qual a idade do bicho? (em anos)"))
    lista_animais_cadastrados.append(novo_animal)
    

def buscar_animal():
    pass

def listar_animais():
    pass

def atualizar_animal():
    pass

def apagar_animal():
    pass

def ler_animais_json():
    with open("animais_cadastrados.json", "r") as arquivo:
        dados = json.load(arquivo)
        lista_animais_cadastrados = dados

def escrever_animais_json():
    with open("animais_cadastrados.json", "w") as arquivo:
        json.dump(lista_animais_cadastrados, arquivo, indent=4)


ler_animais_json()
menu()
escrever_animais_json()