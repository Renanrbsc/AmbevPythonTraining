
def salvar_dicionario(pessoa_dicionario):
    arquivo_dic = open('TrabalhosPython/Aula15 28-11/cadastro_pessoa_dicionario.txt','a')
    arquivo_dic.write(f"{pessoa_dicionario['Nome']};{pessoa_dicionario['Sobrenome']};{pessoa_dicionario['Idade']}\n")
    arquivo_dic.close()

def ler_dicionario():
    lista = []
    arquivo_dic = open('TrabalhosPython/Aula15 28-11/cadastro_pessoa_dicionario.txt','r')
    for linha in arquivo_dic:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'Nome':lista_linha[0],'Sobrenome':lista_linha[1],'Idade':lista_linha[2]}
        lista.append(pessoa)
    arquivo_dic.close()
    return lista

nome = input('Digite o nome: ')
sobrenome = input('Digite o sobrenome: ')
idade = int(input('Digite o idade: '))

pessoa = {'Nome':nome,'Sobrenome':sobrenome,'Idade':idade}

salvar_dicionario(pessoa)
lista = ler_dicionario()
for i in lista:
    print(f"Nome: {i['Nome']} - Sobrenome: {i['Sobrenome']} - Idade: {i['Idade']}")