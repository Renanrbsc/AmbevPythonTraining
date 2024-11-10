# Flask Restful

from flask import Flask
from flask_restful import Api
from Controllers.cerveja_controller import CervejaController

# GET -- SELECT
# POST -- CREATE
# PUT -- UPDATE
# DELETE -- DELETE
# API para uso desses metodos INSOMNIA, POSTMAN

app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/api/cerveja')


@app.route('/')
def inicio():
    return 'Bem vindo ao API'


app.run(debug=True, port=80)  # porta padrao do navegador 80



