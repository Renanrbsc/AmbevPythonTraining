#--- Exercício 2 - For
#--- Escreva programa que leia um número inteiro
#--- Calcule a taboada do número informado
#--- Imprima a taboada com a conta completa (i * j)

num = int(input('Digite o numero da Tabuada:\n'))
print("\nTabuada do",num)
for j in range(1,11):
        print(f'{num} x {j} = {num*j}')

# Tabuada de 1 a 10
for i in range(1,11):
    print("\nTabuada do",i)
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')