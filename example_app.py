import os
from flask import Flask
from flask import render_template
from flask import request
import conekta

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/index')
@app.route('/charge')
def charge():
    return render_template('charge.html')

@app.route('/charges', methods=["POST"])
def charge_create():
    conekta.api_key = 'key_eYvWV7gSDkNYXsmr'

    charge = conekta.Charge.create({
        'amount':request.form['amount'],
        'currency':'MXN',
        'description':request.form['description'],
        'card':request.form['token_id']
    })

    return render_template('charged_successfully.html', charge=charge)

