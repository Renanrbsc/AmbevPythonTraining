# Aula 41

# ciar uma nova pasta com o nome Aula 41
# Dentro dela criar uma novo virtualenv
# -- Voce pode usar o comando (no terminal)
# -- $> where python
# -- para achar o endereco do python
# virtualenv --python="caminho do python" teste-python

# criar uam aplicação flask que tenha os 4 metodos
# HTTP. Quando chamados retorne uma string
# A classe controller e a rota deve ser 'pessoa'

from flask import Flask, render_template
from flask_restful import Api
from Controllers.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)


api.add_resource(PessoaController, '/api/pessoa')


@app.route('/')
def inicio():
	msg = 'Bem vindo ao app'
	return render_template('index.html', msg = msg)


app.run(debug=True, port=80)  # porta padrao do navegador 80
