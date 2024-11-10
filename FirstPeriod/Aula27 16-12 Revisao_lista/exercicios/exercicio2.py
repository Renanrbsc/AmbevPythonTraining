# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como default ela irá criar 2 listas
# diferentes com 10 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10) # cria duas listas de 10 itens // copia a ultima lista criada 2 vezes // e embaralha

#print(lista)

# recebe o valor de cada lista em variaveis diferentes
a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.

lista = embaralhar(2,10,2)

#print(lista)
print(f'Listas por indice:\nlista[0] = {lista[0]}\nlista[1] = {lista[1]}\n')
print(f'Listas Endereco de memoria:\nID lista[0] = {id(lista[0])}\nID lista[1] = {id(lista[1])}\n')

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
print('1- Verificando se as listas sao copias ou unicas')
if lista[0] is lista[1]:
    print(f'Possuem mesmo endereco de memoria\nID[0] = {id(lista[0])}\nID[1] = {id(lista[1])}')
else:
    print('Nao Possuem mesmo endereco de memoria')

if lista[0] == lista[1]:
    print(f'Possuem mesmo valor\nValue[0] = {lista[0]}\nValue[1] = {lista[1]}')
else:
    print('Nao Possuem mesmo valor')
  
# 2) Qual é o maior valor destas duas listas 
print('\n2- Maior valor entre as duas listas')
if max(lista[0]) > max(lista[1]):
    print(f'lista[0] = {max(lista[0])}')

elif max(lista[1]) > max(lista[0]):
    print(f'lista[1] = {max(lista[1])}')
else:
    print(f'Maior valor é igual = {max(lista[1])}')

# 3) Qual é o maior valor de cada lista
print('\n3- Maior valor de cada lista')
print(f'lista[0] = {max(lista[0])}\nlista[1] = {max(lista[1])}\n')

# 4) Há o número 10 dentro da lista[0]?
print('\n4- Verificando se existe valor 10')
if 10 in lista[0]:
    print(f'contem {lista[0].count(10)} valor(s) 10')
else:
    print(f'Nao contem o valor 10')

# 5) Há o número 20 dentro da lista[1]?
print('\n5- Verificando se existe valor 20')
if 20 in lista[0]:
    print(f'contem {lista[0].count(20)} valor(s) 20')
else:
    print(f'Nao contem o valor 20')

# 6) Quantos números da lista[0] tem dentro da lista[1]?
print('\n6- Verificando se os valores da lista[0] existem na lista[1]')
i = 0
for j in lista[0]:
    if j in lista[1]:
        i += 1 
print(f'Existem {i} valores iguais nas listas')


# 7) Mostre os números da lista[0] que estão dentro da lista[1]
print('\n7- Verificando se os valores da lista[0] existem na lista[1]')
print(f'lista[0] = {lista[0]}\nlista[1] = {lista[1]}')
for i in lista[0]:
    if i in lista[1]:
        print(f'valor {i} da lista[0] Existe')
    else:
        print(f'valor {i} da lista[0] nao existe na lista[1]')

# 8) Mutliplique a soma da lista[0] com cada item da lista[1]
soma_lista = sum(lista[0])
print(f'\n8- A soma da lista[0] = {soma_lista}, multiplicada por indices da lista[1]')
for i in lista[1]:
    print(f'Indice {i}: {soma_lista * i}')
         

# 9) Faça uma divizão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
print(f'\n9- A soma do max e min das listas e vefificando se existe nas listas')
nova_lista = lista[0] + lista[1]
maior = max(nova_lista)
menor = min(nova_lista)
divisao_int = maior // menor
print(f'Lista\nMaior valor: {maior}\nMenor valor: {menor}\nDivisão inteira: {divisao_int}\n')
for i in range(2):
    print(f'Verificando na lista[{i}] a divisão: ')
    if divisao_int in lista[i]:
        print(f'A divisao inteira existe em lista[{i}]\n')
    else:
        print(f'A divisao inteira não existe em lista[{i}]\n')


# 10) Verifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]
print(f'10- A soma do max e min das listas e vefificando se existe nas listas')
maior = max(lista[0])
menor = min(lista[1])
print(f'Maior valor lista[0]: {maior}\nMenor valor lista[1]: {menor}')
print(f'Verificando valor maior lista[0] em lista[1]: ')
if maior in lista[1]:
    print(f'O valor maior existe em lista[1]\n')
else:
    print(f'O valor maior não existe em lista[1]\n')
print(f'Verificando valor menor lista[1] em lista[0]: ')
if menor in lista[0]:
    print(f'O valor menor existe em lista[0]\n')
else:
    print(f'O valor menor não existe em lista[0]\n')

