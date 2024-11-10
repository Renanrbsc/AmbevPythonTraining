lista_banda = []
lista_album = []
lista_musica = []

menu = '''#################################################
#                                               #
#            Cadastro de Banda                  #
#                                               #
# 1 - Cadastro da banda                        #
# 2 - Cadastro do album                         #
# 3 - Cadastro da musica                       #
# 4 - Listar                                       #
# 5 - Sair                                      #
#                                               #
#################################################
# Digite a opcao: '''

while True:
    opcao = input(menu)

    if opcao == '1':
        lista_banda.append(input('Digite a banda: '))

    elif opcao == '2':
        lista_album.append(input('Digite o album: ')

    elif opcao == '3':
        lista_musica.append(input('Digite a musica: ')
        elif opcao == '4':
        print(f'Lista de banda: {lista_banda}\nLista de albun: {lista_albun}\nLista de musica: {lista_musica}\n')
        break
    elif opcao == '5':
        print('Programa finalizado!')
        break
    else:
        print('Opcao não existe!\n')
        