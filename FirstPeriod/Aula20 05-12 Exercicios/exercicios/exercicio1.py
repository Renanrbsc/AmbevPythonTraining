# Aula 20 - 05-12-2019
# Lista com for e metodos

# Com esta lista:

lista = [
         ['codigo','produto','valor','quantidade'],
         [1,'Cevada',15.00,10],
         [2,'Lupulo',150.50,200],
         [3,'Malte',57.80,5000],
         [4,'Levedura 1',10.65,500],
         [5,'Extrato de Levedura',15.00,60],
         [6,'Levedura 2',15.50,87]
        ]

# 2.1 - Faça uma função que pegue esta lista e retorne uma lista com biblioteca.

def criar_dicio(lista):
    lista_dicio = []
    for i in range(1,7):
        dicio_produto = {lista[0][0]:lista[i][0],lista[0][1]:lista[i][1],lista[0][2]:lista[i][2],lista[0][3]:lista[i][3]}
        lista_dicio.append(dicio_produto)
    return lista_dicio
                
lista_dicio = criar_dicio(lista)
for i in lista_dicio:
    print(f'{i}')

# 2.2 - Faça outra função para consultar o preço através do código passado
# por parametro. Esta função deve printar o nome do produto, a quantidade
# e o preço.
# Execute esta função dentro do while e quando digitar qualquer código que 
# não tenha produto cadastrado o programa se encerra.



