
#--- Exercicio 1  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia dois números inteiros
#--- Realize as 4 operações matemáticas básicas com os números lidos
#--- Imprima os resultados das operações 
#--- Informe qual número é maior ou se os dois são iguais

a = int(input('Digite o numero 1: '))
b = int(input('Digite o numero 2: '))

z = a+b
x = a-b
c = a*b
v = a/b

print('~'*50)
print(f'A Soma com {a} e {b} é: {z}')
print(f'A Subtração com {a} e {b} é: {x}')
print(f'A Multiplicação com {a} e {b} é: {c}')
print(f'A Divisão com {a} e {b} é: {v:.2f}')
print('~'*50)
if a > b:
    print(f'O Primeiro valor é o maior. {a} > {b}')
elif a == b:
    print(f'Os dois valores são iguais. {a} = {b}')
else:
    print(f'O Segundo valor é o maior. {b} > {a}')
print('~'*50)