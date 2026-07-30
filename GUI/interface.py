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

import tkinter as tk
import sqlite3
janela = tk.Tk()
janela.title("Componentes Básicos")

#######################label nome e caixa de texto nome #########################

label_nome = tk.Label(janela, text="Digite seu nome:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

#######################label idade e caixa de texto idade #########################

label_idade = tk.Label(janela, text="Digite sua idade:")
label_idade.pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

#######################label idade e caixa de texto idade #########################

label_curso = tk.Label(janela, text="Digite seu curso:")
label_curso.pack()
entry_curso = tk.Entry(janela)
entry_curso.pack()



def exibir_nome():
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    curso = entry_curso.get()

    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Idade INTEGER,
        Curso TEXT
    )''')
    conexao.commit()
    cursor.execute("INSERT INTO Alunos (Nome, Idade, Curso) VALUES (?, ?, ?)", (nome, idade, curso))
    conexao.commit()


button = tk.Button(janela, text="Enviar", command=exibir_nome)
button.pack()

janela.mainloop()

