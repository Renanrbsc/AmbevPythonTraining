from flask import Flask, render_template,redirect ,request
from def_playlist import criar_faixa,ler_playlist, salvar_faixa

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html", nome = 'Lista de Faixas')
@app.route('/lista')
def listar_faixas():
    return render_template("lista.html", nome = 'Lista de Faixas', lista=ler_playlist())
@app.route('/salvar')
def salvar():
    musica = request.args['musica']
    album = request.args['album']
    artista = request.args['artista']
    faixa = criar_faixa(musica, album, artista)
    salvar_faixa(faixa)
    return redirect('/lista')


app.run()