from flask_restful import Resource

class PessoaDao(Resource):
    def __init__(self):
        self.connection = MySQLdb.connect(host='padawans16',database='mysql.padawans.dev',user='padawans16',passwd='lr2019')
        self.cursor = self.connectior.cursor()

    def list_all(self):
        self.cursor.execute('SELECT * FROM ')
        pessoas =
        return 'Listando todos os dados da tabela'

    def get_by_id(self, id):
        return f'Listando o dado de id: {id}'

    def insert(self, pessoa):
        return f'Cadastrando a pessoa {pessoa}'

    def update(self, pessoa):
        return f'Alterando a pessoa {pessoa}'

    def remove(self, id):
        return f'Deletando a pessoa de id: {id}'