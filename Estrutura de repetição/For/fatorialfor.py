numero = int(input("Qual fatorial voce quer? "))
resultado = 1
for i in range(1, numero + 1):
    resultado *= i

print(f"O fatorial de {numero} é {resultado}")