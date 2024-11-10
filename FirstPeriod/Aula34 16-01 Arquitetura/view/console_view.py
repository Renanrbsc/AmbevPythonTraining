import sys
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosPython/Aula34 16-01')
from controller.endereco_controller import EnderecoController

end_controll = EnderecoController()

for i in end_controll.listar_tudo():
    print(i)





