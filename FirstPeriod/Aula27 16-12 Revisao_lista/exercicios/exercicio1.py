# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int

from random import randint

lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,50))


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print(f'1- Tamanho de listas:\n lista1: {len(lista1)}\nTamanho lista2: {len(lista2)}\nTamanho lista3: {len(lista3)}\n')


# 1.2) Qual é o maior valor da lista2?
print(f'2- Maior valor lista1: {max(lista1)}\nMaior valor lista2: {max(lista2)}\nMaior valor lista3: {max(lista3)}\n')


# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
print(f'3- A soma max e min da lista 2 é: {sum([max(lista2),min(lista2)])}\n')

# 1.4) Qual é a média aritmética da lista1?
print(f'4- A media aritmetica da lista 2 é: {sum(lista1) / len(lista1):.2f}\n')


# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
print(f'5- A soma das listas:\nLista1 - {sum(lista1)}\nLista2 - {sum(lista2)}\nLista3 - {sum(lista3)}\nTodas - {sum([sum(lista1), sum(lista2), sum(lista3)])}\n')


# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
print(f'6- Valores da lista1: ')
for i in lista1:
    print(f'- {i}')

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
print(f'7- Mostrando valores de posição nas listas')
try:
    print(f'Valores Lista1: ')
    print(f'Posicao 5: {lista1[4]}\nPosicao 9: {lista1[8]}\nPosicao 10: {lista1[9]}\nPosicao 25: {lista1[24]}\n')
except IndexError:
    print('Erro de Index!\n')
try:
    print(f'Valores Lista2: ')
    print(f'Posicao 5: {lista2[4]}\nPosicao 9: {lista2[8]}\nPosicao 20: {lista2[9]}\nPosicao 25: {lista2[24]}\n')
except IndexError:
    print('Erro de Index!\n')
try:
    print(f'Valores Lista3: ')
    print(f'Posicao 5: {lista3[4]}\nPosicao 9: {lista3[8]}\nPosicao 10: {lista3[9]}\nPosicao 25: {lista3[24]}\n')
except IndexError:
    print('Erro de Index!\n')


# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
print(f'8- Lista com maior quantidade de itens.')
if len(lista1) > len(lista2) and len(lista1) > len(lista3):
    print(f'lista1: {len(lista1)}\n')
elif len(lista2) > len(lista1) and len(lista2) > len(lista3):
    print(f'lista2: {len(lista2)}\n')
elif len(lista3) > len(lista2) and len(lista3) > len(lista1):
    print(f'lista3: {len(lista3)}\n')

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.
print(f'9- Soma dos maximos e subtração pelo menor valor dos menores. ')
min_1 = min(lista1)
min_2 = min(lista2)
min_3 = min(lista3)
print(f'valor minimo de cada lista: 1- {min_1} , 2- {min_2}, 3- {min_3}\nMenor das listas: ')
if min_1 < min_2 and min_1 < min_3:
    print(f'lista1: {min_1}\n')
    menor_valor = min_1
elif min_2 < min_1 and min_2 < min_3:
    print(f'lista2: {min_2}\n')
    menor_valor = min_2
elif min_3 < min_1 and min_3 < min_2:
    print(f'lista3: {min_3}\n')
    menor_valor = min_3

print(f'Soma dos maximos - menor valor: {sum([max(lista1),max(lista2),max(lista3)]) - menor_valor}\n')

# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas
print(f'10- Somando maior com menor valor das listas : ')
listas = lista1 + lista2 + lista3

max_listas = max(listas)
min_listas = min(listas)

print(f'Soma do max e min: {sum([max_listas,min_listas])}\n')






