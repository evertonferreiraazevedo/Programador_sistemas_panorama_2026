import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# ==========================================
# PALETA DE CORES (DESIGN BONITINHO)
# ==========================================
COR_FUNDO = "#F4F6F9"  # Cinza bem claro moderno
COR_CARD = "#FFFFFF"  # Branco para os painéis
COR_TEXTO = "#0542BB"  # Cinza escuro para leitura confortável
COR_PRIMARIA = "#1E3A8A"  # Azul escuro elegante (Botões principais)
COR_SUCESSO = "#10B981"  # Verde esmeralda (Salvar)
COR_ALERTA = "#F59E0B"  # Laranja suave (Editar)
COR_PERIGO = "#EF4444"  # Vermelho moderno (Excluir)
COR_TEXTO_BOTAO = "#FFFFFF"  # Texto branco nos botões
COR_NEUTRA = "#FFFFFF"  # Branco para elementos neutros
COR_NEUTRA2 = "#E2E2E2"

user_admin = "admin"
user_senha = "admin123"

###################################BANCO DE DADOS###################################
conexao = sqlite3.connect("sistema.db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")
conexao.commit()
conexao.close()
###################################BANCO DE DADOS###################################


###################################Navegar Telas###################################
def efetuar_login():
    usuario = ent_login_user.get()
    senha = ent_login_senha.get()

    if usuario == user_admin and senha == user_senha:
        # Limpa os campos de login por segurança
        ent_login_user.delete(0, tk.END)
        ent_login_senha.delete(0, tk.END)
        
        # Muda para a tela de menu
        tela_login.pack_forget()
        tela_menu.pack(fill="both", expand=True)
    else:
        messagebox.showerror("Erro de Autenticação", "Usuário ou senha incorretos!")

def realizar_logout():
    tela_menu.pack_forget()
    tela_login.pack(fill="both", expand=True)

def ir_para_menu():
    tela_cadastro.pack_forget()
    tela_visualizacao.pack_forget()
    tela_menu.pack(fill="both", expand=True)

def ir_para_cadastro():
    tela_menu.pack_forget()
    tela_cadastro.pack(fill="both", expand=True)

def ir_para_visualizacao():
    tela_menu.pack_forget()
    # Recarrega os dados do banco na tabela toda vez que abre a tela
    for item in tabela.get_children():
        tabela.delete(item)

    conexao = sqlite3.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    for i, linha in enumerate(cursor.fetchall()):
        # Adiciona a linha alternando a cor de fundo (efeito zebrado)
        tag = "par" if i % 2 == 0 else "impar"
        tabela.insert("", "end", values=linha, tags=(tag,))
    conexao.close()

    tela_visualizacao.pack(fill="both", expand=True)

###################################Navegar Telas###################################

###################################CRUD###################################
def salvar():
    nome = ent_nome.get()
    email = ent_email.get()

    if not nome or not email:
        messagebox.showwarning("Aviso", "Preencha tudo!")
        return

    conexao = sqlite3.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()
    ent_nome.delete(0, tk.END)
    ent_email.delete(0, tk.END)
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    #ir_para_menu()

def deletar():
    selecionado = tabela.selection()
    if not selecionado:
        return
    id_user = tabela.item(selecionado, "values")[0]
    conexao = sqlite3.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_user,))
    conexao.commit()
    conexao.close()
    ir_para_visualizacao()  # Atualiza a tela

def editar():
    selecionado = tabela.selection()
    if not selecionado:
        return

    id_user = tabela.item(selecionado, "values")[0]
    nome_atual = tabela.item(selecionado, "values")[1]
    email_atual = tabela.item(selecionado, "values")[2]

    novo_nome = simpledialog.askstring(
        "Editar Nome", "Novo nome:", initialvalue=nome_atual
    )
    if novo_nome is None:
        return

    novo_email = simpledialog.askstring(
        "Editar E-mail", "Novo e-mail:", initialvalue=email_atual
    )
    if novo_email is None:
        return

    if not novo_nome.strip() or not novo_email.strip():
        messagebox.showwarning("Aviso", "Os campos não podem ficar vazios!")
        return

    conexao = sqlite3.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
        (novo_nome.strip(), novo_email.strip(), id_user),
    )
    conexao.commit()
    conexao.close()

    ir_para_visualizacao()

###################################CRUD###################################

###################################Construção Telas###################################
janela = tk.Tk()
janela.title("Gerenciador CRUD")
janela.geometry("550x450")
janela.resizable(False, False)
janela.configure(bg=COR_FUNDO)

# Estilização da Tabela (ttk.Treeview)
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("Treeview.Heading", font=("Arial", 14, "bold"), background=COR_PRIMARIA, foreground=COR_NEUTRA)
estilo.configure("Treeview", rowheight=28, font=("Arial", 10))

# Criação das 4 telas com fundo personalizado
tela_login = tk.Frame(janela, bg=COR_FUNDO)
tela_menu = tk.Frame(janela, bg=COR_FUNDO)
tela_cadastro = tk.Frame(janela, bg=COR_FUNDO)
tela_visualizacao = tk.Frame(janela, bg=COR_FUNDO)

# --- DESIGN: TELA LOGIN ---
card_login = tk.Frame(tela_login, bg=COR_NEUTRA2, padx=30, pady=30, bd=1, relief="solid")
card_login.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(card_login, text="ACESSO AO SISTEMA", font=("Arial", 14, "bold"), bg=COR_NEUTRA2, fg=COR_PRIMARIA).pack(pady=(0, 20))

tk.Label(card_login, text="Usuário:", font=("Arial", 10), bg=COR_NEUTRA2).pack(anchor="w")
ent_login_user = tk.Entry(card_login, font=("Arial", 11), width=30, bd=1, relief="groove", highlightthickness=0)
ent_login_user.pack(pady=(5, 15))

tk.Label(card_login, text="Senha:", font=("Arial", 10), bg=COR_NEUTRA2).pack(anchor="w")
# O parâmetro show="*" esconde os caracteres digitados
ent_login_senha = tk.Entry(card_login, font=("Arial", 11), width=30, bd=1, relief="groove", highlightthickness=0, show="*")
ent_login_senha.pack(pady=(5, 20))

tk.Button(card_login, text="Entrar", font=("Arial", 10, "bold"), command=efetuar_login, bg=COR_PRIMARIA,
          fg=COR_TEXTO_BOTAO, width=25, height=2, relief="flat").pack(pady=5)

# --- DESIGN: TELA MENU ---
tk.Label(tela_menu, text="MENU PRINCIPAL", font=("Arial", 28, "bold"), bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=40)
tk.Button(tela_menu, text="Cadastrar Novo", font=("Arial", 11), command=ir_para_cadastro, bg=COR_PRIMARIA,
          fg=COR_TEXTO_BOTAO, width=20, height=2, relief="flat").pack(pady=10)
tk.Button(tela_menu, text="Visualizar Registros", font=("Arial", 11), command=ir_para_visualizacao,
          bg=COR_PRIMARIA, fg=COR_TEXTO_BOTAO, width=20, height=2, relief="flat").pack(pady=10)
tk.Button(tela_menu, text="Sair / Logout", font=("Arial", 10), command=realizar_logout,
          bg=COR_PERIGO, fg=COR_TEXTO_BOTAO, width=15, relief="flat").pack(pady=30)

# --- DESIGN: TELA CADASTRO ---
card_cadastro = tk.Frame(tela_cadastro, bg=COR_NEUTRA2, padx=30, pady=30, bd=1, relief="solid")
card_cadastro.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(card_cadastro, text="CADASTRO", font=("Arial", 16, "bold"), bg=COR_NEUTRA2, fg=COR_PRIMARIA).pack(pady=(0, 20))

tk.Label(card_cadastro, text="Nome:", font=("Arial", 10), bg=COR_NEUTRA2).pack(anchor="w")
ent_nome = tk.Entry(card_cadastro, font=("Arial", 11), width=30, bd=1, relief="groove", highlightthickness=0)
ent_nome.pack(pady=(5, 15))

tk.Label(card_cadastro, text="E-mail:", font=("Arial", 10), bg=COR_NEUTRA2).pack(anchor="w")
ent_email = tk.Entry(card_cadastro, font=("Arial", 11), width=30, bd=1, relief="groove", highlightthickness=0)
ent_email.pack(pady=(5, 20))

tk.Button(card_cadastro, text="Salvar Usuário", font=("Arial", 10, "bold"), command=salvar, bg=COR_SUCESSO,
          fg=COR_TEXTO_BOTAO, width=25, height=2, relief="flat").pack(pady=5)

tk.Button(card_cadastro, text="Voltar ao Menu", font=("Arial", 10), command=ir_para_menu, bg=COR_ALERTA,
          fg=COR_TEXTO_BOTAO, width=25, relief="flat").pack(pady=5)

# --- DESIGN: TELA VISUALIZAÇÃO ---
tk.Label(tela_visualizacao, text="LISTA DE REGISTROS", font=("Arial", 16, "bold"), bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=15)

tabela = ttk.Treeview(tela_visualizacao, columns=("id", "nome", "email"), show="headings")
tabela.heading("id", text="ID")
tabela.heading("nome", text="Nome")
tabela.heading("email", text="E-mail")

tabela.column("id", width=50, anchor="center")
tabela.column("nome", width=170, anchor="w")
tabela.column("email", width=270, anchor="w")

# Configura cores alternadas para a tabela
tabela.tag_configure("par", background=COR_NEUTRA)
tabela.tag_configure("impar", background=COR_NEUTRA2)
tabela.pack(fill="both", expand=True, padx=20)

frame_botoes = tk.Frame(tela_visualizacao, bg=COR_FUNDO)
frame_botoes.pack(pady=20)

tk.Button(frame_botoes, text="Editar", font=("Arial", 10, "bold"), command=editar, bg=COR_ALERTA, fg=COR_TEXTO_BOTAO,
          width=10, height=1, relief="flat").pack(side="left", padx=8)

tk.Button(frame_botoes, text="Excluir", font=("Arial", 10, "bold"), command=deletar, bg=COR_PERIGO, fg=COR_TEXTO_BOTAO,
          width=10, height=1, relief="flat").pack(side="left", padx=8)

tk.Button(frame_botoes, text="Voltar", font=("Arial", 10), command=ir_para_menu, bg=COR_SUCESSO, fg=COR_TEXTO_BOTAO,
          width=10, height=1, relief="flat").pack(side="left", padx=8)

# Inicia mostrando apenas a tela de login
tela_login.pack(fill="both", expand=True)
janela.mainloop()
