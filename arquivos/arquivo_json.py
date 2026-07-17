import json

# 1. Criando os dados estruturados (um dicionário com uma lista de usuários)
dados = {
    "usuarios": [
        {"nome": "Felipe", "idade": 25},
        {"nome": "Maria", "idade": 30},
        {"nome": "João", "idade": 22}
    ]
}

# 2. Abrindo o arquivo no modo de escrita ('w')
with open("dados.json", "w") as arquivo:
    # 3. Salvando os dados no formato JSON
    json.dump(dados, arquivo, indent=4)

print("Dados salvos com sucesso no arquivo dados.json!")
