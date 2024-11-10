# Exercicio 3 - Foreach
# Escreva programa que leia as notas (4) de 10 alunos
# Armazene as notas e os nomes em listas
# imprima:
#          o nome dos alunos 
#          suas respectivas medias 
#          resultados (Aprovado nota 7)

notas = []
alunos = []
medias = []

for a in range(0,5): 
    alunos.append(str(input('Digite o nome do aluno:\n'))) 
    v1 = float(input('Digite a primeira nota do aluno:'))
    notas.append(v1)
    v2 = float(input('Digite a segunda nota do aluno:'))
    notas.append(v2)
    v3 = float(input('Digite a terceira nota do aluno:'))
    notas.append(v3)
    v4 = float(input('Digite a quarta nota do aluno:'))
    notas.append(v4)

    media = (v1+v2+v3+v4)/4  
    medias.append(media)
    
i = 0
e = 0
for i in range(0,5):
    print('Aluno:',alunos[i])
    for o in range (0,4):
        print(notas[e])
        e = e +1
    print('Media:',medias[i])
    if medias[i] > 7:
        print('Aluno aprovado!')
    else:
        print('Aluno reprovado')
    i = i + 1

print(notas)
        


