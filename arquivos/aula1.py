# # 1. Abrindo o arquivo no modo de escrita ('w' de write)
# # Se o arquivo não existir, o Python cria ele automaticamente.
# arquivo = open("dados.txt", "w")

# # 2. Escrevendo dados dentro do arquivo
# # O '\n' serve para pular uma linha, organizando os dados.
# arquivo.write("Felipe\n")
# arquivo.write("Maria\n")
# arquivo.write("João\n")

# # 3. Fechando o arquivo
# # Muito importante para salvar as alterações no disco do computador.
# arquivo.close()

# print("Dados salvos com sucesso no arquivo dados.txt!")

##################################################################################

# # Abrindo um arquivo para leitura
# arquivo = open('exemplo.txt', 'r', encoding="utf-8")
# conteudo = arquivo.read()
# print(conteudo)
# arquivo.close()

#O arquivo a ser lido ficar na raiz da pasta que estiver aberta no VScode
###########################################################################################################
# Abrindo um arquivo para escrita
# arquivo = open('exemplo2.txt', 'w', encoding="utf-8")
# arquivo.write('Esta é uma nova linha de texto.\n')
# arquivo.write('Adicionando outra linha.')
# arquivo.close()
#conteudo antigo é sobrescrito 


###########################################################################################################
# # Abrindo um arquivo para escrita
# arquivo = open('exemplo2.txt', 'a', encoding="utf-8")
# arquivo.write('Esta é uma nova linha de texto.\n')
# arquivo.write('Adicionando outra linha.')
# arquivo.close()
# #conteudo antigo é sobrescrito 