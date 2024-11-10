# Aula 3 - 18-11-2019

if 'Teti'.count('t') > 0:
    print('Existe "t" em "Teti"')
if 'e' in 'Teti':
    print('Existe "e" em "Teti"')
if 'M' not in 'Teti':
    print('Nao existe "M" em "Teti"')
else:
    print('Nao existe')

lista_nomes = ['renan','gabriel']
lista_vazia = []

if len(lista_vazia) == 0:
    print('Vazio')
else:
    print('Nao Existe')

nome = ''
if nome:
    print('Preenchido')
else:
    print('Vazia')

if lista_nomes:
    print('Tem nomes')
