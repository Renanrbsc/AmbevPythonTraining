# Aula 18 - 03-11-2019
# Exercicio para lista dentro de lista

# Dada a seguinte lista, resolva os seguintes questões:

lista = [
          ['frutas','verduras','legumes'],
          ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
          ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha'],
          ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja']
        ]

# A lista está organizada da seguinte forma:
#       A primeira lista é o cabeçalho que diz o que siguinifica cada lista a seguir. Ex: Lista de frutas, lita de verduras
#       lista de legumes.
# Com isso responda as seguintes questões:


print('1: imprima a lista cabeçalho e mostre todos os seus elemantos')
print(f'{lista[0:]}\n')

print('2: imprima a lista verduras e mostre todos os seus elemantos')
print(f'{lista[2]}\n')

print('3: imprima com f-string a seguinte sequência: abacaxi - laranja - maçã - vergamota')
print(f'{lista[1][1:3]}-{lista[1][5:7]}\n')

print('4: imprima com f-string a seguinte sequência: alface lisa - salsinha - rucula - alface crespa')
print(f'{lista[2][1:6:4]}-{lista[2][2]}-{lista[2][0]}\n')

print('5: imprima com f-string a seguinte sequência: frutas: laranja e prera - verduras: repolho e rucula'
      '\nlegumes: ervilha, feijão branco e grão de bico')
print(f'{lista[0][0]}: {lista[1][2:5:2]} - {lista[0][1]}: {lista[2][2:5:2]} - {lista[0][2]}: {lista[3][1]},{lista[3][4:6]}\n')

print('6: imprima com f-string a seguinte sequência: mamão - ervilha, rucula, salsinha, mamão, repolho')
print(f'{lista[1][0]}-{lista[3][1]},{lista[2][2]},{lista[2][5]},{lista[1][0]},{lista[2][4]}\n')


print('7: imprima com f-string a seguinte sequência: fruta: 3kg de laranja, 8kg de uva, 4.5kg de maçã, 1kg de vergamota')
print(f'{lista[0][0]}: 3kg de {lista[1][2]}, 8kg de {lista[1][3]}, 4,5kg de {lista[1][5]}, 1kg de {lista[1][6]}\n')


print('8: imprima com f-string a seguinte sequência: verduras: 5 maço de salsinha, 4 pés de alface crespa e alface lisa'
      '2 cabeças de repolho')
print(f'{lista[0][1]}: 5 maço de {lista[2][5]}, 4pes de {lista[2][0]}e {lista[2][1]}\n')


print('9: imprima com f-string a seguinte sequência: legumes: 1kg de feijão, 2kg de gão de bico, 1.5 kg dde soja,'
      '1 pacote de ervilha')


print('10: imprima a lista legumes e mostre todos os seus elemantos')
print(f'{lista[2]}')