import sys
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosPython/Aula35 17-01')
sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosPython/Aula35 17-01')
from Controller.pessoa_controller import PessoaController
from Model.pessoa import Pessoa

def menu():
    print('*********************************')
    print('* 1- Listar por codigo          *')
    print('* 2- Cadastrar Cliente/Endereco *')
    print('* 3- Alterar Cliente            *')
    print('*********************************')
    return int(input('* Digite a opcao: '))

controller = PessoaController()
pessoa = Pessoa()

op = menu()
if op == 1:
    print('-----Busca por codigo-----')
    id = int(input('Digite o codigo: '))
    print(controller.listar_por_id(id))

elif op == 2:
    print('-----Cadastrar Cliente/Endereco-----')
    pessoa.nome = 'Will'
    pessoa.sobrenome = 'Smith'
    pessoa.idade = 85
    pessoa.genero = 'm'
    pessoa.email = 'homensdepreto@hotmail.com'
    pessoa.telefone = '458232232'
    pessoa.endereco.logradouro = 'Rua dos tiras'
    pessoa.endereco.numero = 00
    pessoa.endereco.sigla = 'GH'
    pessoa.endereco.cidade = 'Nova York'
    pessoa.endereco.bairro = '254'
    pessoa.endereco.cep = 115852

    # id_salvo = controller.salvar(pessoa)
    # pessoa_endereco = controller.listar_por_id(id_salvo)
    # print(pessoa_endereco)
    
elif op == 3:
    print('-----Alterar Cliente-----')

else:
    print('Estou perdido!')






# /inserir/id={{ p[0]}} pega o valor e retorna no link da pagina



