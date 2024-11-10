from model.endereco import Endereco
from dao.endereco_db import EnderecoDb

class EnderecoController:
    endereco = Endereco()
    endereco_db = EnderecoDb()

    def listar_tudo(self):
        return self.endereco_db.listar_todos()

    def exportar(self):
        lpc = self.endereco_db.listar_todos()
        self.p.exportar_txt(lpc)
