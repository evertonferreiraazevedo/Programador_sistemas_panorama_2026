def contar_vogais_no_arquivo():
    nome_arquivo = input("Digite o nome do arquivo texto: ")
    vogais = "aeiouAEIOU"
    total_vogais = 0
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().lower()
            for caractere in conteudo:
                if caractere in vogais:
                    total_vogais += 1
        print(f"O arquivo possui {total_vogais} vogais.")
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado. Verifique o nome.")
contar_vogais_no_arquivo()
