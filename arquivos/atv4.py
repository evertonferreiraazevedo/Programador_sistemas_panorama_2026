def substituir_caracter_arquivo():
    nome_arquivo = input("Digite o nome do arquivo texto: ")
    vogais = "aeiouAEIOU"
    novo_texto = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            for caractere in conteudo:
                if caractere in vogais:
                    novo_texto.append("*")
                else:
                    novo_texto.append(caractere)
        with open("novo_texto_subtituido.txt", "w", encoding='utf-8') as arquivo:
            arquivo.write(''.join(novo_texto))
            print("Novo arquivo criado com sucesso!")
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado. Verifique o nome.")

substituir_caracter_arquivo()
