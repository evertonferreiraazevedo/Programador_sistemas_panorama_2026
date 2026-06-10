idade = int(input("Qual a sua idade: "))
tem_titulo = input("Possui titulo de eleitor: ")

if idade >= 16 and tem_titulo =="sim":
    print("pode votar")
else:
    print("Não pode votar")