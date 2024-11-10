# Aula 8 18-11-2019
# WEB

from flask import Flask

app = Flask(__name__)
@app.route('/') # rota principal do endereço web, sendo /
# def inicio():
#    return 'Bem vindos ao mundo real, meus quiridus'

def hello_world():
    return "Hello World! <strong>Bem vindos ao mundo real</strong>", 200


app.run()
# app.run(host='192.168.0.146', port=80')


