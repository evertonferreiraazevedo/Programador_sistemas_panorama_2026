import mysql.connector

# Conectar ao servidor MySQL (ajuste com as suas credenciais)
conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="nome_do_seu_banco"
)

cursor = conexao.cursor()

# Criar a tabela (No MySQL usamos VARCHAR para textos e INT para inteiros)
cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(255),
    Idade INT,
    Curso VARCHAR(255)
)''')

# Confirmar a alteração e fechar as conexões
conexao.commit()
cursor.close()
conexao.close()