from flask import Flask, render_template
import sys
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosPython/Aula34 16-01')
from controller.endereco_controller import EnderecoController

app = Flask(__name__)
pc = EnderecoController()

@app.route('/')
def inicio():
    enderecos = pc.listar_tudo()
    return render_template('index.html', lista = enderecos)

app.run()


