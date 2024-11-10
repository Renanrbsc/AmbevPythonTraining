from Model.endereco import Endereco

class Pessoa:
    codigo: 0
    nome = None
    sobrenome = None
    idade = 0
    genero = None
    email = None
    telefone = None
    endereco = Endereco()
    
    def __str__(self):
        return f'{self.codigo};{self.nome};{self.sobrenome};{self.idade};{self.genero};{self.email};{self.telefone};{self.endereco.id}'