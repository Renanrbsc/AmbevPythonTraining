# Aula 19 - 04-12-2019
# Lista com for e metodos

# Como comer um gigante.... é com um pedaço de cada vez.
# Na hora de fazer este exercicio, atentar para 

# Com o arquivo de cadastro.txt onde possui os seguintes dados: codigo cliente, nome, idade, sexo, e-mail e telefone
# 1 - Crie um metodo que gere e retorne uma lista com dicionarios com os dados dos clientes
# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a dicionario dos maiores de idades.
# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.
# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing


# 1 - Crie um metodo que gere e retorne uma lista com dicionarios com os dados dos clientes
def ler_cadastro():
    lista = []
    arquivo = open('TrabalhosPython\Aula19 04-12\exercicios\exercicio3\cadastro.txt','r')
    for linha in arquivo:
        linha.strip()
        lista_linha = linha.split(';')
        dicionario = {'codigo':lista_linha[0],'nome':lista_linha[1],'idade':lista_linha[2],'sexo':lista_linha[3],'email':lista_linha[4],'telefone':lista_linha[5]}
        lista.append(dicionario)
    return lista

lista = ler_cadastro()
 
# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a dicionario dos maiores de idades.

def separar_idade(lista):
    lista_maior=[]
    lista_menor=[]
    for i in lista:
        if i['idade'] >= '18':
            lista_maior.append(i)
        else:
            lista_menor.append(i)
    salvar(lista_maior,'Idade maior')
    salvar(lista_menor,'Idade menor')
    return lista_maior

# def global para salvar listas com dicionarios
def salvar(lista,nome):
    arq = open(f'TrabalhosPython\Aula19 04-12\exercicios\exercicio3\{nome}.txt','w') #w escreve e se nao exstir, cria 
    for i in lista:
        arq.write(f"{i['codigo']};{i['nome']};{i['idade']};{i['sexo']};{i['email']};{i['telefone']}\n")
    arq.close()

lista_maior = separar_idade(lista)
# a = 1
# for i in lista_maior:
#     print(f"{a}  {i['codigo']};{i['nome']};{i['idade']};{i['sexo']};{i['email']};{i['telefone']}")
#     a+=1

# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.

def separar_sexo(lista):
    lista_homem=[]
    lista_mulher=[]    
    for i in lista:
        if i['sexo'] >= 'm':
            lista_homem.append(i)
        else:
            lista_mulher.append(i)
    print('Quantidade de Homens: ',len(lista_homem))
    print('Quantidade de Mulheres: ',len(lista_mulher))
    salvar(lista_homem,'Homens')
    salvar(lista_mulher,'Mulheres')

separar_sexo(lista)

# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1

def consultar_cadastro(lista,codigo):
    for i in lista:
        if codigo == i['codigo']:
            print(f'''\nCodigo: {i['codigo']}
Nome: {i['nome']}
Idade: {i['idade']}
Sexo: {i['sexo']}
Email: {i['email']}
Telefone: {i['telefone']}''')
            return
    print('Codigo não existe!')

#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:

def condicoes(lista,codigo):
    for i in lista:
        if codigo == i['codigo']:
            if i['sexo'] == 'f':
                if i['idade'] <= '16':
                    print(f"Ola {i['nome']}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!\n")
                elif i['idade'] > '16' and i['idade'] <= '18':
                    print(f"Olá {i['nome']}! Quer experimentar nosso refigerante sabor alegria! O seu cruch vai adorar!\n")
                else:
                    print(f"Olá {i['nome']}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico com o dobro de sabor!!!\n")
            elif i['sexo'] == 'm':
                if i['idade'] <= '16':
                    print(f"Ola {i['nome']}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!\n")
                elif i['idade'] > '16' and i['idade'] <= '18':
                    print(f"Olá {i['nome']}! Quer experimentar nosso refigerante sabor Corriga de carros! A sua amada vai adorar!\n")
                else:
                    print(f"Olá {i['nome']}! Já experimentou nossa cerveja? alto teor alcoolico com o dobro do amargor!!!\n")


            
while True:
    codigo = input('Digite o codigo do funcionario: ')
    consultar_cadastro(lista,codigo)   
    condicoes(lista,codigo)