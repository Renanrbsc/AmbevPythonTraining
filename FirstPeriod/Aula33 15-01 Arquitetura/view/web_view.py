from flask import Flask, render_template
import sys
sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosPython/Aula33 15-01 Arquitetura')
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosPython/Aula33 15-01 Arquitetura')
from controller.pessoa_controller import PessoaController

app = Flask(__name__)
pc = PessoaController()

@app.route('/')
def inicio():
    pessoas = pc.listar_por_like()
    return render_template('index.html', lista = pessoas)

app.run()