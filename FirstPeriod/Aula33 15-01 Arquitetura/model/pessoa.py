import sys
sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosPython/Aula33 15-01 Arquitetura')
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosPython/Aula33 15-01 Arquitetura')

class Pessoa:
    codigo = 0
    nome = ''
    sobrenome = ''
    idade = 0
    genero = ''
    email = ''
    telefone = ''

    def exportar_txt(self, lista_pessoa):
        #----- Criacao de arquivo.txt com base os dados da lista de dicionario
        with open('TrabalhosPython\Aula33 15-01\model\pessoas.txt','w') as arq:
            #----- Percorre a lista de dicionario e salva em arquivo txt
            for j in lista_pessoa:
                arq.write(f"{str(j)}\n")

    def __str__(self):
        return f'{self.codigo};{self.nome};{self.sobrenome};{self.idade};{self.genero};{self.email};{self.telefone}'
  