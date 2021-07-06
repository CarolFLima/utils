# coding: utf-8
from flask import Flask, render_template, redirect, url_for
from urllib.parse import urlparse

from flask.globals import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        url = urlparse(request.form['url'])
        params = url.query.split('&')
        return render_template('index.html', params=params)


if __name__ == '__main__':
    app.run(debug=True)

