#--- Exercicio 2  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um cliente
#--- Cliente: Nome, Sobrenome, ano de nascimento
#--- Exiba uma mensagem de boas vindas para o cliente
#--- Exiba um menu: Produtos alcoolicos e Produtos não alcoolicos, Sair
#--- Caso o cliente seja menor de idade o item 'produtos alcoolicos' não deve ser exibido
#--- Leia a opção digitada e crie uma tela para cada opção

nome = input('Digite seu Nome: ')
sobrenome = input('Digite seu Sobrenome: ')
anoNasc = int(input('Digite o ano de nascimento: '))
print(f'\nOlá {nome}{sobrenome},Seja bem vindo!')

idade = 2019 - anoNasc
i = 1

print('='*50,'\n'*2)
if idade >= 18:
    print(f'{i}-Produtos Alcoolicos')
    i+=1
print(f'{i}-Produtos Não Alcoolicos')
i+=1
print(f'{i}-Sair')
print(f'\n'*2,'='*50)

op = int(input('Digite uma opção: '))
if idade >=18:
    if op == 1:
        print(f'1-Produtos Alcoolicos')
        bebida = input('Digite a Marca da Bebida: ')
        print(f'Bebida selecionada - {bebida}')
    elif op == 2:
        print(f'1-Produtos Não Alcoolicos')
        bebida = input('Digite a Marca do Refrigerante: ')
        print(f'Refrigerante selecionado - {bebida}')
    elif op == 3:
        print('Menu fechado!')
    else:
        print('Opção não existe!')       
else:
    if op == 1:
        print(f'1-Produtos Não Alcoolicos')
        bebida = input('Digite a Marca do Refrigerante: ')
        print(f'Refrigerante selecionado - {bebida}')
    elif op == 2:
        print('Menu fechado!')
    else:
        print('Opção não existe!')




