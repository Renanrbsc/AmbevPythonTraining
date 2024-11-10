from random import randint
from pessoa_base import PessoaBase

class Cliente(PessoaBase):

    def __init__(self, nome, sobrenome, idade,cpf, local):
        super().__init__(nome, sobrenome, idade)
        self.cpf = cpf
        self.local = local
        self.id_funcionario = None

    @property 
    def id_funcionario(self):
        return self._id_funcionario

    @id_funcionario.setter
    def id_funcionario(self,id_funcionario):
        if id_funcionario == None:
            id_funcionario = self.gerador_de_id()
        self._id_funcionario = id_funcionario

    def mostrar_dados(self):
        print(f'{super().nome_completo()}\n'
              f'Idade: {super().idade}\n'
              f'{super().ano_de_nascimento()}\n'
              f'CPF: {self.cpf}\n'
              f'Local de Trabalho: {self.local}\n'
              f'Id funcionario: {self.id_funcionario}\n')
        
    @staticmethod
    def gerador_de_id():
        random_id_funcionario = randint(100,999)
        return random_id_funcionario
        

cliente1 = Cliente('Renan', 'Berti', 21, '256325412', 'HBSIS')
cliente1.mostrar_dados()

cliente2 = Cliente('Luiz', 'Silva', 16, '458745874', 'Padaria do Zé')
cliente2.mostrar_dados()