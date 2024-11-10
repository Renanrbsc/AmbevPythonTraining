#--- Exercicio 2  - Impressão de dados com a função Input
#--- Imprima o menu de uma aplicação de cadastro de pessoas
#--- O menu deve conter as opções de Cadastrar, Alterar, listar pessoas, alem da opção sair

'''
print('~'*25)
print('Escolha uma Opcao de Cadastro')
print('1 - Cadastrar novo')
print('2 - Alterar Cadastro')
print('3 - Listar Pessoas')
print('4 - Sair')
print('~'*25)
op = int(input('Digite a Opcao: '))
print(f'Opcao escolhida: {op}')
print('~'*25)
'''



nome = []
cond = True
while cond:
    print('~'*25)
    print('Escolha uma Opcao de Cadastro')
    print('1 - Cadastrar novo')
    print('2 - Alterar Cadastro')
    print('3 - Listar Pessoas')
    print('4 - Sair')
    op = int(input('Digite a Opcao: '))
    print('~'*25)

    if op == 1:
        print('1 - Cadastrar novo')
        nome.append(input('Digite nome de novo usuario: '))
        
        print(f'Usuario {nome} Cadastrado!')
    elif op == 2:
        print('2 - Alterar Cadastro')
        altera = input('Digite cadastro que deseja alterar: ')
        b = 0
        for c in nome:
            if nome[b] == altera:
                alteraNew = input('Digite nome de novo cadastro: ')
                nome[b] = alteraNew
                a = 1
                for i in nome:
                    print(f'Nome{a}: {i}')
                    a +=1
                print(f'Nome alterado com sucesso para: {alteraNew}')
            else:
                b +=1
    elif op == 3:
        print('Lista de Pessoas Cadastradas:')
        a = 1
        for i in nome:
            print(f'Nome{a}: {i}')
            a +=1
    elif op == 4:
        cond = False
    
        print(f'Cadastro foi fechado com sucesso!')






    



