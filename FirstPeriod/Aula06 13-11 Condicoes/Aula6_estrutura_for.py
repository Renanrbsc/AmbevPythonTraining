# Aula 6 - P2 - 13-11-19
# Estrutura de repetição - FOR

# RANGE(inicio,fim,incremento)
# range(0,10,1) -> 0,1,2,3,4,5,6,7,8,9
# range(1,10,1) -> 1,2,3,4,5,6,7,8,9
# range(0,10,2) -> 0,2,4,6,8

# for simples usando range com intervalo padrao de 10 e incremento de 1
for i in range(0,10): # i = contador, range = funcao intervalo, começa em 0, executa dentro do intervalo de 10
    print(f'{1} - Padawans HBpy') 

# for usando range com incremento de 2
for i in range(0,20,2): # executa dentro do intervalo de 20 e a cada 2 casas, ignora a ultima
    print(f'{i}- Pares')

# for usando range com incremento de 5
for i in range(0,50,5):  # executa dentro do intervalo de 50 e a cada 5 casas, ignora a ultima
    print(f'{i}- Maca')


# Tabuada de 1 a 10
for i in range(1,11):
    print("\nTabuada do",i)
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')