def recebe_dados_endereco():
    lista = []
    arq = open('TrabalhosPython\Aula32 13-01\municipios.csv','r', encoding="utf8")
    for i in arq:
        if len(lista) < 1000:
            a = i.strip()
            lista_linha = a.split(';')
            lista.append(lista_linha)
        else:
            break
    arq.close()
    return lista

def recebe_dados_cliente():
    lista = []
    arq = open('TrabalhosPython\Aula32 13-01\sobrenome.txt','r', encoding="utf8")
    for i in arq:
        a = i.strip()
        #lista_linha = a.split(';')
        lista.append(a)
    arq.close()
    return lista

def insert_endereco_bd(cn,cr,lista):
    j = 1
    for i in lista:
        cr.execute(f"INSERT INTO ENDERECO (LOGRADOURO,NUMERO,SIGLA,CIDADE,BAIRRO,CEP) VALUES ('{i[0]}',{i[1]},'{i[3]}','{i[4]}','{i[5]}',{i[6]})")
        print(f'Linha inserida: {j} - ({i[0]},{i[1]},{i[3]},{i[4]},{i[5]},{i[6]})')
        j += 1
        cn.commit()

def insert_cliente_bd(cn,cr,lista):
    for i in lista:
        cr.execute(f"INSERT INTO CLIENTE (CODIGO,NOME,IDADE,GENERO,EMAIL,TELEFONE) VALUES ({i[0]},'{i[1]}',{i[2]},'{i[3]}','{i[4]}','{i[5]}')")
        print(f'Linha inserida: {i}')
        cn.commit()
 
def update_sobrenome(cn,cr,lista):
    j = 1
    for i in lista: 
        cr.execute(f"UPDATE CLIENTE SET SOBRENOME = '{i}' WHERE CODIGO = {j}")
        print(f'Linha atualizada: Codigo: {j} Sobrenome: {i}')
        j += 1
        cn.commit()

def update_endereco(cn,cr):
    for i in range (1,1001):
        cr.execute(f"UPDATE CLIENTE SET ENDERECO_ID = {i} WHERE CODIGO = {i}")
        print(f'Linha atualizada: Codigo: {i} ENDERECO_ID: {i}')
        cn.commit()

