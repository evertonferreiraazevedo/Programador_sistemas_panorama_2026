import json
aluno = {
    "nome": "Everton",
    "idade": 30,
    "curso": "Programador de Sistemas"
}

with open("aluno.json", "w") as arquivo:
    json.dump(aluno, arquivo, indent=8)
