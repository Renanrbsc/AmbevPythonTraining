import MySQLdb
from Model.pessoa import Pessoa 

class PessoaDao:
    conexao = MySQLdb.connect(host = '127.0.0.1',
                              database = 'PadawanHBSIS',
                              user = 'root')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"SELECT * FROM CLIENTE AS C LEFT JOIN ENDERECO AS E ON C.ENDERECO_ID = E.ID"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def listar_por_id(self,id):
        comando_sql = f"SELECT * FROM CLIENTE AS C LEFT JOIN ENDERECO AS E ON C.ENDERECO_ID = E.ID WHERE C.CODIGO = {id}"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, pessoa:Pessoa):
        comando_sql = f"""INSERT INTO CLIENTE
        (
            NOME,
            SOBRENOME,
            IDADE,
            GENERO,
            EMAIL,
            TELEFONE,
            ENDERECO_ID
        )
        VALUES
        (
            '{pessoa.nome}',
            '{pessoa.sobrenome}',
             {pessoa.idade},
            '{pessoa.genero}',
            '{pessoa.email}',
            '{pessoa.telefone}',
             {pessoa.endereco.id}
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    # def alterar(self, pessoa:Pessoa):
    #     comando_sql = f"""UPDATE CLIENTE
    #     SET 
    #         NOME = '{pessoa.nome}',
    #         SOBRENOME = '{pessoa.sobrenome}',
    #         IDADE = {pessoa.idade},
    #         GENERO = '{pessoa.genero}',
    #         EMAIL = '{pessoa.email}',
    #         TELEFONE = '{pessoa.telefone}'
    #     WHERE CODIGO = {pessoa.id}
    #     """
    #     self.cursor.execute(comando_sql)
    #     self.conexao.commit()

    def alterar(self, pessoa:Pessoa, id):
        if pessoa.nome == '': # verifica a entrada web se for nula 
            comando = f"SELECT NOME FROM CLIENTE WHERE CODIGO = {id}"
            self.cursor.execute(comando) # busca e retorna valor ja existente no BD
            tupla = self.cursor.fetchone() # retorna como tupla de 2 valores
            pessoa.nome = tupla[0] # uso apenas a primeira posicao
        if pessoa.sobrenome == '':
            comando = f"SELECT sobrenome FROM CLIENTE WHERE CODIGO = {id}"
            self.cursor.execute(comando)
            tupla = self.cursor.fetchone()
            pessoa.sobrenome = tupla[0]
        if pessoa.idade == '':
            comando = f"SELECT idade FROM CLIENTE WHERE CODIGO = {id}"
            self.cursor.execute(comando)
            tupla = self.cursor.fetchone()
            pessoa.idade = tupla[0]
        if pessoa.genero == '':
            comando = f"SELECT genero FROM CLIENTE WHERE CODIGO = {id}"
            self.cursor.execute(comando)
            tupla = self.cursor.fetchone()
            pessoa.genero = tupla[0]
        if pessoa.email == '':
            comando = f"SELECT email FROM CLIENTE WHERE CODIGO = {id}"
            self.cursor.execute(comando)
            tupla = self.cursor.fetchone()
            pessoa.email = tupla[0]
        if pessoa.telefone == '':
            comando = f"SELECT telefone FROM CLIENTE WHERE CODIGO = {id}"
            self.cursor.execute(comando)
            tupla = self.cursor.fetchone()
            pessoa.telefone = tupla[0]

        comando_sql = f"""UPDATE CLIENTE 
        SET 
            NOME = '{pessoa.nome}',
            SOBRENOME = '{pessoa.sobrenome}',
            IDADE = {pessoa.idade},
            GENERO = '{pessoa.genero}',
            EMAIL = '{pessoa.email}',
            TELEFONE = '{pessoa.telefone}'
        WHERE CODIGO = {id}
        """ 
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self,id):
        comando_sql = f"DELETE FROM CLIENTE WHERE CODIGO = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        

    

