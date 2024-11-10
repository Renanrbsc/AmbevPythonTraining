#Aula 4
#Fazer um programa que leia dois numeros 
#Realize as 4 operaçoes matematicas
#Imprima o resultado das operaçoes
#Diga qual numero é o maior 

print('~'*50)
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print('~'*50)


mul = valor1 * valor2
print('A Multiplicação de: {} * {} é: {}'.format(valor1,valor2,mul))

div = valor1 / valor2
print('A Divisão de: {} / {} é: {:.3f}'.format(valor1,valor2,div))

sub = valor1 - valor2
print(f'A Subtração de: {valor1} - {valor2} = {sub}')

print(f'Soma: {valor1} + {valor2} = {valor1 + valor2}')

print('~'*50)
if valor1 > valor2:
    print('O Primeiro valor é o maior. {} > {}'.format(valor1,valor2))
elif valor1 == valor2:
    print(f'Os dois valores são iguais. {valor1} = {valor2}')
else:
    print(f'O Segundo valor é o maior. {valor2} > {valor1}')
print('~'*50)


s = input('Digite uma frase: ')
print(f'a frase: {s} tem',len(s),'caracteres')






