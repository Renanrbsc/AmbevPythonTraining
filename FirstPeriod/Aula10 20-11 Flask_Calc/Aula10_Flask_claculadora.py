# Aula 10 - 20-11-19
# 
# Web - Calculadora

nome_pagina = 'Calculadora sem calculo'
from flask import Flask, render_template, request
from calculos import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo=nome_pagina)

@app.route('/calcular')
def calcular():
    n1 = int(request.args['v1'])
    n2 = int(request.args['v2'])
    r_soma = calculo_soma(n1,n2)
    r_subtracao = calculo_sub(n1,n2)
    r_multiplicacao = calculo_mul(n1,n2)
    r_divisao_inteira = calculo_div_int(n1,n2)
    r_divisao_fracionada = calculo_div(n1,n2)
    r_resto = calculo_resto_div(n1,n2)
    r_raiz = calculo_raiz(n1,n2)
    resultados = {'soma':r_soma,'subtracao':r_subtracao,'mul':r_multiplicacao,'div':r_divisao_inteira,'div_frac':r_divisao_fracionada,'resto':r_resto,'raiz':r_raiz}
    

    return render_template('resultado.html',n1 = n1,n2 = n2,resultados = resultados)

app.run(host = '192.168.15.76')



