# # numero = 10
# lista_vazia = []
# print(lista_vazia)

# lista_numeros = [10, 20, 30, 40, 50]
# print(lista_numeros)
# # print(lista_numeros[0])
# # print(lista_numeros[1])
# # print(lista_numeros[-1])

# lista_numeros[0] = 100
# print(lista_numeros)
# print(lista_numeros[0:3])
# print(lista_numeros[2:])
# print(lista_numeros[:3])
# print(lista_numeros[-5:-2])

# lista_letras = ['a', 'b', 'c', 'd', 'e']
# print(lista_letras)
# print(lista_letras[0])
# lista_letras[0] = 'z'
# print(lista_letras)
# lista_letras[0:1] = ['x', 'y']
# print(lista_letras)


# cliente = ['João', 'Maria', 'José', 'Ana']
# # print(cliente)
# # cliente.append('mirela')
# # print(cliente)
# # nome = input('nome do cliente: ')
# # cliente.append(nome)
# print(cliente)
# for i in range(3):
#     nome = input('nome do cliente: ')
#     cliente.append(nome)
# print(cliente)


# lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# print("Tamanho da lista:", len(lista)) # Saída: Tamanho da lista: 10
# print("Soma dos elementos:", sum(lista)) # Saída: Soma dos elementos: 39
# print("Menor elemento:", min(lista)) # Saída: Menor elemento: 1
# print("Maior elemento:", max(lista)) # Saída: Maior elemento: 9
# print("Lista ordenada:", sorted(lista)) # Saída: Lista ordenada: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# lista_palavras = ["banana", "abacaxi", "laranja", "uva", "maçã"]

# # Utilizando todas as funções dentro do print
# print("Tamanho da lista:", len(lista_palavras), 
#    "\nLista de palavras:", lista_palavras,
#    "\nMenor palavra (lexicograficamente):", min(lista_palavras), 
#    "\nMaior palavra (lexicograficamente):", max(lista_palavras), 
#    "\nLista ordenada:", sorted(lista_palavras))
lista = [1, 2, 5 , 6 , 78, 5 ,55 , 3, 4, 5]
# Adicionando elementos com .append(), .insert() e .extend()
# lista.append(6) # adiciona 6 ao final da lista
# lista.insert(0, 0) # insere 0 na posição 0
# lista.extend([7, 8, 9]) # adiciona os elementos 7, 8, 9 ao final da lista

# Removendo elementos com .remove(), .pop() e .clear()
#lista.remove(5) # remove o elemento 5
elemento_removido = lista.pop(2) # remove o elemento na posição 2 e retorna o valor removido
# lista.clear() # limpa a lista completamente
print(lista)
print("Elemento removido:", elemento_removido)