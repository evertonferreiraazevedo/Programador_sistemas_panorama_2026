comb = float(input("Quantidade de combustivel: "))
atm = input("Atmosfera respiravel ? ")
traje = float(input("Qual integridade do traje? "))

if comb >= 15 and (atm == "boa" or traje == 100):
    print("Pouso autorizado")
else:
    print("Nao autorizado")