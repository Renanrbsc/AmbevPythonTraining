# Aula 18 - 03-11-2019

# Ao receber a seguinte lista, faça um metodo que retorne cada um destes itens de forma individual 
# com cabaçalho dizendo em que posição estes itens estão dentro da lista principal:
# Exemplo: 
# ############# posição 0 ##################
# Agua
# mamão
# ############# posição 1 ##################
# banana
# limão

#Regra: Não pode usar a função range e no máximo 2 print()

lista = [
          ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
          ['skol','kaiser','sol','schin','brahma','itaipava','bavaria'],
          ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha','skol'],
          ['rizoto','macarronada','polenta','guizado','dobradinha','revirado','pure'],
          ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
          ['agua','cachoeira','rio','lagoa','sanga','brejo','laguna'],
          ['vento','ciclone','tufão','furacão','brisa','minuano','zefiro'],
          ['carro','moto','vespa','caminhão','sprinter','kombi','fusca'],
          ['calça','camisa','japona','jaqueta','camiseta','bone','regata']
        ]


a = 0
for i in lista:
    print(f'################## Posicao {a} #####################')
    a+=1
    for j in i:
      print(j)

    # print(f'{lista[0][a]}, {lista[1][a]}, {lista[2][a]}, {lista[3][a]}, {lista[4][a]}, {lista[5][a]}, {lista[6][a]}, {lista[7][a]}, {lista[8][a]}')
    # a+=1
    # if a == 7:
    #   break

