# Aula9 19-11-2019
# Web conceitos

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def inicia():
    return render_template('inicio.html')  

app.run()