#Faça um programa que peça ao usuario uma senha e enquanto ele errar deve tentar novamente, se acerta deve da a mensagem de boas vindas

cont = 0
senha = input("Digite sua senha")
while True:
    if senha == "everton":
        print("Seja bem vindo")
        break
    else:
        cont = cont + 1
        if cont < 3:
            print("Acesso negado, voce tem: ", 3 - cont, "tentativas")
            senha = input("Tente novamente")
        else:
            print("Bloqueado, acabaram as tentativas :/ ")
            break
print("FIM")
