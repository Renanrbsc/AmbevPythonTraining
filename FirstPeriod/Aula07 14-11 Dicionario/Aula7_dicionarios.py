# Aula 7 - 14-11-2019
# Dicionarios

lista = [] # Array
# dicionario = {chave:valor, chave:valor} # armazena valor com uma chave de acesso
dicionario = {'Nome':'Renan', 'Sobrenome':'Berti'} # chave entre aspas, valor sendo int ou str''  

print(dicionario) 
print(dicionario['Sobrenome'])

nome = 'Mirella'
lista_notas = [10,20,30,40]
media = sum(lista_notas)/ len(lista_notas) # sum funao de soma valores # len conta valores armazenados
situacao = 'Reprovado'
if media >= 7:
    situacao = 'Aprovado'
# armazenando 4 tipos de valores com chaves distintas
dicionario_alunos = {'Nome':nome, 'Lista_Notas':lista_notas,'Media':media, 'Situacao':situacao}

print(dicionario_alunos)
print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Situacao']}")

# criando um dicionario com uma coluna inicial
dicionario_bandas = {'Nome':''}
dicionario_bandas['Nome'] = 'Calipso' # adicionando valor
dicionario_bandas['Nome'] = 'Dejavu' # alterando valor

print(dicionario_bandas) # imprimindo dici

dicionario = {'Nome':'Renan','Sobrenome':'Berti'} # criando dicionario com dois campos adicionados
dicionario['Sobrenome'] = 'Rauen' # alterando valor
dicionario['CPF'] = '012.125.666-75' # adicionando coluna

print(dicionario)

lista_pessoas = [] # criando lista
for i in range(1,11): # loop for recebe dados
    dicionario_pessoa = {'Nome':'','Sobrenome':'','CPF':'','RG':''} # criando o dicionarios de dados 
    dicionario_pessoa['Nome'] = input(f'Digite o Nome {i}:') # criando coluna e adicionando dado
    dicionario_pessoa['Sobrenome'] = input(f'Digite o Sobrenome {i}:') # criando coluna e adicionando dado
    dicionario_pessoa['CPF'] = input(f'Digite o CPF {i}:') # criando coluna e adicionando dado
    dicionario_pessoa['RG'] = input(f'Digite o RG {i}:') # criando coluna e adicionando dado
    lista_pessoas.append(dicionario_pessoa) # adicionando dados de dicionario em uma lista [{'','','',''},{'','','',''}]


# imprimindo a lista
for a in lista_pessoas:
    print(a)

    
