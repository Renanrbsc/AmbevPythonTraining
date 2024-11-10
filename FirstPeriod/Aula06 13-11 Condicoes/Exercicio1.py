# Exercicio 1 - Lista
# Escreva programa que leia o nome de 10 alunos
# armazene os nomes em uma lista
# imprima a lista

nomes = []

print('Insira 10 nomes.')

for i in range(0,10):
    nomes.append(str(input(f'Digite o nome {i+1}:')))

print(f'A lista de nomes é: {nomes}')



