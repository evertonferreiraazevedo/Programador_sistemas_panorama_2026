def contar_caracter_arquivo():
    nome_arquivo = input("Digite o nome do arquivo texto: ")
    vogais = input("Digite o caracter a ser buscado no arquivo: ")
    total_caracter = 0
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().lower()
            for caractere in conteudo:
                if caractere in vogais:
                    total_caracter += 1
        print(f"O arquivo possui {total_caracter} vogais.")
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado. Verifique o nome.")
contar_caracter_arquivo()
