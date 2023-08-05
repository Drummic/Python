from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/miki')
def miki():
    return render_template('miki.html')

@app.route('/editText')
def editText():
    return render_template('editText.html')