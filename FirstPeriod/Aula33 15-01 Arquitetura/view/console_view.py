import sys
sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosPython/Aula33 15-01 Arquitetura')
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosPython/Aula33 15-01 Arquitetura')

from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_por_like():
    print(p)

print('Deseja Exportar arquivo txt com os dados?')
op = input('( y - n )')

if op == 'y':
    pc.exportar()
    print('Arquivo salvo com sucesso!')
else:
    print('Ação cancelada!')
