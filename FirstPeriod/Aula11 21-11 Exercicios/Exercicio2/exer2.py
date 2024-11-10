#2 - Crie um programa que calcule
# a rentabilidade anual de um investimento
# baseando-se em uma rentabilidade mensal(juros compostos)
# a rentabilidade deve ser apresentada em % e R$
# Utilizar metodos

investimento_inicial = float(input('Digite o seu investimento inicial: '))
taxa_juros = float(input('Digite a taxa de juros composta: '))
juros_composto = investimento_inicial * (1+taxa_juros/100)**12

investimento_anual = investimento_inicial + (investimento_inicial*juros_composto)


print(investimento_anual)