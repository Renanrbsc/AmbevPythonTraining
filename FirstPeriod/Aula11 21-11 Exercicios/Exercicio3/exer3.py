
#3 - Crie um programa para calculo de investimento
  #  Solicitar valor a ser investido no tesouro selic
  #  (considerar valor do tesouro selic hoje)
  # pedir cota que deseja comprar
  #  Calcular o valor total ate o vencimento do titulo
#    Utilizar metodos
    

Tesouro_selic = 10410.00
Taxa_rendimento = 0.02

cota_investida = float(input('Digite a quantidade de cotas de investimento: '))


if cota_investida >= 1:
    titulo = Tesouro_selic*(cota_investida/100)
    print(f'Valor da Cota investica: R${titulo:.2f}')
else:
    print(f'Numero de cotas invalidas!')

Taxa_mensal = titulo*0.02
print(f'Taxa mensal cobrada:{Taxa_mensal:.2f}')
Renda_anual = (titulo + (Taxa_mensal*12))*0.05
print(f'Renda Anual sobre a taxa:{Renda_anual:.2f}')

def convert_ano_mes(titulo):
  mes_atual = int(input('Digite o mes do ano atual: '))
  ano_atual = int(input('Digite o ano atual: '))

  mes_venc = 3
  ano_venc = 2025

  convert_mes_restante = (mes_atual - 12) + mes_venc
  convert_ano_mes = ano_venc - ano_atual
  convert_data = (convert_ano_mes*12) + convert_mes_restante
  return convert_data

convert_data = convert_ano_mes(titulo)
print(f'A quantidade de meses entre {2019} e {2025} é: {convert_data}')

taxa_rendida = Taxa_mensal*convert_data
taxa_total = titulo + taxa_rendida
juros_total = taxa_total*0.05


print(f'''A taxa de juros rendida no periodo até vencimento: R${taxa_rendida} 
O valor do titulo após taxa: R${taxa_total:.2f}
O juros total rendido sobre a taxa é: R${juros_total:.2f}''')
 