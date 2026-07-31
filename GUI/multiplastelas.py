# import tkinter as tk

# def abrir_nova_janela():
#     nova_janela = tk.Toplevel()
#     nova_janela.title("Nova Janela")
#     label = tk.Label(nova_janela, text="Esta é uma nova janela")
#     label.pack(pady=20)

# root = tk.Tk()
# root.title("Janela Principal")

# botao = tk.Button(root, text="Abrir Nova Janela", command=abrir_nova_janela)
# botao.pack(pady=20)
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title("Janela Principal")

# def sair():
#     root.destroy()

# def mostrar_mensagem():
#     tk.messagebox.showinfo("Mensagem", "Você clicou no botão!")

# botao_sair = tk.Button(root, text="Sair", command=sair)
# botao_sair.pack(pady=10)

# botao_mensagem = tk.Button(root, text="Mostrar Mensagem", command=mostrar_mensagem)
# botao_mensagem.pack(pady=10)
# root.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.title("Interface com Frame")

# frame = tk.Frame(root, borderwidth=2, relief="sunken")
# frame.pack(padx=10, pady=10)

# label = tk.Label(frame, text="Este é um frame!")
# label.pack(padx=5, pady=5)

# button = tk.Button(frame, text="Clique aqui")
# button.pack(padx=5, pady=5)

# root.mainloop()

import tkinter as tk

def mudar():
    if tela1.winfo_viewable():
        tela1.pack_forget()
        tela2.pack(fill="both", expand=True)
    else:
        tela2.pack_forget()
        tela1.pack(fill="both", expand=True)

janela = tk.Tk()

tela1 = tk.Frame(janela,  bg="red")
tk.Label(tela1, text="Tela 1").pack()
tk.Button(tela1, text="Mudar", command=mudar).pack()

tela2 = tk.Frame(janela)
tk.Label(tela2, text="Tela 2").pack()
tk.Button(tela2, text="Mudar", command=mudar).pack()

tela1.pack(fill="both", expand=True)

janela.mainloop()
