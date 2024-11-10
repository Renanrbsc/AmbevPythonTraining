import sys
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosPython/Aula34 16-01')

class Endereco:
    codigo = 0
    logradouro = ''
    numero = 0
    sigla = ''
    cidade = ''
    bairro = ''
    cep = 0

    def exportar_txt(self, lista_enderecos):
        #----- Criacao de arquivo.txt com base os dados da lista de dicionario
        with open('TrabalhosPython\Aula33 15-01\model\enderecos.txt','w') as arq:
            #----- Percorre a lista de dicionario e salva em arquivo txt
            for j in lista_enderecos:
                arq.write(f"{str(j)}\n")

    def __str__(self):
        return f'{self.codigo};{self.logradouro};{self.numero};{self.sigla};{self.cidade};{self.bairro};{self.cep}'
    
