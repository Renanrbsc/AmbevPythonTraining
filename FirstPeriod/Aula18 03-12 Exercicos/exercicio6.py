# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"

def leia_cad():
    lista = []
    arquivo = open('Aula18 03-12 Exercicios/cadastro.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        dicio = {'codigo': lista_linha[0], 'nome': lista_linha[1],
                 'sexo': lista_linha[2], 'idade': lista_linha[3]}
        lista.append(dicio)
    return lista


def separa_pessoa(lista):
    lista_masc = []
    lista_femi = []
    for linha in lista:
        if linha['idade'] >= '18':
            if linha['sexo'] == 'm':
                lista_masc.append(linha)
            else:
                lista_femi.append(linha)
    salvar(lista_masc, 'homens')
    salvar(lista_femi, 'mulheres')


def salvar(lista, nome):
    arquivo = open(f'Aula18 03-12 Exercicios/{nome}.txt', 'a')
    for linha in lista:
        arquivo.write(f"{linha['codigo']};{linha['nome']};{linha['sexo']};{linha['idade']}\n")
    arquivo.close()


def chamar_func(codigo, lista):
    for linha in lista:
        if codigo == linha['codigo']:
            print('-' * 50)
            print(f"Nome do Funcionario: {linha['nome']}")
            if linha['idade'] < '18':
                print(f"Entrada Proibida menores de 18! Sua idade: {linha['idade']}")
                print('-' * 50)
            else:
                if linha['sexo'] == 'f':
                    print(f'Valor do Ingresso: R$ 15,00')
                    print('-' * 50)
                else:
                    print(f'Valor do Ingresso: R$ 35,00')
                    print('-' * 50)


menu = '''################################################################
#             Cadastro Festa da HBSIS                          #
################################################################

# 1 - Criar Lista Dicionario com Cadastro.txt 
# 2 - Separar dados entre Homens e Mulheres
# 3 - Listar funcionario HBSIS Festa
# 4 - Sair

# Escolha a Opcao: '''
while True:
    opcao = input(menu)
    print('#' * 64)
    if opcao == '1':
        print('\nCriar Lista Dicionario com Cadastro.txt')
        lista = leia_cad()
        print('Sucesso!\n')
    elif opcao == '2':
        print('\nSeparar dados entre Homens e Mulheres\n')
        separa_pessoa(lista)
        print('Sucesso!\n')
    elif opcao == '3':
        print('\nListar funcionario HBSIS Festa')
        print('-' * 50)
        cod = input('Digite o codigo do funcionario: ')
        chamar_func(cod, lista)
    elif opcao == '4':
        print('\nEncerrar Programa\n')
        break
    else:
        print('\nOpcão não existe!\n')
