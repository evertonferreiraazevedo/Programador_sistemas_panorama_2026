numeros = [10, 5, 8, 3, 12, 7, 4, 15]
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros[i] = 0

print(numeros)