
def exportar_txt(lista_pessoa):
    #----- Criacao de arquivo.txt com base os dados da lista de dicionario
    with open('TrabalhosPython\Aula33 15-01\Aula33 OObj\pessoas.txt','w') as arq:
        for j in lista_pessoa:
            arq.write(f"{j['CODIGO']};{j['NOME']};{j['SOBRENOME']};{j['IDADE']};{j['GENERO']};{j['EMAIL']};{j['TELEFONE']}\n")
