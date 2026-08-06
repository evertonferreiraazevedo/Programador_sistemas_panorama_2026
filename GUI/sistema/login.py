import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3

# Login admin (agora começam com esses valores, mas mudam ao cadastrar)
user_name = "admin"
senha_admin = "admin123"

# Variáveis globais para armazenar os campos de texto das telas
entry_usuario = None
entry_senha = None
entry_usuario_cadastro = None
entry_senha_cadastro = None
entry_senha_confirmar = None

#Cores Padrao
COR_FUNDO = "#FFFFFF"
COR_TEXTO = "#000000"
COR_BOTAO = "#4CAF50"
COR_BOTAO_TEXTO = "#000000"
COR_BOTAO_2 = "#ffa500"

#__________________________BANCO DE DADOS __________________________#
######################ALUNO############################

def buscar_aluno_banco():
    pass

def salvar_aluno_banco():
    pass

def atualizar_aluno_banco():
    pass

def deletar_aluno_banco():
    pass

######################ALUNO############################

######################ADMINISTRADOR############################

def salvar_admin_banco():
    pass

def atualizar_admin_banco():
    pass

def deletar_admin_banco():
    pass

######################ADMINISTRADOR############################

def conectar_banco():
    conexao = sqlite3.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ADMIN (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL
            )

        CREATE TABLE IF NOT EXISTS ALUNO (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
            )

        CREATE TABLE IF NOT EXISTS PROFESSOR (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
            )
        
        CREATE TABLE IF NOT EXISTS DISCIPLINA (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL
            )
        
        CREATE TABLE IF NOT EXISTS TURMA (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            curso_id INTEGER NOT NULL,
            aluno_id INTEGER NOT NULL,
            professor_id INTEGER NOT NULL,
            foreign key (aluno_id) references ALUNO(id),
            foreign key (professor_id) references PROFESSOR(id),
            FOREIGN KEY (curso_id) REFERENCES DISCIPLINA(id)
            )
        
        """)
    conexao.commit()
    conexao.close()

#__________________________BANCO DE DADOS __________________________#

#__________________________INTERFACE GRAFICA__________________________#
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
    # Usamos global para alterar o login padrão do sistema na memória
    global user_name, senha_admin

    usuario_novo = entry_usuario_cadastro.get()
    senha_nova = entry_senha_cadastro.get()
    confirmacao = entry_senha_confirmar.get()

    # Validação 1: Campos vazios
    if not usuario_novo or not senha_nova:
        messagebox.showwarning(
            "Cadastro", "Todos os campos devem ser preenchidos!")
        return

    # Validação 2: Verificar se as senhas batem
    if senha_nova != confirmacao:
        messagebox.showerror("Cadastro", "As senhas não coincidem!")
        return

    # Se passou nas validações, salva os novos dados de acesso
    user_name = usuario_novo
    senha_admin = senha_nova

    messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
    tela_login()

def tela_cadastro():
    # Informa ao Python que vamos modificar as variáveis globais nesta tela
    global entry_usuario_cadastro, entry_senha_cadastro, entry_senha_confirmar

    limpar_janela()
    janela.title("Cadastro")
    janela.geometry("300x350")

    # frame para a tela de cadastro
    frame_cadastro = tk.Frame(janela)
    frame_cadastro.pack(fill="both", expand=True)

    # Titulo da tela de cadastro
    label_titulo = tk.Label(
        frame_cadastro, text="Cadastro de Usuário", font=("Arial", 16))
    label_titulo.pack(pady=10)

    # Texto indicando que se deve inserir o usuario
    label_usuario = tk.Label(frame_cadastro, text="Usuário:")
    label_usuario.pack(pady=5)

    # Campo de entrada para usuario
    entry_usuario_cadastro = tk.Entry(frame_cadastro)
    entry_usuario_cadastro.pack(pady=5)

    # Texto indicando que se deve inserir a senha
    label_senha = tk.Label(frame_cadastro, text="Senha:")
    label_senha.pack(pady=5)

    # Campo de entrada para senha
    entry_senha_cadastro = tk.Entry(frame_cadastro, show="*")
    entry_senha_cadastro.pack(pady=5)

    # Texto indicando que se deve inserir a senha
    label_senha_confirmar = tk.Label(frame_cadastro, text="Confirmar Senha:")
    label_senha_confirmar.pack(pady=5)

    # Campo de entrada para senha
    entry_senha_confirmar = tk.Entry(frame_cadastro, show="*")
    entry_senha_confirmar.pack(pady=5)

    # criando botoes para fazer login e cadastrar
    frame_botoes = tk.Frame(frame_cadastro)
    frame_botoes.pack(pady=10)

    botao_cadastrar = tk.Button(frame_botoes, text="Cadastrar", command=fazer_cadastro, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO)
    botao_cadastrar.pack(side="left", pady=5, padx=10)

    botao_voltar = tk.Button(frame_botoes, text="Voltar", command=tela_login, bg=COR_BOTAO_2, fg=COR_BOTAO_TEXTO)
    botao_voltar.pack(side="right", pady=5, padx=10)

def tela_login():
    global entry_usuario, entry_senha

    limpar_janela()
    janela.title("Login")
    janela.geometry("300x250")

    # frame para a tela de login
    frame_login = tk.Frame(janela)
    frame_login.pack(fill="both", expand=True)

    # Titulo da tela de login
    label_titulo = tk.Label(
        frame_login, text="Sistema de Login", font=("Arial", 16))
    label_titulo.pack(pady=10)

    # Texto indicando que se deve inserir o usuario
    label_usuario = tk.Label(frame_login, text="Usuário:")
    label_usuario.pack(pady=5)

    # Campo de entrada para usuario
    entry_usuario = tk.Entry(frame_login)
    entry_usuario.pack(pady=5)

    # Texto indicando que se deve inserir a senha
    label_senha = tk.Label(frame_login, text="Senha:")
    label_senha.pack(pady=5)

    # Campo de entrada para senha
    entry_senha = tk.Entry(frame_login, show="*")
    entry_senha.pack(pady=5)

    # criando botoes para fazer login e cadastrar
    frame_botoes = tk.Frame(frame_login)
    frame_botoes.pack(pady=10)

    botao_login = tk.Button(frame_botoes, text="Login", command=fazer_login, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO)
    botao_login.pack(side="left", pady=5, padx=10)

    botao_cadastrar = tk.Button(
        frame_botoes, text="Cadastrar", command=tela_cadastro, bg=COR_BOTAO_2, fg=COR_BOTAO_TEXTO)
    botao_cadastrar.pack(side="right", pady=5, padx=10)


#__________________________INTERFACE GRAFICA__________________________#


# Criar janela principal
janela = tk.Tk()
janela.title("Login")
janela.geometry("300x250")
janela.resizable(False, False)
tela_login()
janela.mainloop()
