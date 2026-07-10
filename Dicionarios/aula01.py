# lista_frutas = ["maçã", "banana", "laranja", "uva", "pera"]
# dicionario_frutas = {
#     "maçã": "vermelha",
#     "banana": "amarela",
#     # "laranja": "Gol da argentina",
#     # "uva": "Uma fruta pequena, redonda e doce, geralmente usada para fazer vinho ",
#     # "pera": "Uma fruta verde, com polpa doce e aroma agradável."
#     }

# #print(lista_frutas[0])
# print(dicionario_frutas)
# print("*"*100)
# dicionario_frutas["jaca"] = "desagradável."
# print("*"*100)
# print(dicionario_frutas)
# del dicionario_frutas["banana"]
# print("*"*100)
# print(dicionario_frutas)
# del dicionario_frutas["banana"]
# print(dicionario_frutas)

# dicionario_frutas = {
#     "maçã": "vermelha",
#     "banana": "amarela",
#     "laranja": "Gol da argentina"}

# if "banana" in dicionario_frutas:
#     print("A banana está no dicionário.")
# else:
#     print("A banana não está no dicionário.")

# del dicionario_frutas["banana"]

# if "banana" in dicionario_frutas:
#     print("A banana está no dicionário.")
# else:
#     print("A banana não está no dicionário.")

# print(dicionario_frutas.keys())
# print(dicionario_frutas.values())
# print(dicionario_frutas.items())


# lista_frutas = ["maçã", "banana", "laranja", "uva", "pera"]
# dicionario_frutas = {
#     "maçã": "vermelha",
#     "banana": "amarela",
#     "laranja": "laranja",
#     "uva": "Roxa",
#     "pera": "verde"
# }

# # for fruta in lista_frutas:
# #     print(f"A {fruta} é boa")

# for chave_apontada in dicionario_frutas:
#         print(dicionario_frutas[chave_apontada])
    

# pessoa = {
#     "nome": "Everton",
#     "idade": 31,
#     "cidade": "Fortaleza",
#     "profissao": "Programador",
#     "altura": 1.95
# }

lista_pessoas = [
    {
        "nome": "Everton",
        "idade": 31,
        "cidade": "Fortaleza",
        "profissao": "Programador",
        "altura": 1.95
    },
    {
        "nome": "Maria",
        "idade": 25,
        "cidade": "São Paulo",
        "profissao": "Designer",
        "altura": 1.70
    },
    {
        "nome": "João",
        "idade": 40,
        "cidade": "Rio de Janeiro",
        "profissao": "Engenheiro",
        "altura": 1.80
    }
]

for pessoa in lista_pessoas: #pecorrer a lista de pessoas
    print (pessoa)