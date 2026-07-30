import sqlite3

# Conectar e criar a tabela
conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT,
    Idade INTEGER,
    Curso TEXT
)''')
conexao.commit()


# 1. CREATE
def inserir_aluno():
    print("\nCadastrar Aluno")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")
    
    cursor.execute("INSERT INTO Alunos (Nome, Idade, Curso) VALUES (?, ?, ?)", (nome, idade, curso))
    conexao.commit()
    print("Aluno cadastrado com sucesso!")

# 2. READ (Listar)
def listar_alunos():
    print("\nLista de Alunos")
    cursor.execute("SELECT * FROM Alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Curso: {aluno[3]}")

# 2.1 READ (Pesquisar)
def pesquisar_aluno():
    print("\nPesquisar Aluno")
    print("1. Buscar por ID")
    print("2. Buscar por Nome")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        id_busca = int(input("Digite o ID: "))
        cursor.execute("SELECT * FROM Alunos WHERE ID = ?", (id_busca,))
        aluno = cursor.fetchone()
        if aluno:
            print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Curso: {aluno[3]}")
    elif opcao == "2":
        nome_busca = input("Digite o nome: ")
        cursor.execute("SELECT * FROM Alunos WHERE Nome LIKE ?", (f"%{nome_busca}%",))
        resultados = cursor.fetchall()
        for aluno in resultados:
            print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Curso: {aluno[3]}")

# 3. UPDATE
def atualizar_aluno():
    print("\nAtualizar Aluno")
    id_aluno = int(input("Digite o ID do aluno que deseja atualizar: "))
    
    novo_nome = input("Novo Nome: ")
    nova_idade = int(input("Nova Idade: "))
    novo_curso = input("Novo Curso: ")
    
    cursor.execute("UPDATE Alunos SET Nome = ?, Idade = ?, Curso = ? WHERE ID = ?", (novo_nome, nova_idade, novo_curso, id_aluno))
    conexao.commit()
    print("Dados atualizados com sucesso!")

# 4. DELETE
def deletar_aluno():
    print("\nDeletar Aluno")
    id_aluno = int(input("Digite o ID do aluno que deseja remover: "))
    
    cursor.execute("DELETE FROM Alunos WHERE ID = ?", (id_aluno,))
    conexao.commit()
    print("Aluno removido com sucesso!")

# Menu Principal
while True:
    print("\nSISTEMA DE ALUNOS")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Pesquisar")
    print("4. Atualizar")
    print("5. Deletar")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        inserir_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        pesquisar_aluno()
    elif opcao == "4":
        atualizar_aluno()
    elif opcao == "5":
        deletar_aluno()
    elif opcao == "0":
        conexao.close()
        print("Sistema encerrado.")
        break