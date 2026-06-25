vip = input("Cliente vip? ")
valor_compra = float(input("Valor da compra: "))
if vip == "sim" or valor_compra >= 100:
    print("Compra com desconto")
    print(valor_compra * 0.9)
else:
    print("Compra SEM desconto")
    print(valor_compra)