import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('tipos_basicos.html')

@app.route('/tipos/basicos')
def tipos_basicos():
    return render_template('tipos_basicos.html')

@app.route('/tipos/avancados')
def tipos_avancados():
    return render_template('tipos_avancados.html')

@app.route('/condicoes')
def condicoes():
    return render_template('condicoes.html')

@app.route('/lacos')
def lacos():
    return render_template('lacos.html')

@app.route('/poo')
def poo():
    return render_template('poo.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='127.0.0.1', port=port)