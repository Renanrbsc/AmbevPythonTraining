# Aula 15 - 28-11-2019
# Manipulação de arquivos e texto

arquivo = open('aula15.txt','r')
for linha in arquivo:
    print(linha)
arquivo.close()

###############################################################################

hello = input('Digite seu nome: ') # variavel recebe valor

arquivo = open('Nomes.txt','a') # abre o arquivo para anexar, cria se nao existir
arquivo.write(f'{hello}\n') # anexa valor da variavel com \n no arquivo
arquivo.close()

arquivo = open('Nomes.txt','r') # lendo arquivo Nomes
for linha in arquivo: # loop por linha no txt
    print(linha) # print valor em formato string

arquivo = open('Nomes.txt','r')
arquivo.write(f"")

####################################################################


