#indice - valor
#chave - valor
lista = [1, 2, 3, 4, 5]
dicionario = {"primeiro": 1, "segundo": 2, "terceiro": 3, "quarto": 4, "quinto": 5}
lista.append(6)
dicionario["sexto"] = 6
lista.remove(3)
if "terceiro" in dicionario:
    print("A chave 'terceiro' está no dicionário.")
else:
    print("A chave 'terceiro' não está no dicionário.")


del dicionario["terceiro"]
lista[0] = 10
dicionario["primeiro"] = 10

# for i in lista:
#     print(i)

# for chave in dicionario:
#     print(chave, dicionario[chave])

if "terceiro" in dicionario:
    print("A chave 'terceiro' está no dicionário.")
else:
    print("A chave 'terceiro' não está no dicionário.")