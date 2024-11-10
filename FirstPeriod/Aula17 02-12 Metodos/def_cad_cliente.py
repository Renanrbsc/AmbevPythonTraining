def inf_cad_cliente():
    nome = input('Digite o nome do cliente: ')
    sobrenome = input('Digite o sobrenome do cliente: ')
    cpf = input('Digite o cpf: ')
    idade = int(input('Digite a idade: '))
    dic_cliente = {'nome':nome,'sobrenome':sobrenome,'cpf':cpf, 'idade':idade}
    print('''################################################################
#            Informações do cliente recebidas!                #''')
    return dic_cliente

def salvar_dic_cliente(dic_cliente):
    arq_dic = open('Aula17 02-12/cadastro_cliente.txt','a')
    arq_dic.write(f"{dic_cliente['nome']};{dic_cliente['sobrenome']};{dic_cliente['cpf']};{dic_cliente['idade']}\n")
    arq_dic.close()
    print('''################################################################
#                    Informações salvas!                       #
################################################################\n\n\n''')


def ler_dic():
    lista = []
    arq_dic = open('Aula17 02-12/cadastro_produtos.txt','r')
    for linha in arq_dic:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'Nome':lista_linha[0],'Marca':lista_linha[1],'Tipo':lista_linha[2],'Teor':lista_linha[3]}
        lista.append(cerveja)
    arq_dic.close()
    return lista
