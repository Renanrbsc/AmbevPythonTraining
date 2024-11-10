# Exercicio 2 - Dicionario
# escreva um programa que leia os dados de 11 jogadores
# Jogador: Nome, posicao, numero, PernaBoa
# Crie um dicionario para armazenar os dados
# Imprima todos os jogadores e seus dados

print('Insira 11 Jogadores.')
time = [] # criando lista
for i in range(0,2): # loop for recebe dados

    jogador_inf = {'Nome': '','Posicao': '','Numero': '','PernaBoa': ''} # criando dicionario com colunas pre-estabelecidas

    jogador_inf['Nome'] = input(f'Digite o nome {i+1}:') # adicionando dados nas colunas 
    jogador_inf['Posicao'] = input(f'Digite o posicao {i+1}:') # adicionando dados nas colunas
    jogador_inf['Numero'] = input(f'Digite o Numero {i+1}:') # adicionando dados nas colunas
    jogador_inf['PernaBoa'] = input(f'Digite o PernaBoa {i+1}:') # adicionando dados nas colunas
    time.append(jogador_inf) # colocando dados de dicionario em um Array [{'','','',''},{'','','',''}]

for a in time: # loop for pra imprimir dados do array
    print(f"Nome:{a['Nome']}|Posicao:{a['Posicao']}|Numero:{a['Numero']}|PernaBoa:{a['PernaBoa']}")
















