from random import randint

aleatorio = randint(1,1000)
print('Digite um numero entre 1 e 1000')
i=0

while (aleatorio):    
    numero = int(input('Digite um numero: '))

    if aleatorio == numero:
        print('Voce acertou!')
        break    
    elif aleatorio > numero:
        print('O numero é maior!')
        i +=1
        if i == 5:
            print('Deseja ver a resposta? (y/n)')
            opcao = input()
            if opcao == 'y':
                print(f'O valor aleatorio foi:{aleatorio}')
                break
    elif aleatorio < numero:
        print('O numero é menor!')
        i +=1
        if i == 5:
            print('Deseja ver a resposta? (y/n)')
            opcao = input()
            if opcao == 'y':
                print(f'O valor aleatorio foi:{aleatorio}')
                break



