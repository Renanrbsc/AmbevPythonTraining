class Pessoa():
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

nova_pessoa = Pessoa()
nova_pessoa.set_nome("Renan")

assert isinstance(nova_pessoa, Pessoa)
assert nova_pessoa.get_nome() == "Renan", "nome esta correto!"

# assert nova_pessoa.get_nome() == "Renannnnn", "nome não esta correto!"
# assert isinstance(nova_pessoa, Carro), "Nao é da classe carro"






