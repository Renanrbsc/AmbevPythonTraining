from pessoa_base import PessoaBase

class Cliente(PessoaBase):

    def __init__(self, nome, sobrenome, idade,cpf, despezas):
        super().__init__(nome, sobrenome, idade)
        self.cpf = cpf
        self.despezas = despezas
        
    def mostrar_dados(self):
        print(f'{super().nome_completo()}\n'
              f'Idade: {super().idade}\n'
              f'{super().ano_de_nascimento()}\n'
              f'CPF: {self.cpf}\n'
              f'Valor a Pagar: R${self.despezas}\n')


cliente1 = Cliente('Renan', 'Berti', 21, '256325412', 1250.00)
cliente1.mostrar_dados()

cliente2 = Cliente('Luiz', 'Silva', 16, '458745874', 741.00)
cliente2.mostrar_dados()