# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.
op = 's'
while (op) != 'n':
    while True:
        try:
            v1 = int(input('Digite o primeiro numero: '))            
        except ValueError:
            print('Voce digitou o numero errado, animal!\nDigite novamente!')
        else:
            while True:
                try:
                    v2 = int(input('Digite o segundo numero: '))
                except ValueError:
                    print('Voce digitou o numero errado, animal!\nDigite novamente!')
                else:
                    soma = v1 + v2
                    mul = v1 * v2
                    sub  = v1 - v2
                    while True:
                        try:
                            div = v1 / v2
                        except ZeroDivisionError:
                            print('Impossivel dividir por zero!\n Digite outro divisor!')
                            v2 = int(input('Digite o segundo numero: '))
                        else:
                            print(f'\nA soma é: {soma}\nA Multiplicação é: {mul}\nA Divisao é: {div:.2f}\nA Subtração é: {sub}\n')
                        break
                break        
        break     
    op = input('Deseja continuar? (s or n) ')

    
    