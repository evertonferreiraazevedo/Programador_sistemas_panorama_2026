def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
    arquivo.close()

def adicionar_animal(nome_arquivo, animal):
    arquivo = open(nome_arquivo, "a")
    arquivo.write("\n" + animal)
    arquivo.close()

# Programa principal
nome_arquivo = "animais.txt"
ler_arquivo(nome_arquivo)

animal = input("\nDigite o nome de um animal: ")
adicionar_animal(nome_arquivo, animal)
print("\nArquivo atualizado:\n")
ler_arquivo(nome_arquivo)