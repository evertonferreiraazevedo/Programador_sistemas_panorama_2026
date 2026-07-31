# import tkinter as tk
# # Criação da janela principal
# janela = tk.Tk()
# janela.title("Olá, Tkinter!")
# janela.geometry("800x600+100+100")
# janela.resizable(False, False)

# # Rótulo simples
# label = tk.Label(janela, text="Bem-vindo ao Tkinter!", bg="red")
# label2 = tk.Label(janela, text="Lorem ipsum dolor sit amet.", bg="blue")
# label.pack(side=tk.RIGHT, padx=10, pady=10)
# label2.pack(side=tk.LEFT, padx=10, pady=10)
# # Início do loop principal
# janela.mainloop()


import sqlite3
import tkinter as tk

def inicializar_banco_de_dados():
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            curso TEXT NOT NULL
        )
    """
    )

    conexao.commit()
    conexao.close()

def salvar_dados_do_aluno():
    nome_digitado = campo_nome.get()
    idade_digitada = campo_idade.get()
    curso_digitado = campo_curso.get()

    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Alunos (nome, idade, curso) VALUES (?, ?, ?)" , (nome_digitado, idade_digitada, curso_digitado))

    conexao.commit()
    conexao.close()

    campo_nome.delete(0, tk.END)
    campo_idade.delete(0, tk.END)
    campo_curso.delete(0, tk.END)
    print("Aluno cadastrado com sucesso!")


inicializar_banco_de_dados()
janela = tk.Tk()
janela.title("Sistema de Cadastro Escolar")
janela.geometry("300x300")  

texto_nome = tk.Label(janela, text="Nome Completo:")
texto_nome.pack(pady=2)  
campo_nome = tk.Entry(janela, width=30)
campo_nome.pack(pady=5)

texto_idade = tk.Label(janela, text="Idade:")
texto_idade.pack(pady=2)
campo_idade = tk.Entry(janela, width=30)
campo_idade.pack(pady=5)

texto_curso = tk.Label(janela, text="Curso:")
texto_curso.pack(pady=2)
campo_curso = tk.Entry(janela, width=30)
campo_curso.pack(pady=5)

botao_enviar = tk.Button(
    janela, text="Cadastrar Aluno", command=salvar_dados_do_aluno
)
botao_enviar.pack(pady=15)

janela.mainloop()
