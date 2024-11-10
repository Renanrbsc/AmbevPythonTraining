def inf_produto_cad():
    nome = input('Digite o nome da cerveja: ')
    marca = input('Digite a marca: ')
    tipo = input('Digite o tipo: (Alcoolica/Nao alcoolica): ')
    teor = float(input('Digite o teor: '))
    dic_produtos = {'nome':nome,'Marca':marca,'Tipo':tipo, 'Teor':teor}
    print('''################################################################
#            Informações de Produtos recebidas!                #''')
    return dic_produtos

# def criar_dic_produtos(nome, marca, tipo, teor):
   # dic_produtos = {'Nome':nome,'Marca':Marca,'Tipo':tipo, 'Teor':teor}
   # return dic_produtos

def salvar_dic_produto(dic_produtos):
    arq_dic = open('Aula17 02-12/cadastro_produtos.txt','a')
    arq_dic.write(f"{dic_produtos['nome']};{dic_produtos['marca']};{dic_produtos['tipo']};{dic_produtos['teor']}\n")
    arq_dic.close()
    print('''################################################################
#                    Informações salvas!                       #
################################################################\n\n\n''')


def ler_dic_produtos():
    lista = []
    arq_dic = open('Aula17 02-12/cadastro_produtos.txt','r')
    for linha in arq_dic:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'Nome':lista_linha[0],'Marca':lista_linha[1],'Tipo':lista_linha[2],'Teor':lista_linha[3]}
        lista.append(cerveja)
    arq_dic.close()
    return lista

def mostrar_lista(lista):
    c=0
    for i in lista:
        print(f"Nome da Cerveja: {i['Nome']} - Marca: {i['Marca']} - Tipo: {i['Tipo']} - Teor: {i['Teor']}")
        c = c + 1
    print('\n\n\n')
