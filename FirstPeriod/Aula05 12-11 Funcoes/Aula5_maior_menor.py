# Crie um programa que leia 4 notas
# imprima a maior nota
# imprima a menor nota
# imprima a media 
# imprima se o aluno foi aprovado ou reprovado(media 7.0

v1 = float(input('Digite a Primeira Nota:\n'))
v2 = float(input('Digite a Segunda Nota:\n'))
v3 = float(input('Digite a Terceira Nota:\n'))
v4 = float(input('Digite a Quarta Nota:\n'))

if (v1 >= v2 and v1 >= v3 and v1 >= v4):
    print(f'A Maior nota é: {v1}')
elif (v2 >= v1 and v2 >= v3 and v2 >= v4):
    print(f'A Maior nota é: {v2}')
elif (v3 >= v1 and v3 >= v2 and v3 >= v4):
    print(f'A Maior nota é: {v3}')
elif (v4 >= v1 and v4 >= v2 and v4 >= v3):
    print(f'A Maior nota é: {v4}')
else:
    print(f'As notas são iguais: {v1} {v2} {v3} {v4}') 

if (v1 <= v2 and v1 <= v3 and v1 <= v4):
    print(f'A Menor nota é: {v1}')
elif (v2 <= v1 and v2 <= v3 and v2 <= v4):
    print(f'A Menor nota é: {v2}')
elif (v3 <= v1 and v3 <= v2 and v3 <= v4):
    print(f'A Menor nota é: {v3}')
elif (v4 <= v1 and v4 <= v2 and v4 <= v3):
    print(f'A Menor nota é: {v4}')
else:
    print(f'As notas são iguais: {v1} {v2} {v3} {v4}') 

'''
lista = [v1,v2,v3,v4]
print('A maior nota foi:',max(lista))
lista = [v1,v2,v3,v4]
print('A menor nota foi:',min(lista))
'''

media = (v1+v2+v3+v4)/4
print(f'Media: {media}')

if media < 7:
    print(f'Reprovado!')
else:
    print(f'Aprovado!')






