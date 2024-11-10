def listar_todos(c):
    cursor.execute('SELECT * FROM CLIENTE')
    pessoas = cursor.fetchall()
    for i in pessoas:
        print(f'{i}')

def listar_tudo(c):
    cursor.execute('SELECT * FROM CLIENTE AS C JOIN ENDERECO AS E WHERE C.ENDERECO_ID = E.ID')
    pessoas = cursor.fetchall()
    for i in pessoas:
        print(f'{i}')

def buscar_pessoa_id(c):
    id = input('Informe o codigo de cadastro do cliente: ')
    c.execute(f'SELECT * FROM CLIENTE WHERE ID = {id}')
    pessoa = c.fetchone()
    print(f'{pessoa}\n')

def buscar_tudo_id(c):
    id = input('Informe o codigo de cadastro do cliente: ')
    c.execute(f'SELECT * FROM CLIENTE AS C JOIN ENDERECO AS E WHERE C.ENDERECO_ID = E.ID AND C.ID = {id}')
    pessoa = c.fetchone()
    print(f'{pessoa}\n')

def menu():
    print('***************************************')
    print('* 1- Listar todas as pessoas          *')
    print('* 2- Listar pessoas com enderecos     *')
    print('* 3- Listar pessoas por ID            *')
    print('* 4- Listar pessoas e endereco por ID *')
    print('***************************************')
    print('Digite a opcao: ')
    
while True:
    menu()
    op = int(input())
    if op == 1:
        listar_todos(cursor)
    if op == 2:
        listar_tudo(cursor)
    if op == 3:
        buscar_pessoa_id(cursor)
    if op == 4:
        buscar_tudo_id(cursor)

