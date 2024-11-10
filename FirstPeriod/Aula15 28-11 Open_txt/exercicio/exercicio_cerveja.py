
def salvar_dic(cerveja_dicionario):
    arq_dic = open('TrabalhosPython/Aula15 28-11/exercicio/cadastro_cerveja_dic.txt','a')
    arq_dic.write(f"{cerveja_dicionario['Nome']};{cerveja_dicionario['Marca']};{cerveja_dicionario['Tipo']};{cerveja_dicionario['Teor']}\n")
    arq_dic.close()

def ler_dic():
    lista = []
    arq_dic = open('TrabalhosPython/Aula15 28-11/exercicio/cadastro_cerveja_dic.txt','r')
    for linha in arq_dic:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'Nome':lista_linha[0],'Marca':lista_linha[1],'Tipo':lista_linha[2],'Teor':lista_linha[3]}
        lista.append(cerveja)
    arq_dic.close()
    return lista

nome = input('Digite o nome da cerveja: ')
marca = input('Digite a marca: ')
tipo = input('Digite o tipo: (Alcoolica/Nao alcoolica): ')
teor = float(input('Digite o teor: '))

cerveja = {'Nome':nome,'Marca':marca,'Tipo':tipo,'Teor':teor}

salvar_dic(cerveja)
lista = ler_dic()
for i in lista:
    print(f"Nome da Cerveja: {i['Nome']} - Marca: {i['Marca']} - Tipo: {i['Tipo']} - Teor: {i['Teor']}")
