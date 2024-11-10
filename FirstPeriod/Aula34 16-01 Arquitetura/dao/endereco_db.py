import sys
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosPython/Aula34 16-01')

#----- Importar bibliotecas de Mysql
import MySQLdb
from model.endereco import Endereco

class EnderecoDb:
    #----- configurar a conexâo
    conexao = MySQLdb.connect(host='127.0.0.1', database = 'PadawanHBSIS', user = 'root')
    #----- Salvar o cursor da conexão em um variavel
    cursor = conexao.cursor()
    #----- Criacao do comando SQL e passado para o cursor
        
    def listar_todos(self):
        comando_sql_select = f"SELECT * FROM ENDERECO"
        self.cursor.execute(comando_sql_select)
        #----- pega o resultado do comando SQL e armazena em variavel
        resultado = self.cursor.fetchall()
        return self.converter_tabela_classe(resultado)

    def converter_tabela_classe(self,lista_tuplas):
        #----- Criação de lista de dicionarios que representa enderecos 
        lista_enderecos = []
        for i in lista_tuplas:
            dic_enderecos = {'ID':i[0],'LOGRADOURO':i[1],'NUMERO':i[2],'SIGLA':i[3],'CIDADE':i[4],
                        'BAIRRO':i[5],'CEP':i[6]}
            lista_enderecos.append(dic_enderecos)
        return lista_enderecos

