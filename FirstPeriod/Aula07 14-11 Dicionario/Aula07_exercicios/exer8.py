#--- Exercicio 3  - Variávies e impressão com interpolacão de string
#--- Imprima dois paragráfos do ultimo livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- Livro: Título, Edição, Autor, Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

titulo = 'Cosmos'
edicao = 'Edição: 1'
autor = 'Carl Sagan - Neil deGrasse Tyson'
datapub = '6 de novembro de 2017'
cap = 'VI - Historias de Viajantes - Pg 165'

print('     Tanto o campo magnético de Saturno como o de Júpiter')
print('captam e aceleram as partículas carregadas do vento solar.')
print('Quando uma partícula dessas salta de um pólo magnético a outro,')
print('deve atravessar o plano equatorial de Saturno. Se houver uma')
print('partícula do anel no caminho, o próton ou elétron é absorvido por')
print('esta pequena bola de neve. Como resultado, em ambos os')
print('planetas os anéis limpam os cinturões radioativos, que existem')
print('somente interna e externamente aos anéis. Uma lua próxima de')
print('Júpiter ou Saturno traga as partículas do cinturão, sendo uma das')
print('novas luas de Saturno descoberta desta forma: a Pioneer 11')
print('descobriu uma falha inesperada nos cinturões radioativos, causada')
print('pela varredura das partículas carregadas por uma lua não')
print('conhecida anteriormente.')
print('     O vento solar desliza no sistema solar exterior bem além da')
print('órbita de Saturno. Quando a Voyager chegar a Urano e às órbitas')
print('de Netuno e Plutão, se os instrumentos ainda estiverem')
print('funcionando, certamente sentirão a sua presença, o vento entre os')
print('mundos, o topo da atmosfera do Sol levado ao domínio das')
print('estrelas. A duas ou três vezes a distância do Sol a Plutão, a')
print('pressão dos prótons e elétrons se torna maior que a exercida lá')
print('pelo vento solar. Aquele local, chamado heliopausa, é uma')
print('definição da fronteira externa do Império do Sol. Mas a espaçonave')
print('Voyager mergulhará e penetrará na heliopausa em algum momento')
print('na metade do século XXI, deslizando no oceano do espaço, nunca')
print('penetrando em outro sistema solar, destinada a vagar pela')
print('eternidade entre as linhas estelares e a completar a primeira')
print('circunavegação do centro massivo da Via-láctea, daqui a algumas')
print('centenas de milhões de anos. Aventuramo-nos em viagens épicas.')

print(f'\nTitulo: {titulo}, Autor: {autor}\nEdição: {edicao}, Data de Publicação: {datapub} ')
print(f'Capitulo: {cap}')

