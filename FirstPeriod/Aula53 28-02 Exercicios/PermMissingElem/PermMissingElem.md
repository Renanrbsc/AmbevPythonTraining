Uma matriz A composta por N diferentes inteiros é dada. A matriz contém inteiros na faixa [1... N + 1)], o que significa que exatamente um elemento está faltando.

Seu objetivo é encontrar esse elemento perdido.

Escreva uma função:

solução def(A)

que, dada uma matriz A, devolve o valor do elemento ausente.

Por exemplo, dada a matriz A tal que:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
a função deve retornar 4, pois é o elemento ausente.

Escreva um algoritmo eficiente para as seguintes suposições:

N é um inteiro dentro da faixa [0.. 100.000];
os elementos de A são todos distintos;
cada elemento da matriz A é um inteiro dentro do intervalo [1..; N + 1)].