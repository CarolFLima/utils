from flask import Flask, render_template
from urllib.parse import urlparse


app = Flask(__name__)

@app.route('/')
def index():
    url = urlparse('apimhmllocal.intranet/api/appointment/v1/searchTimeSlot?addressId=1773&type=452')
    params = url.query.split('&')

    return render_template('index.html', params=params)

