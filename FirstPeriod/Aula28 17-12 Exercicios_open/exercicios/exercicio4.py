# Aula 28 - 17-12-2019
# Listas

# DICA!!!!
# Procurem primeiro o padrão que estas listas vão apresentar! Depois de encontrado, faça o uso da linguagem
# para facilitar na hora de codar!


lista1 = [['frutas','verduras','legumes','preço'],# 0 1 2 3 [0][i]
         ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'], # [i][0]
         ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha','cebolinha'],
         ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
         [ [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
           [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] #[4][][]
         ]
        ]


lista2 = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]

# 1) Faça um dicionário com a lista1 onde cada elemento esteja junto com o seu respectivo
# preço. (Dica: Use a indexação e fatiamento para ajudar)
def dic_lista1(lista):
  lista_dic = []
  indice = lista[0]
  dados = [lista[1],lista[2],lista[3]]
  preco = lista[4]
  for i in range(3):
    for j in range(7):
      dicionario = {indice[i]:dados[i][j],indice[3]:preco[i][j]}
      lista_dic.append(dicionario)
  return lista_dic

lista_nova = dic_lista1(lista1)


# 2) Com o dicionário, imprima os seguintes valores:
for i in lista_nova:
# 2.1) Preço do feijão
  if 'legumes' in i and 'feijão' == i['legumes']:
      print(i)
# 2.2) Preço da cebolinha
  if 'verduras' in i and 'cebolinha' == i['verduras']:
      print(i)
# 2.3) Preço da Alface lisa
  if 'verduras' in i and 'alface lisa' == i['verduras']:
      print(i)
# 2.4) Preço do Abacaxi
  if 'frutas' in i and 'abacaxi' == i['frutas']:
      print(i)
# 2.5) Preço do feijão branco.
  if 'legumes' in i and 'feijão branco' == i['legumes']:
      print(i)
# 3) Com a lista1 qual seria a média dos valores das frutas, verduras e legumes?
preco = lista1[4]
medias = []
print(f'A media de preco das listas é: ')
for i in preco:
  media = sum(i)/7
  medias.append(media)
print(f'Frutas: {medias[0]:.2f} Verduras: {medias[1]:.2f} Legumes: {medias[2]:.2f}\n')
    
# 4) Com a lista 1, Qual é o maior e menor valor das frutas, verduras e legumes?
lista_max = []
lista_min = []
for i in preco:
  lista_max.append(max(i))
  lista_min.append(min(i))

print(f'Frutas: {lista_max[0]} | {lista_min[0]}\nVerduras: {lista_max[1]} | {lista_min[1]}\nLegumes: {lista_max[2]} | {lista_min[2]}')
# 5) Adicione no cabeçalho da lista1 (entre o legumes e preço) a "roupa". Aṕos adicione de forma que fique 
# com a lista coerente 7 roupas e os seus preços.
#print(f'Frutas: {lista_max[0]} | {lista_min[0]}\nVerduras: {lista_max[1]} | {lista_min[1]}\nLegumes: {lista_max[2]} | {lista_min[2]}')


# 6) Salve esta lista em um arquivo .txt de moque que cada linha tenha o item e seu preço.
<<<<<<< HEAD
arquivo = open('ExerciciosPython\Resolucao_Exercicio\Renan Berti Ribas\Aula28-Exercicio\exercicios\precos.txt','w')
=======
arquivo = open('TrabalhosPython\Aula28 17-12\exercicios\precos.txt','w')
>>>>>>> 52baa6a0e1c78ef1d22cf380e6d815fea57d5d8d
for i in lista_nova:
      lista_dados = []
      for j in i:
            lista_dados.append(str(i[j]))
      arquivo.write(';'.join(lista_dados)+'\n')
arquivo.close()


# 7) Com a lista2, crie uma lista com dicionário onde cada dicionário é um cadastro de uma pessoa.
def dic_lista2(lista):
      lista_dic = []
      indice = [lista[0],lista[2],lista[4],lista[6]]
      dados = [lista[1],lista[3],lista[5],lista[7]]
      print(indice[0])
      print(dados[0][0])
      j = len(lista[2])-1
      for i in range(j):
            dicionario = {indice[0]:dados[0][i],indice[1]:dados[1][i],indice[2]:dados[2][i],indice[3]:dados[3][i]}
            lista_dic.append(dicionario)
      return lista_dic
pessoa = dic_lista2(lista2)
for i in pessoa:
      print(i)

# 8) Organize a lista2, retirando o cabeçalho e junte os dados de modo que cada cliente ocupe uma lista. Após, salve os dados
# em um arquivo .txt
<<<<<<< HEAD
arquivo = open('ExerciciosPython\Resolucao_Exercicio\Renan Berti Ribas\Aula28-Exercicio\exercicios\pessoa.txt','w')
=======
arquivo = open('TrabalhosPython\Aula28 17-12\exercicios\pessoa.txt','w')
>>>>>>> 52baa6a0e1c78ef1d22cf380e6d815fea57d5d8d
for i in pessoa:
      lista_dados = []
      for j in i:
            lista_dados.append(str(i[j]))
      arquivo.write(';'.join(lista_dados)+'\n')
arquivo.close()


# 9) Criando uma fila. Uma fila é uma estrutura de dados onde o primeiro item que entra é o ultimo que sai. Resumindo, o item novo
# entra no indice 0 da lista e sai pelo ultimo indice. 

# Crie um programa que adiciona novos clientes em uma fila e conforme vai atendendo, remova-os da fila do caixa da loja.
fila = []
tamanho = int(input('Insira o limite da fila de clientes: '))
for i in range(tamanho):
      valor = input('Digite o nome do ultimo cliente que entrou na fila: ')
      fila.insert(0,valor)
      print(f'- {fila}')
print('Fila excedida!')
for i in range(tamanho):
      pessoa = fila.pop()
      print(f'Cliente passou no caixa! {pessoa}')
      print(f'- {fila}')
print('Fila livre!')

# 10) Criando uma pilha. Uma pilha é uma estrutura de dados onde o primeiro que entra é o ultimo a sair. Resumindo,
# Os elementos são adicionados e removidos no mesmo lado da lista.

# Crie um programa em que adicione os novos números na pilha. Após some eles removendo da pilha.
pilha = []
tamanho = int(input('Insira o tamanho da lista: '))
for i in range(tamanho):
      valor = int(input('Digite o valor a ser inserido na fila: '))
      pilha.append(valor)
      print(f'- {pilha}')
print('Fim da inserçao!')
soma = 0
for i in range(tamanho):
      soma += pilha.pop()
      print(f'- [{pilha},{soma}]')
print(f'Soma: {soma}')
print('Fim da retirada!')