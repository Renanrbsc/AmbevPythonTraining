#----- Importar bibliotecas de Mysql
import MySQLdb

def listar_todos():
    #----- configurar a conexâo
    conexao = MySQLdb.connect(host='127.0.0.1', database = 'CursoHBSIS', user = 'root')
    #----- Salvar o cursor da conexão em um variavel
    cursor = conexao.cursor()
    #----- Criacao do comando SQL e passado para o cursor
    comando_sql_select = "SELECT * FROM CLIENTE WHERE NOME LIKE 'S%'"
    cursor.execute(comando_sql_select)
    #----- pega o resultado do comando SQL e armazena em variavel
    resultado = cursor.fetchall()
    return resultado