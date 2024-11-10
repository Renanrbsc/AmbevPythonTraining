# from exer1_calculos import calculo_div, calculo_div_int, calculo_mul, calculo_raiz, calculo_resto_div, calculo_soma, calculo_sub
from exer1_calculos import *

print('~'*50)

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

print('~'*50)

mul = calculo_mul(valor1,valor2)
div = calculo_div(valor1,valor2)
sub = calculo_sub(valor1,valor2)
soma = calculo_soma(valor1,valor2)
div_int = calculo_div_int(valor1,valor2)
resto_div = calculo_resto_div(valor1,valor2)
raiz = calculo_raiz(valor1,valor2)

print(f'''A Subtração de: {valor1} - {valor2} = {sub}
A Multiplicação de: {valor1} * {valor2} é: {mul}
A Divisão de: {valor1} / {valor2} é: {div:.3f}
A Soma de: {valor1} + {valor2} = {soma}
A Divisão inteira de: {valor1} // {valor2} é: {div_int}
O resto da divisão de: {valor1} % {valor2} é: {resto_div}
A Raiz de: {valor1} em {valor2} é: {raiz:.5f}''')

print('~'*50)


