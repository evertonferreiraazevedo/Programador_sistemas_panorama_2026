def cont_vogais(texto):
    vogais = "aeiouAEIOU"
    count = 0
    for char in texto:
        if char in vogais:
            count += 1
    return count

texto = input("Digite um texto: ")
print("número vogais", cont_vogais(texto))