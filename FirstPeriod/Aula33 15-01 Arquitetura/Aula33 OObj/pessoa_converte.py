def converter_tabela_dicionario(resultado):
    #----- Criação de lista de dicionarios que representa pessoas 
    lista_pessoa = []
    for i in resultado:
        dic_pessoa = {'CODIGO':i[0],'NOME':i[1],'SOBRENOME':i[2],'IDADE':i[3],
                      'GENERO':i[4],'EMAIL':i[5],'TELEFONE':i[6]}
        lista_pessoa.append(dic_pessoa)
    return lista_pessoa
