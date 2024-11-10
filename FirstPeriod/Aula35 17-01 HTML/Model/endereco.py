class Endereco:
    codigo = 0
    logradouro = ''
    numero = int('0')
    sigla = ''
    cidade = ''
    bairro = ''
    cep = int('0')

    def __str__(self):
        return f'{self.codigo};{self.logradouro};{self.numero};{self.sigla};{self.cidade};{self.bairro};{self.cep}'

