import random

# Efetua 1000 testes:
for _ in range(1000):

    # Gera um conjunto de 10 números inteiros entre 0 e 9:
    a = set(random.randint(0, 9) for __ in range(10))

    # Verifica se o conjunto é igual à sua respectiva lista sortida:
    if list(a) != sorted(a):

        # Se for diferente, exibe o conjunto:
        print(a)