from def_cad_cliente import *
from def_cad_produtos import *

menu = '''################################################################
#             I Festival de Cervaeja de Ituroró                #
################################################################

1 - Cadastro de Cliente
2 - Ver clientes Cadastrados
3 - Cadastro de Produtos
4 - Ver produtos Cadastrados
5 - Vendas
6 - Relátorios de Vendas
7 - Encerrar Programa

Escolha a Opcao: '''

while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de Cliente')
        dic_cliente = inf_cad_cliente()
        salvar_dic_cliente(dic_cliente)
    elif opcao == '2':
        print('Ver clientes Cadastrados')
        
    elif opcao == '3':
        print('Cadastro de Produtos')
        dic_produtos = inf_produto_cad()
        salvar_dic_produto(dic_produtos)
    elif opcao == '4':
        print('Ver produtos Cadastrados')
        lista = ler_dic_produtos()
        mostrar_lista(lista)
    elif opcao == '5':
        print('Vendas')
    elif opcao == '6':
        print('Relátorios de Vendas')
    elif opcao == '7':
        print('Encerrar Programa')
        break
    else:
        print('Opcão não existe!')
