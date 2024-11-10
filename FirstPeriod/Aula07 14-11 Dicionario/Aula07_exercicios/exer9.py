#--- Exercicio 4  - Variávies e impressão com interpolacão de string
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- Entre os dois pontos deve conter no minimo 10 pontos de parada
#--- Cada item deve conter data, hora e descrição
#--- O itineário deve conter cabeçalho com o título da viagem
#--- Os dados de cada ponto devem estar em variáveis
#--- Deve ser usado os caracteres de tabulação, quebra de linha e a função Format()

inf_ponto1 = {'Local':'','Data':'','Hora':'','Descricao':''}

partida = 'Amsterdam (Holanda)'
destino = 'Budapeste (Hungria)'
ponto2 = 'Bruges (Bélgica)'
ponto3 = 'Cidade de Luxemburgo (Luxemburgo)'
ponto4 = 'Estrasburgo / Strasbourg (França)'
ponto5 = 'Vaduz (Principado de Liechenstein)'
ponto6 = 'Munique (Alemanha)'
ponto7 = 'Praga (República Tcheca)'
ponto8 = 'Viena (Áustria)'
ponto9 = 'Bratislava (Eslováquia)'

inf_ponto1 = {'Local':partida,'Data':'17-11-2019','Hora':'12:05','Descricao':'Partida'}
inf_ponto2 = {'Local':ponto2,'Data':'17-11-2019','Hora':'15:03','Descricao':'Ponto de parada 1'}
inf_ponto3 = {'Local':ponto3,'Data':'17-11-2019','Hora':'18:09','Descricao':'Ponto de parada 2'}
inf_ponto4 = {'Local':ponto4,'Data':'17-11-2019','Hora':'20:25','Descricao':'Ponto de parada 3'}
inf_ponto5 = {'Local':ponto5,'Data':'17-11-2019','Hora':'23:36','Descricao':'Ponto de parada 4'}
inf_ponto6 = {'Local':ponto6,'Data':'18-11-2019','Hora':'02:14','Descricao':'Ponto de parada 5'}
inf_ponto7 = {'Local':ponto7,'Data':'18-11-2019','Hora':'05:52','Descricao':'Ponto de parada 6'}
inf_ponto8 = {'Local':ponto8,'Data':'18-11-2019','Hora':'09:19','Descricao':'Ponto de parada 7'}
inf_ponto9 = {'Local':ponto9,'Data':'18-11-2019','Hora':'10:24','Descricao':'Ponto de parada 8'}
inf_ponto10 = {'Local':destino,'Data':'18-11-2019','Hora':'12:39','Descricao':'Destino'}

pontos = [inf_ponto1,inf_ponto2,inf_ponto3,inf_ponto4,inf_ponto5,inf_ponto6,inf_ponto7,inf_ponto8,inf_ponto9,inf_ponto10]


print('~'*60,'\n')
print('Plano de Viagem Europa, 10 Pontos Turisticos em 2 dias!')
print('\n','~'*60)
for i in pontos:
    print(f"    Localização: {i['Local']}\nData: {i['Data']} | Hora: {i['Hora']} | Descrição: {i['Descricao']}\n")
print('~'*60,'\n'*4,'~'*60)
