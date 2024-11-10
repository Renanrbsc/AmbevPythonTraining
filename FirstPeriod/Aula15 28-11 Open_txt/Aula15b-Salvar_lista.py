
def salvar(linha):
    arquivo = open('TrabalhosPython/Aula15 28-11/cadastro_pessoa.txt','a')
    arquivo.write(linha+'\n')
    arquivo.close()

def ler():
    lista = []
    arquivo = open('TrabalhosPython/Aula15 28-11/cadastro_pessoa.txt','r')
    for linha in arquivo:
        lista.append(linha)
    arquivo.close()
    return lista

nome = input('Digite o nome: ')
sobrenome = input('Digite o sobrenome: ')
idade = int(input('Digite o idade: '))
pessoa = f'{nome};{sobrenome};{idade}'
salvar(pessoa)
print( ler() )


