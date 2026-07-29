import sqlite3
import customtkinter as ctk
from tkinter import messagebox

# --- CONFIGURAÇÃO VISUAL ---
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

# --- FUNÇÕES DE BANCO DE DADOS ---
def conectar_banco():
    conn = sqlite3.connect("ficha_tecnica.db")
    conn.execute("PRAGMA foreign_keys = ON;")  # Garante a integridade dos relacionamentos
    return conn

def inicializar_banco():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        unidade_medida TEXT NOT NULL,
        preco_custo REAL NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS receitas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        rendimento_porcoes INTEGER NOT NULL,
        modo_preparo TEXT
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS receita_ingredientes (
        receita_id INTEGER,
        ingrediente_id INTEGER,
        quantidade REAL NOT NULL,
        PRIMARY KEY (receita_id, ingrediente_id),
        FOREIGN KEY (receita_id) REFERENCES receitas(id) ON DELETE CASCADE,
        FOREIGN KEY (ingrediente_id) REFERENCES ingredientes(id) ON DELETE CASCADE
    );
    """)
    conn.commit()
    conn.close()

# --- CLASSE PRINCIPAL ---
class AppFichaTecnica(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Ficha Técnica Pro")
        self.geometry("850x720")
        
        self.tabview = ctk.CTkTabview(self, width=810, height=680)
        self.tabview.pack(padx=20, pady=20)
        
        self.tab_ingredientes = self.tabview.add("1. Cadastrar Ingredientes")
        self.tab_receitas = self.tabview.add("2. Montar Receitas")
        self.tab_fichas = self.tabview.add("3. Fichas Técnicas e Custos")
        
        self.montar_aba_ingredientes()
        self.montar_aba_fichas()
        self.montar_aba_receitas()
        

    # --- ABA 1: GERENCIAR INGREDIENTES ---
    def montar_aba_ingredientes(self):
        ctk.CTkLabel(self.tab_ingredientes, text="Gerenciar Insumos e Ingredientes", font=("Arial", 18, "bold")).pack(pady=10)
        
        self.entry_ing_id = ctk.CTkEntry(self.tab_ingredientes, placeholder_text="ID (Apenas para Atualizar/Apagar)", width=350, fg_color="gray30")
        self.entry_ing_id.pack(pady=5)
        
        self.entry_ing_nome = ctk.CTkEntry(self.tab_ingredientes, placeholder_text="Nome do Ingrediente", width=350)
        self.entry_ing_nome.pack(pady=5)
        
        unidades_disponiveis = ["g (Grama)", "kg (Quilograma)", "ml (Mililitro)", "L (Litro)", "un (Unidade)", "maço", "caixa"]
        self.combo_ing_unidade = ctk.CTkComboBox(self.tab_ingredientes, values=unidades_disponiveis, width=350)
        self.combo_ing_unidade.pack(pady=5)
        self.combo_ing_unidade.set("g (Grama)")
        
        self.entry_ing_preco = ctk.CTkEntry(self.tab_ingredientes, placeholder_text="Preço de Custo unitário", width=350)
        self.entry_ing_preco.pack(pady=5)
        
        frame_botoes = ctk.CTkFrame(self.tab_ingredientes, fg_color="transparent")
        frame_botoes.pack(pady=10)
        
        ctk.CTkButton(frame_botoes, text="Adicionar", command=self.acao_salvar_ingrediente, fg_color="green", width=110).grid(row=0, column=0, padx=5)
        ctk.CTkButton(frame_botoes, text="Atualizar por ID", command=self.acao_atualizar_ingrediente, fg_color="orange", text_color="black", width=110).grid(row=0, column=1, padx=5)
        ctk.CTkButton(frame_botoes, text="Apagar por ID", command=self.acao_apagar_ingrediente, fg_color="red", width=110).grid(row=0, column=2, padx=5)
        
        self.txt_lista_ingredientes = ctk.CTkTextbox(self.tab_ingredientes, width=650, height=200)
        self.txt_lista_ingredientes.pack(pady=10)
        self.atualizar_lista_ingredientes()

    def acao_salvar_ingrediente(self):
        nome = self.entry_ing_nome.get().strip()
        unidade = self.combo_ing_unidade.get().split(" ")[0]
        preco = self.entry_ing_preco.get().strip()
        
        if not nome or not preco:
            messagebox.showwarning("Aviso", "Preencha Nome e Preço!")
            return
        try:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ingredientes (nome, unidade_medida, preco_custo) VALUES (?, ?, ?);", (nome, unidade, float(preco)))
            conn.commit()
            conn.close()
            self.limpar_campos_ingredientes()
            messagebox.showinfo("Sucesso", f"'{nome}' adicionado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {e}")

    def acao_atualizar_ingrediente(self):
        id_ing = self.entry_ing_id.get().strip()
        nome = self.entry_ing_nome.get().strip()
        unidade = self.combo_ing_unidade.get().split(" ")
        preco = self.entry_ing_preco.get().strip()
        
        if not id_ing or not nome or not preco:
            messagebox.showwarning("Aviso", "Para atualizar, preencha ID, Nome e Preço!")
            return
        try:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("UPDATE ingredientes SET nome=?, unidade_medida=?, preco_custo=? WHERE id=?;", (nome, unidade, float(preco), int(id_ing)))
            conn.commit()
            conn.close()
            self.limpar_campos_ingredientes()
            messagebox.showinfo("Sucesso", "Ingrediente atualizado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar: {e}")

    def acao_apagar_ingrediente(self):
        id_ing = self.entry_ing_id.get().strip()
        if not id_ing:
            messagebox.showwarning("Aviso", "Digite o ID do ingrediente!")
            return
        if messagebox.askyesno("Confirmar", "Apagar este ingrediente removerá ele de todas as receitas. Deseja continuar?"):
            try:
                conn = conectar_banco()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM ingredientes WHERE id=?;", (int(id_ing),))
                conn.commit()
                conn.close()
                self.limpar_campos_ingredientes()
                messagebox.showinfo("Sucesso", "Ingrediente deletado!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar: {e}")

    def limpar_campos_ingredientes(self):
        self.entry_ing_id.delete(0, 'end')
        self.entry_ing_nome.delete(0, 'end')
        self.entry_ing_preco.delete(0, 'end')
        self.atualizar_lista_ingredientes()
        self.atualizar_dropdown_ingredientes()

    def atualizar_lista_ingredientes(self):
        self.txt_lista_ingredientes.configure(state="normal")
        self.txt_lista_ingredientes.delete("1.0", "end")
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, unidade_medida, preco_custo FROM ingredientes;")
        for id_ing, nome, un, preco in cursor.fetchall():
            self.txt_lista_ingredientes.insert("end", f"ID: {id_ing} | {nome} ({un}) - R$ {preco:.4f}\n")
        conn.close()
        self.txt_lista_ingredientes.configure(state="disabled")
    # --- ABA 2: MONTAR RECEITAS (VÍNCULOS MULTIPLOS E LIVRES) ---
    def montar_aba_receitas(self):
        # Container dividido em duas colunas (Esquerda: Dados da Receita | Direita: Adicionar Insumos)
        self.tab_receitas.columnconfigure(0, weight=1)
        self.tab_receitas.columnconfigure(1, weight=1)

        # --- COLUNA ESQUERDA: CADASTRO E SELEÇÃO DA RECEITA ---
        frame_esquerda = ctk.CTkFrame(self.tab_receitas)
        frame_esquerda.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(frame_esquerda, text="Passo 1: Definir Receita", font=("Arial", 16, "bold")).pack(pady=10)
        
        self.entry_rec_id = ctk.CTkEntry(frame_esquerda, placeholder_text="ID da Receita (Para Atualizar/Apagar)", width=280, fg_color="gray30")
        self.entry_rec_id.pack(pady=5)

        self.entry_rec_nome = ctk.CTkEntry(frame_esquerda, placeholder_text="Nome da Receita (Ex: Bolo de Chocolate)", width=280)
        self.entry_rec_nome.pack(pady=5)
        
        self.entry_rec_rendimento = ctk.CTkEntry(frame_esquerda, placeholder_text="Rendimento (Quantidade de porções)", width=280)
        self.entry_rec_rendimento.pack(pady=5)
        
        self.entry_rec_preparo = ctk.CTkEntry(frame_esquerda, placeholder_text="Modo de Preparo resumido", width=280)
        self.entry_rec_preparo.pack(pady=5)

        # Botões da Receita Principal
        ctk.CTkButton(frame_esquerda, text="Gravar Base da Receita", command=self.acao_salvar_receita, fg_color="blue", width=240).pack(pady=5)
        ctk.CTkButton(frame_esquerda, text="Atualizar Base por ID", command=self.acao_atualizar_receita, fg_color="orange", text_color="black", width=240).pack(pady=5)
        ctk.CTkButton(frame_esquerda, text="Apagar Receita Completa", command=self.acao_apagar_receita, fg_color="red", width=240).pack(pady=5)

        # --- COLUNA DIREITA: ADICIONAR INGREDIENTES À RECEITA SELECIONADA ---
        frame_direita = ctk.CTkFrame(self.tab_receitas)
        frame_direita.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(frame_direita, text="Passo 2: Vincular Ingredientes", font=("Arial", 16, "bold")).pack(pady=10)
        
        ctk.CTkLabel(frame_direita, text="1. Selecione a Receita Alvo:", font=("Arial", 11)).pack(pady=2)
        self.combo_vinc_receita = ctk.CTkComboBox(frame_direita, values=["Nenhuma receita cadastrada"], width=280, command=self.atualizar_lista_insumos_venculados)
        self.combo_vinc_receita.pack(pady=5)

        ctk.CTkLabel(frame_direita, text="2. Escolha o Ingrediente a incluir:", font=("Arial", 11)).pack(pady=2)
        self.combo_ingredientes = ctk.CTkComboBox(frame_direita, values=["Nenhum ingrediente cadastrado"], width=280)
        self.combo_ingredientes.pack(pady=5)
        
        self.entry_rec_qtd = ctk.CTkEntry(frame_direita, placeholder_text="Quantidade (Ex: 250, 3, 1.5)", width=280)
        self.entry_rec_qtd.pack(pady=5)
        
        ctk.CTkButton(frame_direita, text="＋ Adicionar este Ingrediente", command=self.acao_vincular_ingrediente, fg_color="green", hover_color="darkgreen", width=240).pack(pady=10)

        # Mini monitor para ver o que já está na receita selecionada
        self.txt_itens_da_receita = ctk.CTkTextbox(frame_direita, width=280, height=130)
        self.txt_itens_da_receita.pack(pady=5)

        # Inicializa as listas suspensas
        self.atualizar_dropdown_ingredientes()
        self.atualizar_dropdown_receitas()

    def atualizar_dropdown_ingredientes(self):
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM ingredientes;")
        itens = [f"{id_ing} - {nome}" for id_ing, nome in cursor.fetchall()]
        conn.close()
        if itens:
            self.combo_ingredientes.configure(values=itens)
            self.combo_ingredientes.set(itens[0])

    def acao_salvar_receita(self):
        nome_rec = self.entry_rec_nome.get().strip()
        rendimento = self.entry_rec_rendimento.get().strip()
        preparo = self.entry_rec_preparo.get().strip()
        
        if not nome_rec or not rendimento:
            messagebox.showwarning("Aviso", "Preencha Nome e Rendimento para criar a base da receita!")
            return
            
        try:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO receitas (nome, rendimento_porcoes, modo_preparo) VALUES (?, ?, ?);", (nome_rec, int(rendimento), preparo))
            conn.commit()
            id_criado = cursor.lastrowid
            conn.close()
            
            messagebox.showinfo("Sucesso", f"Base da receita '{nome_rec}' criada!\nAgora adicione os ingredientes na coluna da direita.")
            self.limpar_campos_receitas()
            
            # Força o combobox da direita a selecionar a receita recém-criada
            item_selecao = f"{id_criado} - {nome_rec}"
            self.combo_vinc_receita.set(item_selecao)
            self.atualizar_lista_insumos_venculados()
            
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "O nome desta receita já existe.")
        except ValueError:
            messagebox.showerror("Erro", "Rendimento deve ser um número inteiro.")

    def acao_vincular_ingrediente(self):
        receita_sel = self.combo_vinc_receita.get()
        ing_sel = self.combo_ingredientes.get()
        qtd = self.entry_rec_qtd.get().strip()
        
        if receita_sel == "Nenhuma receita cadastrada" or ing_sel == "Nenhum ingrediente cadastrado" or not qtd:
            messagebox.showwarning("Aviso", "Selecione a receita, o ingrediente e informe a quantidade!")
            return
            
        try:
            id_receita = int(receita_sel.split(" - ")[0])
            id_ingrediente = int(ing_sel.split(" - ")[0])
            
            conn = conectar_banco()
            cursor = conn.cursor()
            
            # Insere ou atualiza a quantidade caso o ingrediente já tenha sido inserido antes nessa receita
            cursor.execute("""
                INSERT INTO receita_ingredientes (receita_id, ingrediente_id, quantidade) 
                VALUES (?, ?, ?)
                ON CONFLICT(receita_id, ingrediente_id) DO UPDATE SET quantidade = quantidade + excluded.quantidade;
            """, (id_receita, id_ingrediente, float(qtd)))
            
            conn.commit()
            conn.close()
            
            self.entry_rec_qtd.delete(0, 'end')
            self.atualizar_lista_insumos_venculados()
            self.atualizar_visualizador_fichas_externo()
            
        except ValueError:
            messagebox.showerror("Erro", "A quantidade precisa ser um número válido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao vincular: {e}")
    def acao_atualizar_receita(self):
        id_rec = self.entry_rec_id.get().strip()
        nome_rec = self.entry_rec_nome.get().strip()
        rendimento = self.entry_rec_rendimento.get().strip()
        preparo = self.entry_rec_preparo.get().strip()
        
        if not id_rec or not nome_rec or not rendimento:
            messagebox.showwarning("Aviso", "Para atualizar a base, insira o ID, Novo Nome e Rendimento!")
            return
            
        try:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("UPDATE receitas SET nome=?, rendimento_porcoes=?, modo_preparo=? WHERE id=?;", (nome_rec, int(rendimento), preparo, int(id_rec)))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Sucesso", "Base estrutural da receita atualizada!")
            self.limpar_campos_receitas()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar: {e}")

    def acao_apagar_receita(self):
        id_rec = self.entry_rec_id.get().strip()
        if not id_rec:
            messagebox.showwarning("Aviso", "Digite o ID da receita que deseja apagar!")
            return
            
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar permanentemente esta receita e todos os seus ingredientes vinculados?"):
            try:
                conn = conectar_banco()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM receitas WHERE id=?;", (int(id_rec),))
                conn.commit()
                conn.close()
                
                messagebox.showinfo("Sucesso", "Receita removida!")
                self.limpar_campos_receitas()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar: {e}")

    def limpar_campos_receitas(self):
        self.entry_rec_id.delete(0, 'end')
        self.entry_rec_nome.delete(0, 'end')
        self.entry_rec_rendimento.delete(0, 'end')
        self.entry_rec_preparo.delete(0, 'end')
        self.atualizar_dropdown_receitas()

    def atualizar_dropdown_receitas(self):
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM receitas;")
        itens = [f"{id_rec} - {nome}" for id_rec, nome in cursor.fetchall()]
        conn.close()
        
        if itens:
            self.combo_vinc_receita.configure(values=itens)
            self.combo_consultar_receitas.configure(values=itens)
        else:
            self.combo_vinc_receita.configure(values=["Nenhuma receita cadastrada"])
            self.combo_vinc_receita.set("Nenhuma receita cadastrada")
            self.combo_consultar_receitas.configure(values=["Nenhuma receita encontrada"])
            self.combo_consultar_receitas.set("Nenhuma receita encontrada")
            
        self.atualizar_lista_insumos_venculados()

    def atualizar_lista_insumos_venculados(self, escolha=None):
        self.txt_itens_da_receita.configure(state="normal")
        self.txt_itens_da_receita.delete("1.0", "end")
        
        receita_sel = self.combo_vinc_receita.get()
        if receita_sel == "Nenhuma receita cadastrada":
            self.txt_itens_da_receita.configure(state="disabled")
            return
            
        try:
            id_receita = int(receita_sel.split(" - "))
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT i.nome, ri.quantidade, i.unidade_medida 
                FROM receita_ingredientes ri
                JOIN ingredientes i ON ri.ingrediente_id = i.id
                WHERE ri.receita_id = ?;
            """, (id_receita,))
            
            linhas = cursor.fetchall()
            conn.close()
            
            self.txt_itens_da_receita.insert("end", "Ingredientes já vinculados:\n")
            for nome, qtd, un in linhas:
                self.txt_itens_da_receita.insert("end", f"• {nome}: {qtd} {un}\n")
        except Exception:
            pass
            
        self.txt_itens_da_receita.configure(state="disabled")

    # --- ABA 3: VISUALIZAR CUSTOS E VALOR VENAL ---
    def montar_aba_fichas(self):
        ctk.CTkLabel(self.tab_fichas, text="Visualizador de Fichas Técnicas e Custos", font=("Arial", 18, "bold")).pack(pady=10)
        
        ctk.CTkLabel(self.tab_fichas, text="Escolha uma receita salva para calcular:", font=("Arial", 12)).pack(pady=2)
        self.combo_consultar_receitas = ctk.CTkComboBox(self.tab_fichas, values=["Nenhuma receita encontrada"], width=400, command=self.carregar_dados_ficha)
        self.combo_consultar_receitas.pack(pady=5)
        
        self.frame_financeiro = ctk.CTkFrame(self.tab_fichas, width=600, height=80)
        self.frame_financeiro.pack(pady=10, fill="x", padx=40)
        
        self.lbl_custo_total = ctk.CTkLabel(self.frame_financeiro, text="Custo Total:\nR$ 0,00", font=("Arial", 13, "bold"))
        self.lbl_custo_total.grid(row=0, column=0, padx=20, pady=15)
        
        self.lbl_custo_porcao = ctk.CTkLabel(self.frame_financeiro, text="Custo p/ Porção:\nR$ 0,00", font=("Arial", 13, "bold"), text_color="orange")
        self.lbl_custo_porcao.grid(row=0, column=1, padx=20, pady=15)
        
        self.lbl_valor_venal = ctk.CTkLabel(self.frame_financeiro, text="Sugestão Venda:\nR$ 0,00", font=("Arial", 13, "bold"), text_color="green")
        self.lbl_valor_venal.grid(row=0, column=2, padx=20, pady=15)

        ctk.CTkLabel(self.tab_fichas, text="Ingredientes Utilizados e Subtotais:", font=("Arial", 11, "italic")).pack(pady=2)
        self.txt_detalhes_ficha = ctk.CTkTextbox(self.tab_fichas, width=600, height=180)
        self.txt_detalhes_ficha.pack(pady=5)

    def atualizar_visualizador_fichas_externo(self):
        # Atualiza a aba 3 caso ela esteja olhando para a receita modificada na aba 2
        try:
            self.carregar_dados_ficha()
        except Exception:
            pass

    def carregar_dados_ficha(self, escolha=None):
        texto_selecionado = self.combo_consultar_receitas.get()
        if texto_selecionado == "Nenhuma receita encontrada":
            return
            
        id_receita = int(texto_selecionado.split(" - ")[0])
        
        conn = conectar_banco()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, rendimento_porcoes, modo_preparo FROM receitas WHERE id = ?;", (id_receita,))
        rec_id_banco, rendimento, preparo = cursor.fetchone()
        
        cursor.execute("""
            SELECT 
                i.nome, 
                ri.quantidade, 
                i.unidade_medida, 
                i.preco_custo,
                (ri.quantidade * i.preco_custo) AS subtotal
            FROM receita_ingredientes ri
            JOIN ingredientes i ON ri.ingrediente_id = i.id
            WHERE ri.receita_id = ?;
        """, (id_receita,))
        
        itens = cursor.fetchall()
        conn.close()
        
        self.txt_detalhes_ficha.configure(state="normal")
        self.txt_detalhes_ficha.delete("1.0", "end")
        
        custo_total_receita = 0.0
        
        self.txt_detalhes_ficha.insert("end", f"ID da Receita: {rec_id_banco} | Modo de Preparo: {preparo}\n")
        self.txt_detalhes_ficha.insert("end", "-"*60 + "\n")
        
        for nome_ing, qtd, un, preco_un, subtotal in itens:
            custo_total_receita += subtotal
            self.txt_detalhes_ficha.insert(
                "end", 
                f"• {nome_ing}: {qtd} {un} x R$ {preco_un:.4f} = Subtotal: R$ {subtotal:.2f}\n"
            )
            
        self.txt_detalhes_ficha.configure(state="disabled")
        
        custo_por_porcao = custo_total_receita / rendimento if rendimento > 0 else 0
        valor_venal_sugerido = custo_por_porcao * 3.0 
        
        self.lbl_custo_total.configure(text=f"Custo Total:\nR$ {custo_total_receita:.2f}")
        self.lbl_custo_porcao.configure(text=f"Custo p/ Porção:\nR$ {custo_por_porcao:.2f}")
        self.lbl_valor_venal.configure(text=f"Sugestão Venda:\nR$ {valor_venal_sugerido:.2f}")


# --- INICIALIZAÇÃO DO PROGRAMA ---
if __name__ == "__main__":
    inicializar_banco()
    app = AppFichaTecnica()
    app.mainloop()
