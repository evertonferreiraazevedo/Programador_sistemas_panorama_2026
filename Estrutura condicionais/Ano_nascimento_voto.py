#Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).
ano_nascimento = int(input("Digite o ano que vc nasceu: "))
idade_atual = 2026 - ano_nascimento
if idade_atual >= 16:
    print("Voce pode votar")
else: 
    print("Voto nao autorizado")