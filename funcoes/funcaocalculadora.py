def menu():
    while True:
        print("""Escolha uma das opções abaixo:
            1 - Soma
            2 - Subtração
            3 - Multiplicação
            4 - Divisão
            5 - Sair""")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            n1, n2 = numeros()
            soma(n1, n2)
        elif opcao == "2":
            n1, n2 = numeros()
            subtracao(n1, n2)
        elif opcao == "3":
            n1, n2 = numeros()
            multiplicacao(n1, n2)
        elif opcao == "4":
            n1, n2 = numeros()
            divisao(n1, n2)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def soma(a, b):
    resultado = a + b
    print(f"O resultado da soma é: {resultado}")

def subtracao(a, b):
    resultado = a - b
    print(f"O resultado da subtração é: {resultado}")

def multiplicacao(a, b):
    resultado = a * b
    print(f"O resultado da multiplicação é: {resultado}")

def divisao(a, b):
    if b != 0:
        resultado = a / b
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")

def numeros():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    return n1, n2

menu()
