from flask_restful import Resource
from Dao.pessoa_dao import PessoaDao


class PessoaController(PessoaDao):
    def __init__(self):
        self.pessoa_dao = PessoaDao()

    def get(self, id=None):
        if id:
            return self.pessoa_dao.get_by_id(id)
        return self.pessoa_dao.list_all()

    def post(self):
        msg = self.pessoa_dao.insert('Olá')
        return msg

    def put(self):
        msg = self.pessoa_dao.update('Olá')
        return msg

    def delete(self, id):
        msg = self.pessoa_dao.remove(10)
        return msg