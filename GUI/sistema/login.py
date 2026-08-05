import tkinter as tk
import tkinter.messagebox as messagebox
#login admin
user_name = "admin"
senha_admin = "admin123"

def limpar_janela():
    # Procura todos os widgets/frames dentro da janela e os destrói
    for widget in janela.winfo_children():
        widget.destroy()

def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == user_name and senha == senha_admin:
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

def fazer_cadastro():
    pass

def tela_cadastro():
    limpar_janela()
    janela.title("Cadastro")
    janela.geometry("300x350")
    #frame para a tela de cadastro
    frame_cadastro = tk.Frame(janela)
    frame_cadastro.pack(fill="both", expand=True)
    #Titulo da tela de cadastro
    label_titulo = tk.Label(frame_cadastro, text="Cadastro de Usuário", font=("Arial", 16))
    label_titulo.pack(pady=10)
    #Texto indicando que se deve inserir o usuario
    label_usuario = tk.Label(frame_cadastro, text="Usuário:")
    label_usuario.pack(pady=5)
    #Campo de entrada para usuario
    entry_usuario = tk.Entry(frame_cadastro)
    entry_usuario.pack(pady=5)
    #Texto indicando que se deve inserir a senha
    label_senha = tk.Label(frame_cadastro, text="Senha:")
    label_senha.pack(pady=5)
    #Campo de entrada para senha
    entry_senha = tk.Entry(frame_cadastro, show="*")
    entry_senha.pack(pady=5)
    #Texto indicando que se deve inserir a senha
    label_senha_confirmar = tk.Label(frame_cadastro, text="Confirmar Senha:")
    label_senha_confirmar.pack(pady=5)
    #Campo de entrada para senha
    entry_senha_confirmar = tk.Entry(frame_cadastro, show="*")
    entry_senha_confirmar.pack(pady=5)
    #criando botoes para fazer login e cadastrar
    frame_botoes = tk.Frame(frame_cadastro)
    frame_botoes.pack(pady=10) 
    botao_cadastrar= tk.Button(frame_botoes, text="Cadastrar", command=fazer_cadastro)
    botao_cadastrar.pack(side="left", pady=5, padx=10)
    botao_voltar = tk.Button(frame_botoes, text="Voltar", command=tela_login)
    botao_voltar.pack(side="right", pady=5, padx=10)

def tela_login():
    limpar_janela()
    janela.title("Login")
    janela.geometry("300x250")
    #frame para a tela de login
    frame_login = tk.Frame(janela)
    frame_login.pack(fill="both", expand=True)
    #Titulo da tela de login
    label_titulo = tk.Label(frame_login, text="Sistema de Login", font=("Arial", 16))
    label_titulo.pack(pady=10)
    #Texto indicando que se deve inserir o usuario
    label_usuario = tk.Label(frame_login, text="Usuário:")
    label_usuario.pack(pady=5)
    #Campo de entrada para usuario
    entry_usuario = tk.Entry(frame_login)
    entry_usuario.pack(pady=5)
    #Texto indicando que se deve inserir a senha
    label_senha = tk.Label(frame_login, text="Senha:")
    label_senha.pack(pady=5)

    #Campo de entrada para senha
    entry_senha = tk.Entry(frame_login, show="*")
    entry_senha.pack(pady=5)
    #criando botoes para fazer login e cadastrar
    frame_botoes = tk.Frame(frame_login)
    frame_botoes.pack(pady=10) 
    botao_login = tk.Button(frame_botoes, text="Login", command=fazer_login)
    botao_login.pack(side="left", pady=5, padx=10)
    botao_cadastrar = tk.Button(frame_botoes, text="Cadastrar", command=tela_cadastro)
    botao_cadastrar.pack(side="right", pady=5, padx=10)

#Criar janela principal
janela = tk.Tk()
janela.title("Login")
janela.geometry("300x250")
janela.resizable(False, False)
tela_login()
janela.mainloop()