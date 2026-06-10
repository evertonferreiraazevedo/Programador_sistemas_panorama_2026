#Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas: •	para homens: (72.7 * Altura) – 58 •	para mulheres: (62.1 * Altura) – 44.7
altura = float(input("Digite sua Altura: "))
sexo = int(input("Digite 1 p/ feminino ou 2 p/ masculino"))
if sexo == 1:
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideia é: {peso_ideal:.2f}")
else:
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideia é: {peso_ideal:.2f}")