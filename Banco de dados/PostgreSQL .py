import psycopg2

# Conectar ao servidor PostgreSQL (ajuste com as suas credenciais)
conexao = psycopg2.connect(
    host="localhost",
    port="5432",          # Porta padrão do PostgreSQL
    user="seu_usuario",
    password="sua_senha",
    database="nome_do_seu_banco"
)

cursor = conexao.cursor()

# Criar a tabela (No PostgreSQL usamos SERIAL para autoincremento e VARCHAR/TEXT)
cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos (
    ID SERIAL PRIMARY KEY,
    Nome VARCHAR(255),
    Idade INTEGER,
    Curso VARCHAR(255)
)''')

# Confirmar a alteração e fechar as conexões
conexao.commit()
cursor.close()
conexao.close()
