# import tkinter as tk
# from tkinter import messagebox
# import random

# # Número secreto
# numero_secreto = random.randint(1, 10)

# # Função para verificar o palpite
# def verificar_palpite():
#     global numero_secreto
    
#     try:
#         palpite = int(entrada.get())

#         if palpite < numero_secreto:
#             resultado.config(text="O número é maior. Tente novamente.")
#         elif palpite > numero_secreto:
#             resultado.config(text="O número é menor. Tente novamente.")
#         else:
#             messagebox.showinfo("Parabéns!", "Você acertou o número!")
#             janela.destroy()  # Fecha a janela ao acertar

#         entrada.delete(0, tk.END)

#     except ValueError:
#         messagebox.showerror("Erro", "Digite apenas números!")

# # Criando janela
# janela = tk.Tk()
# janela.title("Jogo de Adivinhação")
# janela.geometry("400x250")

# # Título
# titulo = tk.Label(
#     janela,
#     text="Jogo de Adivinhação",
#     font=("Arial", 16)
# )
# titulo.pack(pady=10)

# # Texto explicativo
# texto = tk.Label(
#     janela,
#     text="Estou pensando em um número entre 1 e 10"
# )
# texto.pack()

# # Campo de entrada
# entrada = tk.Entry(janela, font=("Arial", 14))
# entrada.pack(pady=10)

# # Botão
# botao = tk.Button(
#     janela,
#     text="Enviar Palpite",
#     command=verificar_palpite
# )
# botao.pack()

# # Resultado
# resultado = tk.Label(
#     janela,
#     text="",
#     font=("Arial", 12)
# )
# resultado.pack(pady=20)

# # Executa a janela
# janela.mainloop()


import tkinter as tk
import random

# Função para gerar números
def gerar_numeros():
    numeros = random.sample(range(1, 61), 6)   # escolhe 6 números sem repetir
    numeros.sort()  # organiza em ordem crescente
    
    resultado.config(
        text=" - ".join(str(n) for n in numeros)
    )

# Criando janela
janela = tk.Tk()
janela.title("Gerador Mega-Sena")
janela.geometry("450x250")

# Título
titulo = tk.Label(
    janela,
    text="Gerador de Números da Mega-Sena",
    font=("Arial", 16)
)
titulo.pack(pady=20)

# Botão
botao = tk.Button(
    janela,
    text="Gerar Números",
    font=("Arial", 12),
    command=gerar_numeros
)
botao.pack(pady=20)

# Resultado
resultado = tk.Label(
    janela,
    text="Clique para gerar seus números",
    font=("Arial", 14)
)
resultado.pack(pady=20)

# Rodar aplicação
janela.mainloop()