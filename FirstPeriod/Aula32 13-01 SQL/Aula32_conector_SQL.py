# install flask, flask_mysql, flask_mysqldb, sql

import MySQLdb
from Aula32_def_insert_txt import *

# conexao = MySQLdb.connect(host = 'mysql.topskills.study',
#                           database = 'topskills01',
#                           user = 'topskills01',
#                           passwd = 'ts2019')

conexao = MySQLdb.connect(host='127.0.0.1',
                          database='PadawanHBSIS',
                          user='root')

cursor = conexao.cursor()

# lista = recebe_dados_cliente()
# update_sobrenome(conexao,cursor,lista)
# insert_cliente_bd(conexao,cursor,lista)

# lista = recebe_dados_endereco()
# insert_endereco_bd(conexao,cursor,lista)

update_endereco(conexao, cursor)
