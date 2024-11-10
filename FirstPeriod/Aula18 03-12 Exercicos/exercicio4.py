# Aula 18 - 03-11-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

cerveja = (('marca', 'tipo', 'ibu', 'preço'),
           ('Skol', 'IPA', 'ultra-leve', 3.50),
           ('Brahma', 'lager', 'leve/media', 3.45),
           ('Kaiser', 'Americam Larger', 'leve', 2.35),
           ('Sol', 'larger mão', 'agua', 1.19)
           )
# for i in cerveja:

a = 1
for i in range(1, 5):
    print(
        f'{cerveja[0][0]}: {cerveja[a][0]}, {cerveja[0][1]}: {cerveja[a][1]}, {cerveja[0][2]}: {cerveja[a][2]}, {cerveja[0][3]}: {cerveja[a][3]}')
    a += 1


# 1.2 Crie uma função que receba esta tupla e devolva uma lista com um dicionários referenciando cada uma destas
# cervejas.

def criar_lista_dicio(cerveja):
    a = 1
    lista = []
    for i in range(1, 5):
        dicio = {'marca': cerveja[a][0], 'tipo': cerveja[a][1], 'ibu': cerveja[a][2], 'preco': cerveja[a][3]}
        lista.append(dicio)
        a += 1
    return lista


lista = criar_lista_dicio(cerveja)
for i in lista:
    print(f'{i}')
