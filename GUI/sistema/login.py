import tkinter as tk
import tkinter.messagebox as messagebox

def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == user_name and senha == senha_admin:
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")
#login admin
user_name = "admin"
senha_admin = "admin123"

#Criar janela principal
janela = tk.Tk()
janela.title("Login")
janela.geometry("300x250")
janela.resizable(False, False)
#Titulo da tela de login
label_titulo = tk.Label(janela, text="Sistema de Login", font=("Arial", 16))
label_titulo.pack(pady=10)
#Texto indicando que se deve inserir o usuario
label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.pack(pady=5)
#Campo de entrada para usuario
entry_usuario = tk.Entry(janela)
entry_usuario.pack(pady=5)
#Texto indicando que se deve inserir a senha
label_senha = tk.Label(janela, text="Senha:")
label_senha.pack(pady=5)

#Campo de entrada para senha
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack(pady=5)
#criando botao para fazer login
botao_login = tk.Button(janela, text="Login", command=fazer_login)
botao_login.pack(pady=10)
janela.mainloop()