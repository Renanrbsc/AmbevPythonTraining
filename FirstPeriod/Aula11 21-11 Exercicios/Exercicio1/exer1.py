
#1 - Crie um programa que calcule 
# o imposto ISS de um serviço de desenvolvimento de software 
# Utilizar metodos

from calculoISSdef import *

print('='*50)
print('1 - Empresas produtoras')
print('2 - Empresa de serviço geral Software')
print('='*50)

op = int(input('Digite uma opcao:'))

calculo = calculoISS(op)

print(f"Seu Orcamento é: R${calculo['orcamento']} \nO desconto de ISS é: {calculo['iss']*100}% \nO desconto de ISS é: {calculo['desconto']}")


#Em Blumenau o ISS varia de 2% para as 
#empresas produtoras a 5% para empresas que atuam na área de serviços em geral