from Dao.pessoa_dao import PessoaDao
from Model.pessoa import Pessoa
from Controller.endereco_controller import EnderecoController

class PessoaController:
    dao = PessoaDao()
    endereco_controller = EnderecoController()
    lista_copia_dados = [0]
    id_copia = 0

    def listar_todos(self):
        return self.dao.listar_todos()

    def listar_por_id(self, id):
        self.lista_copia_dados = self.copia_id(id)
        return self.dao.listar_por_id(id)

    def copia_id(self, id):
        self.lista_copia_dados = self.dao.listar_por_id(id)
        self.id_copia = id
        return self.lista_copia_dados

    def salvar(self, pessoa:Pessoa):
        pessoa.endereco.id = self.endereco_controller.salvar(pessoa.endereco)
        return self.dao.salvar(pessoa)

    def alterar(self, pessoa:Pessoa, id):
        self.dao.alterar(pessoa, id)

    def deletar(self, id):
        self.dao.deletar(id)
