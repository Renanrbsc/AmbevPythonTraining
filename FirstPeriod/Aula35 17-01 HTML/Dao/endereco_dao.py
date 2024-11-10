import MySQLdb
from Model.endereco import Endereco

class EnderecoDao:
    conexao = MySQLdb.connect(host = '127.0.0.1',
                              database = 'PadawanHBSIS',
                              user = 'root')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"SELECT * FROM ENDERECO"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def listar_por_id(self,id):
        comando_sql = f"SELECT * FROM ENDERECO WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, endereco:Endereco):
        comando_sql = f"""INSERT INTO ENDERECO
        (
            LOGRADOURO,
            NUMERO,
            SIGLA,
            CIDADE,
            BAIRRO,
            CEP
        )
        VALUES
        (
            '{endereco.logradouro}',
             {endereco.numero},
            '{endereco.sigla}',
            '{endereco.cidade}',
            '{endereco.bairro}',
             {endereco.cep}
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, endereco:Endereco):
        comando_sql = f"""UPDATE ENDERECO
        SET 
            LOGRADOURO = '{endereco.logradouro}',
            NUMERO = {endereco.numero},
            SIGLA = '{endereco.sigla}',
            CIDADE = '{endereco.cidade}',
            BAIRRO = '{endereco.bairro}',
            CEP = {endereco.cep}
        WHERE ID = {endereco.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self,id):
        comando_sql = f"""DELETE FROM ENDERECO WHERE ID = {id}"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()