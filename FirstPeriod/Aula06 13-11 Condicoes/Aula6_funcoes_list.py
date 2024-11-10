# Aula 6 - 13-11-19

# Lista - Array

# lista -> []

# variaveis numericas
var1 = 9
var2 = 0
var3 = 4

# Alguns tipos de Arrays
lista1 = []
lista2 = ['Marcela','Nicole', '*Matheus']
lista3 = [var1, var2, var3]
lista4 = [4, 9, 4, 6]

# imprimindo Arrays
print(lista1,lista2,lista3,lista4)

# função Append para adicionar Arrays e dados em lista ja criada - um por vez

lista1.append(lista2) # Append = funçao para adicionar dados em array
lista1.append(lista3) # Adicionando array dentro de array
lista1.append(input('Qual seu artista favorito?\n')) # Adicionando dado no array atraves do usuario

print(f'Lista com duas listas e dados individuais: {lista1} ')

# Array armazenando funcao de digitação
lista_pergunta = [str(input('Digite seu artista favorito:\n')), str(input('Digite seu Guitarrista favorito:\n')), int(input('Digite um numero: '))]
print(f'Array com os artistas e numero: {lista_pergunta}')

# Procurando um dado no Array
print(f'Array lista2: {lista2}')
posicao = int(input('Digite a posicao da lista2:\n '))
print( lista2[posicao-1]) # começa no 0, -1 diminui a posicao





