import io
import os
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

# Configuração do Banco de Dados
conexa = sqlite3.connect("banco_imagens_real.db")
cursor = conexa.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS imagens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    arquivo_binario BLOB NOT NULL
                )"""
)
conexa.commit()

caminho_imagem_selecionada = ""


# Gerenciador de Telas (Alternância de Frames)
def mostrar_tela(frame_alvo):
    frame_cadastro.pack_forget()
    frame_listagem.pack_forget()
    frame_busca_direta.pack_forget()

    frame_alvo.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    if frame_alvo == frame_listagem:
        atualizar_tabela()


# Funções da Tela de Cadastro
def selecionar_imagem():
    global caminho_imagem_selecionada
    caminho = filedialog.askopenfilename(
        title="Selecione",
        filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif")],
    )
    if caminho:
        caminho_imagem_selecionada = caminho
        entry_caminho.delete(0, tk.END)
        entry_caminho.insert(0, os.path.basename(caminho))


def salvar_no_banco():
    nome = entry_nome.get().strip()
    if not nome or not caminho_imagem_selecionada:
        messagebox.showwarning(
            "Aviso", "Preencha o nome e selecione uma imagem!"
        )
        return

    try:
        with open(caminho_imagem_selecionada, "rb") as f:
            dados = f.read()

        cursor.execute(
            "INSERT INTO imagens (nome, arquivo_binario) VALUES (?, ?)",
            (nome, dados),
        )
        conexa.commit()

        entry_nome.delete(0, tk.END)
        entry_caminho.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Imagem salva!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Funções da Tela de Listagem Geral
def atualizar_tabela():
    for l in tabela.get_children():
        tabela.delete(l)

    cursor.execute("SELECT id, nome FROM imagens")
    for l in cursor.fetchall():
        tabela.insert("", tk.END, values=l)


# Função Genérica de Carregamento de Imagem para o Preview
def carregar_foto(tab, lbl, frm, idx_id, h):
    item = tab.selection()
    if not item:
        return

    id_img = tab.item(item)["values"][idx_id]
    try:
        cursor.execute(
            "SELECT nome, arquivo_binario FROM imagens WHERE id = ?", (id_img,)
        )
        res = cursor.fetchone()

        if res:
            nome_img = res[0]
            dados_binarios = res[1]

            fluxo = io.BytesIO(dados_binarios)
            img_pil = Image.open(fluxo)
            img_pil.thumbnail((500, h))
            img_tk = ImageTk.PhotoImage(img_pil)

            lbl.config(image=img_tk, text="")
            lbl.image = img_tk

            if frm:
                frm.config(text=f" Exibindo: {nome_img} ")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Funções da Tela de Pesquisa Direta
def executar_busca():
    texto = entry_busca.get().strip()
    if not texto:
        messagebox.showwarning("Aviso", "Digite um nome para pesquisar!")
        return

    for l in tabela_busca.get_children():
        tabela_busca.delete(l)

    lbl_resultado_foto.config(
        image="", text="Selecione um item da lista acima"
    )
    lbl_resultado_foto.image = None

    try:
        cursor.execute(
            "SELECT id, nome FROM imagens WHERE nome LIKE ?",
            (f"%{texto}%",),
        )
        resultados = cursor.fetchall()

        if resultados:
            for l in resultados:
                tabela_busca.insert("", tk.END, values=l)
        else:
            lbl_resultado_foto.config(text="Nenhuma imagem encontrada.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Configuração Principal da Janela
janela = tk.Tk()
janela.title("Painel Integrado de Imagens")
janela.geometry("650x650")
janela.resizable(False, False)

# Interface: Barra de Menus (Top Bar)
frame_menu = tk.Frame(janela, bd=1, relief=tk.RAISED)
frame_menu.pack(side=tk.TOP, fill=tk.X)

btn_menu_cad = tk.Button(
    frame_menu,
    text="Cadastrar Imagem ➕",
    command=lambda: mostrar_tela(frame_cadastro),
)
btn_menu_cad.pack(side=tk.LEFT, padx=5, pady=5)

btn_menu_lis = tk.Button(
    frame_menu,
    text="Ver Lista Geral 📂",
    command=lambda: mostrar_tela(frame_listagem),
)
btn_menu_lis.pack(side=tk.LEFT, padx=5, pady=5)

btn_menu_bus = tk.Button(
    frame_menu,
    text="Pesquisa Direta 🔍",
    command=lambda: mostrar_tela(frame_busca_direta),
)
btn_menu_bus.pack(side=tk.LEFT, padx=5, pady=5)

# Interface: Frame de Cadastro
frame_cadastro = tk.Frame(janela)

label_titulo = tk.Label(
    frame_cadastro, text="Cadastro de Fotos no Banco", font=("Arial", 14, "bold")
)
label_titulo.pack(pady=10)

label_nome = tk.Label(frame_cadastro, text="Nome da Imagem:")
label_nome.pack(anchor="w", pady=(10, 2))

entry_nome = tk.Entry(frame_cadastro, width=50)
entry_nome.pack(fill=tk.X, pady=2)

label_caminho = tk.Label(frame_cadastro, text="Arquivo Selecionado:")
label_caminho.pack(anchor="w", pady=(10, 2))

frame_caminho_aux = tk.Frame(frame_cadastro)
frame_caminho_aux.pack(fill=tk.X, pady=2)

entry_caminho = tk.Entry(frame_caminho_aux, width=35)
entry_caminho.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
entry_caminho.bind("<Key>", lambda e: "break")

btn_procurar = tk.Button(
    frame_caminho_aux, text="Procurar...", command=selecionar_imagem
)
btn_procurar.pack(side=tk.RIGHT)

btn_salvar = tk.Button(
    frame_cadastro,
    text="Salvar Imagem no Banco 💾",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    command=salvar_no_banco,
)
btn_salvar.pack(pady=20, ipady=5, fill=tk.X)

# Interface: Frame de Listagem Geral
frame_listagem = tk.Frame(janela)

lbl_instrucao = tk.Label(
    frame_listagem,
    text="Dê um duplo clique na linha para ver a imagem",
    font=("Arial", 10, "italic"),
)
lbl_instrucao.pack(pady=5)

tabela = ttk.Treeview(frame_listagem, columns=("id", "nome"), show="headings", height=6)
tabela.heading("id", text="ID")
tabela.heading("nome", text="Nome da Imagem")
tabela.column("id", width=80, anchor="center")
tabela.column("nome", width=480, anchor="w")
tabela.pack(pady=5, fill=tk.X)

frame_preview = tk.LabelFrame(frame_listagem, text=" Pré-visualização ")
frame_preview.pack(pady=10, fill=tk.BOTH, expand=True)
frame_preview.pack_propagate(False)

lbl_foto = tk.Label(frame_preview, text="Nenhuma imagem selecionada")
lbl_foto.pack(expand=True)

tabela.bind(
    "<Double-1>", lambda e: carregar_foto(tabela, lbl_foto, None, 0, 180)
)

# Interface: Frame de Pesquisa Direta
frame_busca_direta = tk.Frame(janela)

frame_topo_busca = tk.Frame(frame_busca_direta)
frame_topo_busca.pack(pady=10, fill=tk.X)

lbl_busca = tk.Label(
    frame_topo_busca, text="Buscar Nome:", font=("Arial", 10, "bold")
)
lbl_busca.pack(side=tk.LEFT, padx=(0, 5))

entry_busca = tk.Entry(frame_topo_busca, font=("Arial", 11))
entry_busca.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

btn_buscar = tk.Button(
    frame_topo_busca,
    text="Buscar 🔍",
    bg="#2196F3",
    fg="white",
    font=("Arial", 9, "bold"),
    command=executar_busca,
)
btn_buscar.pack(side=tk.RIGHT, padx=(5, 0))
entry_busca.bind("<Return>", lambda e: ejecutar_busca())

tabela_busca = ttk.Treeview(
    frame_busca_direta, columns=("id", "nome"), show="headings", height=4
)
tabela_busca.heading("id", text="ID")
tabela_busca.heading("nome", text="Resultados Encontrados")
tabela_busca.column("id", width=60, anchor="center")
tabela_busca.column("nome", width=500, anchor="w")
tabela_busca.pack(fill=tk.X, pady=5)

frame_foto_busca = tk.LabelFrame(
    frame_busca_direta, text=" Visualização do Resultado Selecionado "
)
frame_foto_busca.pack(pady=10, fill=tk.BOTH, expand=True)
frame_foto_busca.pack_propagate(False)

lbl_resultado_foto = tk.Label(
    frame_foto_busca, text="Busque um termo e clique no resultado para ver"
)
lbl_resultado_foto.pack(expand=True)

tabela_busca.bind(
    "&lt;&lt;TreeviewSelect&gt;&gt;",
    lambda e: carregar_foto(
        tabela_busca, lbl_resultado_foto, frame_foto_busca, 0, 220
    ),
)

# Inicialização do Aplicativo
mostrar_tela(frame_cadastro)
janela.mainloop()
conexa.close()
