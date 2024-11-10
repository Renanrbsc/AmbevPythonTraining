
#   X = 10
#   Y = 85
#   D = 30
# a função deve retornar 3, porque o sapo será posicionado da seguinte maneira:

# após o primeiro salto, na posição 10 + 30 = 40
# após o segundo salto, na posição 10 + 30 + 30 = 70
# após o terceiro salto, na posição 10 + 30 + 30 + 30 = 100
# Escreva um algoritmo eficiente para as seguintes suposições:

def solution(X,Y,D):
    jump_distance = Y - X
    jump_obtained = jump_distance / D
    if (jump_obtained % D) != 0:
        jump_obtained += 1
    return int(jump_obtained)
    
print(solution(10, 85, 30))