# Aula9 19-11-2019
# BLOCO DE CODIGO - METODOS - IMPORT

from calculo_imposto import calculo_inss, calculo_irrf

salario = float(input('Digite seu Salario: '))

inss = calculo_inss(salario) 
irrf = calculo_irrf(salario,inss)

salario_liquido = salario - inss - irrf

print(f'Com base seu Salario: R${salario:0.2f}\nDesconto de INSS é: R${inss:0.2f}\nDesconto de IRRF é: R${irrf:0.2f}')
print(f'Seu salario liquido é R${salario_liquido:0.2f}')