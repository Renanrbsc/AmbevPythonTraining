Uma matriz não vazia A consistindo de N inteiros é dada. O Array A representa números em uma fita.

Qualquer tetger P, de tal forma que 0 < P < N, divide essa fita em duas partes não vazias: A[0], A[1], ..., A[P − 1] e A[P], A[P + 1], ..., A[N − 1].

A diferença entre as duas partes é o valor de: | (A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

Em outras palavras, é a diferença absoluta entre a soma da primeira parte e a soma da segunda parte.

Por exemplo, considere a matriz A tal que:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
Podemos dividir esta fita em quatro lugares:

P = 1, diferença = |3 − 10| = 7
P = 2, diferença = |4 − 9| = 5
P = 3, diferença = |6 − 7| = 1
P = 4, diferença = |10 − 3| = 7
Escreva uma função:

solução def(A)

que, dada uma matriz não vazia A de N inteiros, retorna a diferença mínima que pode ser alcançada.

Por exemplo, dado:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
a função deve retornar 1, como explicado acima.

Escreva um algoritmo eficiente para as seguintes suposições:

N é um inteiro dentro da faixa [2.. 100.000];
cada elemento da matriz A é um inteiro dentro da faixa [−1.000.. 1.000].