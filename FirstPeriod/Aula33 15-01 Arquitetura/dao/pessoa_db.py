import sys
sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosPython/Aula33 15-01 Arquitetura')
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosPython/Aula33 15-01 Arquitetura')

#----- Importar bibliotecas de Mysql
import MySQLdb
from model.pessoa import Pessoa

class PessoaDb:
    #----- configurar a conexâo
    conexao = MySQLdb.connect(host='127.0.0.1', database = 'PadawanHBSIS', user = 'root')
    #----- Salvar o cursor da conexão em um variavel
    cursor = conexao.cursor()
        
    def listar_por_like(self):
        print('----REFERENTE A TABELA CLIENTE----')
        column = input('Informe a coluna: ')
        posicao = int(input('Deseja buscar caracter em qual posicao? (1-inicio 2-meio 3-fim) '))
        like = input('Informe os caracteres: ')
        
        if posicao == 1:
            like_pos = f'{like}%'
        elif posicao == 2:
            like_pos = f'%{like}%'
        elif posicao == 3:
            like_pos = f'%{like}'
        else:
            print('Dados não informados!')
           
        #----- Criacao do comando SQL e passado para o cursor
        comando_sql_select = f"SELECT * FROM CLIENTE WHERE {column} LIKE '{like_pos}'"
        self.cursor.execute(comando_sql_select)
        #----- pega o resultado do comando SQL e armazena em variavel
        resultado = self.cursor.fetchall()
        return self.converter_tabela_classe(resultado)
     
    def converter_tabela_classe(self,lista_tuplas):
        #----- Criação de lista de dicionarios que representa pessoas 
        lista_pessoa = []
        for p in lista_tuplas:
            #----- Criação do objeto da classe pessoa
            p1 = Pessoa()
            #--- pega cada posição da tupla e atribui a uma chave do dicionário
            p1.codigo = p[0]
            p1.nome = p[1]
            p1.sobrenome= p[2]
            p1.idade = p[3]
            p1.genero = p[4]
            p1.email = p[5]
            p1.telefone = p[6]
            lista_pessoa.append(p1)
        return lista_pessoa
