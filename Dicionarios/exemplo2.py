#como cadastrar uma pessoa em um dicionário
def cadastrar_pessoa():
    pessoa = {}
    pessoa["nome"] = input("Digite o nome da pessoa: ")
    pessoa["idade"] = int(input("Digite a idade da pessoa: "))
    pessoa["cidade"] = input("Digite a cidade da pessoa: ")
    pessoa["profissao"] = input("Digite a profissão da pessoa: ")
    return pessoa
#Criação da lista de pessoas
lista_de_pessoas_cadastradas = []
#cadastrando a primeira pessoa
pessoa = cadastrar_pessoa()
lista_de_pessoas_cadastradas.append(pessoa)
print(lista_de_pessoas_cadastradas)
#cadastrando a segunda pessoa
pessoa = cadastrar_pessoa()
lista_de_pessoas_cadastradas.append(pessoa)
print(lista_de_pessoas_cadastradas)
