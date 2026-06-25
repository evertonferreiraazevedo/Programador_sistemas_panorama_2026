opcao = int(input("1 p/ ponte, 2 p/ tunel, escolha: "))
if opcao == 1:
    carro = input("Carro blindado? ")
    ponte = input("Ponte ok? ")
    if carro == "sim" and ponte =="sim":
        print("FUGA OK")
    else:
        print("Morte")
elif opcao == 2:
    mascara = input("Tem mascara? ")
    cartao = input("tem cartao? ")
    if mascara == "sim" and cartao =="sim":
        print("FUGA OK")
    else:
        print("Morte")
else:
    print("Opcao invalida, morreu!")