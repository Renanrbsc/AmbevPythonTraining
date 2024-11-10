#--- Exercicio 5  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia o salário de uma pessoa
#--- Use o método 50-20-10-20 - https://www.jaseimevirar.com/blog/como-voce-organiza-seu-orcamento-mensal/
# Método 50-20-10-20 (50% gastos, 20% investimentos a longo prazo, 10% investimentos a curto prazo, 20% livre)
#--- Informe os percentuais e valores que a pessoa deve utilizar em cada categoria
#--- Deve ser utilizado a função format e os caracteres de tabulação e quebra de linha para cada categoria

salario = float(input('Digite o seu Salario: R$'))

gastos = salario * 0.50
investLp = salario * 0.20
investCp = salario * 0.10
livre = salario * 0.20

print(f'''Salario: R${salario:.2f}\n
Usando metodo 50-20-10-20\n
\t50% gastos = R${gastos:.2f}
\t20% investimentos a longo prazo = R${investLp:.2f}
\t10% investimentos a curto prazo = R${investCp:.2f}
\t20% livre = R${livre:.2f}
''')