# coding: utf-8
from flask import Flask, render_template, redirect, url_for
from urllib.parse import urlparse

from flask.globals import request

app = Flask(__name__)

class Parcela(): 
    def __init__(self, id, valor, saldo, amortizacao, juros):
        self.id = id
        self.valor = valor
        self.saldo = saldo
        self.amortizacao = amortizacao
        self.juros = juros


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        url = urlparse(request.form['url'])
        params = url.query.split('&')
        return render_template('index.html', params=params)


@app.route('/financiamento/', methods=['GET', 'POST'])
def financiamento():
    if request.method == 'GET':
        return render_template('amortizacao.html')
    if request.method == 'POST':
        valor = int(request.form['valor'])
        meses = int(request.form['meses'])
        juros_a = float(request.form['juros'])
        juros_m = ((1 + juros_a/100)**(1/12)) - 1

        parcelas = []
        saldo_d = valor 
        amortizacao_m = valor/meses
        for i in range(meses):
            juros_parcela = saldo_d * juros_m
            parcela_m = juros_parcela + amortizacao_m
            saldo_d = saldo_d - amortizacao_m
            parcela = Parcela(id=i+1, valor=round(parcela_m, 2), saldo=round(saldo_d, 2), amortizacao=round(amortizacao_m, 2), juros=round(juros_parcela, 2))
            parcelas.append(parcela)
            
            

        return render_template('amortizacao.html', parcelas=parcelas)


if __name__ == '__main__':
    app.run(debug=True)

