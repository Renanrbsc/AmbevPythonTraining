# Aula 20 - 05-12-2019


# Surgiu a necessidade de envio massivo de e-mails dos clientes cadastrados
# no arquivo cadastro1.txt 

# >>>> Fazer tudo com metodos <<<<<

# 1 - Para isso o programa necessita que separe os clientes maiores de 20 anos 
# em um arquivo separado chamado menores_de_idade.txt

# 2 - Separar os clientes femininos e salvar em um arquivo chamado feminini.txt

# 3 - Fazer um terminal de consulta onde se digita o código cliente e 
# imprima na tela o (f-string) o codigo, nome, idade, sexo, email, telefone.
# Se digitar um número que não exista, deverá aparecer uma mensagem dizendo
# "código não encontrado!" Se digitar 'S' (sair) o programa deve finalizar.


def ler_cadastro():
    lista = []
    arquivo = open('TrabalhosPython\Aula20 05-12\exercicios\cadastro1.txt','r')
    for linha in arquivo:
        linha.strip()
        lista_linha = linha.split(';')
        dicionario = {'codigo':lista_linha[0],'nome':lista_linha[1],'idade':lista_linha[2],'sexo':lista_linha[3],'email':lista_linha[4],'telefone':lista_linha[5]}
        lista.append(dicionario)
    return lista

lista = ler_cadastro()
for i in lista:
    print(i)

