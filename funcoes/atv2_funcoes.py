def media_lista(lista):
    return sum(lista) / len(lista)
lista = []
for i in range (4):
    numero = float(input("Digite um número: "))
    lista.append(numero)
print("A média é:", media_lista(lista))