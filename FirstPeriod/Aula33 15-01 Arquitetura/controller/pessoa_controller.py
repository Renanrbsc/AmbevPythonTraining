from model.pessoa import Pessoa
from dao.pessoa_db import PessoaDb

class PessoaController:
    #---- variaveis padrao da classe
    p = Pessoa() #--- padrao vazia, mas recebe dados temporarios de (self)
    p_db = PessoaDb() #--- padrao vazia, mas recebe dados temporarios de (self)
    lpc = [] #--- padrao vazia, mas recebe dados temporarios de (self)

    def listar_por_like(self):
        #---- SELF -> resultados temporarios da classe
        self.lpc = self.p_db.listar_por_like()
        return self.lpc

    def exportar(self):
        #--- salvando o resultado temporario da (self.lpc) e exportando...
        self.p.exportar_txt(self.lpc)
