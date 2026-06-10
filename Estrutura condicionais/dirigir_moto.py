idade = int(input("Qual sua idade: "))
carta = input("Tem carteira? ")

if idade >=18 and (carta =="Sim" or carta =="s"):
    print("Pode pilotar")
else:
    print("Não Autorizado")