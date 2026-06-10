#As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.
qnt_compradas = int(input("Quantas maças compradas: "))
if qnt_compradas < 12:
    valor_total = 0.3 * qnt_compradas
    print(f"Valor da compra R${valor_total:.2f}")
else:
    valor_total = 0.25 * qnt_compradas
    print(f"Valor da compra R${valor_total:.2f}")