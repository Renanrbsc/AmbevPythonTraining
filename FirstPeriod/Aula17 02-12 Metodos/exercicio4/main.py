dados_cliente = ['Codigo_cliente','CPF', 'Nome_completo','Data_de_nascimento',
'Estado','Cidade','Cep','Bairro','Rua','Numero_casa', 'Complemento']

def cadastro_for(numero):
    lista = []
    dicionario = {}
    b = 1
    for j in range(numero):
        print(f'\nInforme as informaçoes do {b} cadastro')

        for i in dados_cliente:
            dicionario[i] = input(f'{i}: ')

        lista.append(dicionario)
        b +=1
    return lista



numero = int(input('Digite o numero de cadastros: '))
lista = cadastro_for(numero)


for cliente in lista_cadastro:
        cliente_chave = lista(cliente.keys())
    for chaves in cliente_chave:
        salva = (f'{cliente[chaves]}')
        




# #numero=int(input('Digite numero de  cadastros: '))
# #lista_cadastro = cadastro_cliente(numero)


# lista_cadastro = [{'Codigo_cliente':12, 'CPF':00000, 'nome_completo':'Alberto', 
#                     'data_de_nascimento':"10/12/2000", 'estado':'SC',
#                     'cidade':'Camboriú',
#                     'cep':8885555, 'bairro':Garcia, 'rua':'Italia',
#                     'numero_casa':53, 'complemento': 'ap 35'}]
# # Criar uma função para salvar em arquivo:

# for cliente in lista_cadastro:
#     cliente_chave = list(cliente.keys())
#     for chaves in cliente_chave:
#         salva = (f'{cliente[chaves]}')
#         print(salva)


# # Continua em outra hora
    