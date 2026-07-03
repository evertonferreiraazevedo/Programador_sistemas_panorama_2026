soma_pares = 0
soma_impares = 0
for i in range(1, 51):
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i
print(f"A soma números pares é: {soma_pares}")
print(f"A soma números ímpares é: {soma_impares}")