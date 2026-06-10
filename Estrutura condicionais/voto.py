idade = int(input("Digite sua idade: "))
if idade <16:
    print("Não pode votar")
elif idade < 18:
    print("Facultativo")
elif idade < 70:
    print("Obrigado a votar")
else:
    print("Facultativo")